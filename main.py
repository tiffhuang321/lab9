
def encode(n):
    encode = []

    for number in n:
        number = int(number) + 3
        if number >= 10:
            encode.append(str(number - 10))
        else:
            encode.append(str(number))

    return "".join(encode)


def decode():
    print("The encoded password is " + encoded + ", and the original password is " + password + ".\n")


if __name__ == "__main__":
    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quite\n")

        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!\n")

        if option == "2":
            decode()

        if option == "3":
            break
