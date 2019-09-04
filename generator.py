# -*- coding: utf-8 -*-
import random
import re


class PasswordGenerator:
    def __init__(self, length, **kwargs):
        self.length = length
        self.available_chars = {
            'lower': "abcdefghijklmnopqrstuvwxyz",
            'upper': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            'numbers': "1234567890",
            'symbols': "!$%&@=._-"
        }

        self.base_string = self.prepare_base_string(**kwargs)
        self.regex = self.build_regex(**kwargs)

    def prepare_base_string(self, **kwargs):
        base_string = []

        for option in self.available_chars:
            if kwargs.get(option, True):
                base_string.append(self.available_chars[option])

        return "".join(base_string)

    def build_regex(self, **kwargs):
        must_lower = kwargs.get('must_lower', False)
        must_upper = kwargs.get('must_upper', False)
        must_number = kwargs.get('must_number', False)
        must_symbols = kwargs.get('must_symbols', False)

        symbols_regex = "[{}]".format(
            self.available_chars['symbols'])
        regex = None

        if must_symbols and (
                must_lower is False and
                must_upper is False and
                must_number is False):
            regex = symbols_regex
        elif must_lower or must_upper or must_number:
            regex = "[{opts}]"
            opts = []

            if must_lower and kwargs.get('lower', True):
                opts.append("a-z")

            if must_upper and kwargs.get('upper', True):
                opts.append("A-Z")

            if must_number and kwargs.get('numbers', True):
                opts.append("0-9")

            if len(opts) > 0:
                items = "".join(opts)

                if not must_symbols:
                    regex = regex.format(opts=items)
                else:
                    regex = "[{opts}]{symbols}" \
                        .format(opts=items, symbols=symbols_regex)
            else:
                regex = None

        return regex

    def get(self):
        if self.regex is not None:
            pattern = re.compile(self.regex)
            tries = 0

            while True:
                tries += 1
                result = "".join([
                    self.base_string[
                        random.randint(0,
                                       (len(self.base_string) - 1))
                    ] for i in range(0, self.length)])

                if pattern.match(result) or tries > 1000:
                    break

            return result
        else:
            return "".join([
                self.base_string[
                    random.randint(0,
                                   (len(self.base_string) - 1))
                ] for i in range(0, self.length)])
