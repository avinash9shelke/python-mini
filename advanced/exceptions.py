# Errors and exceptions
class MyCustomError(Exception):
    """Custom exception for specific error cases."""
    pass


def check_value(x):
    if x < 0:
        raise MyCustomError("Negative value not allowed!")


try:
    check_value(-5)
except MyCustomError as e:
    print(f"Caught an error: {e}")

class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

def validate_age(age):
    if age < 0:
        raise ValidationError("age", "Age cannot be negative")

try:
    validate_age(-1)
except ValidationError as e:
    print(f"Validation failed on {e.field}: {e.message}")

