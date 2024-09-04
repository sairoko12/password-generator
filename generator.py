import secrets
import re
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class PasswordGenerator(object):
    length: int
    lower: Optional[bool] = True
    upper: Optional[bool] = True
    numbers: Optional[bool] = True
    symbols: Optional[bool] = True

    _pattern: str = field(init=False)
    _base_string: str = field(init=False)
    _available_chars: dict = field(default_factory=lambda: {
        'lower': 'abcdefghijklmnopqrstuvwxyz',
        'upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'numbers': '1234567890',
        'symbols': '!$%&@=._-,~≠/?+*#',
    })

    def __post_init__(self):
        if not any([self.lower, self.upper, self.numbers, self.symbols]):
            raise ValueError(
                'At least one of the options (lower, upper, numbers, or symbols) must be True.'
            )

        self._pattern = self._build_pattern()
        self._base_string = self._prepare_base_string()

    def _prepare_base_string(self) -> str:
        return ''.join(chars for key, chars in self._available_chars.items() if getattr(self, key))

    def _build_pattern(self) -> str:
        pattern = ''
        if self.lower:
            pattern += '(?=.*[a-z])'
        if self.upper:
            pattern += '(?=.*[A-Z])'
        if self.numbers:
            pattern += '(?=.*[0-9])'
        if self.symbols:
            pattern += '(?=.*[!$%&@=._-])'
        return pattern

    def _generate_password(self) -> str:
        password = []
        if self.lower:
            password.append(secrets.choice(self._available_chars['lower']))
        if self.upper:
            password.append(secrets.choice(self._available_chars['upper']))
        if self.numbers:
            password.append(secrets.choice(self._available_chars['numbers']))
        if self.symbols:
            password.append(secrets.choice(self._available_chars['symbols']))

        while len(password) < self.length:
            password.append(secrets.choice(self._base_string))

        secrets.SystemRandom().shuffle(password)
        return ''.join(password)

    def get(self) -> str:
        while True:
            result = self._generate_password()
            if not self._pattern or re.match(self._pattern, result):
                return result
