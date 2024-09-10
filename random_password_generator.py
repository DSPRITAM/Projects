import string 
import random 


characters = list(string.ascii_letters + "@#$%&<>?" + string.digits )

def password_generate():
    password_length = int(input("How long, you like ? "))
    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)


option = input("Do you want to generate password : ").upper()


if option == "YES":
    password_generate()

elif option == "NO":
    print("Ok..")
    quit()

else:
    print("Please type correctly...only Yes or No")


