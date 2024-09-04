# Password generator

Script that create secure passwords with multiple options

## Usage

```python
from generator import PasswordGenerator

length_of_password = 25

secure_password = PasswordGenerator(length_of_password)

print("Your secure password is: {}".format(secure_password.get()))

# Create a password without lowercase letters
password = PasswordGenerator(length_of_password, lower=False)
print(password.get())

# Available options with default values
options = {
    'lower': True,
    'upper': True,
    'numbers': True,
    'symbols': True,
    'must_lower': False,
    'must_upper': False,
    'must_numbers': False,
    'must_symbols': False
}

password = PasswordGenerator(length_of_password, **options)
print(password.get())
```
