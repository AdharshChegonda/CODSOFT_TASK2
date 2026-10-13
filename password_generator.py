import secrets
import string

print("===================================")
print("      PASSWORD GENERATOR")
print("===================================")

length = int(input("Enter password length: "))

if length < 4:
    print("Password length must be at least 4")

else:
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    characters = uppercase + lowercase + digits + symbols

    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    for i in range(length - 4):
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)

    generated_password = "".join(password)

    print("\nGenerated Password:", generated_password)
    print("Password Length:", len(generated_password))

    print("\nPassword Details:")
    print("Contains uppercase letters:", any(c.isupper() for c in generated_password))
    print("Contains lowercase letters:", any(c.islower() for c in generated_password))
    print("Contains numbers:", any(c.isdigit() for c in generated_password))
    print("Contains symbols:", any(c in symbols for c in generated_password))

    if length >= 12:
        print("Password strength: Strong")
    elif length >= 8:
        print("Password strength: Medium")
    else:
        print("Password strength: Short")
