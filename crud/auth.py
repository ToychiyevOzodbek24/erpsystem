from utils.file_manager import read, write

super_admin_login = "superadmin"
super_admin_password = "superadmin"

def login():
    user_login = input("Enter your phone number: ")
    password = input("Enter your password: ")

    if user_login == super_admin_login and password == super_admin_password:
        print("Welcome boss!")
        return "super_admin"

    users = read(filename="data/users.csv")
    for index, user in enumerate(users):
        if user[1] == user_login and user[2] == password:
            role = user[3]
            users[index][-1] = "1"
            write(filename="data/users.csv", data=users)
            print(f"Welcome, {user[1]} ({role})")
            return role

    print("Wrong phone number or password.")
    return False


def logout():
    users = read(filename="data/users.csv")
    for index in range(len(users)):
        users[index][-1] = "0"
    write(filename="data/users.csv", data=users)
