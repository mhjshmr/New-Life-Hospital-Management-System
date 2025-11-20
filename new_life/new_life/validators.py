from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

def validate_file_size(value):
    filesize = value.size
    if filesize > 10485760:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")
    else:
        return value

phone_regex = RegexValidator(regex=r"^(\d{1,3}(-(\d{1,4}(-(\d{1,7}(-(\d{1,1})?)?)?)?)?)?)$", message="Emirates ID must be in format 111-1111-1111111-1")
