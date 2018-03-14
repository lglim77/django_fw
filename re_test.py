import re

def validate_phone_number(number):
    if not re.match(r'^01[016789][1-9]\d{6,7}$', number):
        return False
    # 후에 Form Validator에서는 forms.ValidationError예외를 발생시킴
    return True

print(validate_phone_number('01012341234')) # True
print(validate_phone_number('010123412')) # False
print(validate_phone_number('01012341234a')) # False
print(validate_phone_number('0101234123')) # True