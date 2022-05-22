import random

chars = "!@#$%^&*()_+|№;:?/1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"


def main():
    size_password = random.randint(10, 20)
    password = ""
    for i in range(size_password):
        password += random.choice(chars)

    print(f"Your random password: {password}")


if __name__ == '__main__':
    main()
