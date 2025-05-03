from utils.file_manager import read, write



def show_all_admins():
    users = read(filename="users.csv")
    admins = [user for user in users if user[3] == "admin"]
    if admins:
        for admin in admins:
            print(f"Admin: {admin[1]} - {admin[2]}")
    else:
        print("No admins found!")



def create_admin():
    username = input("Enter admin's name: ")
    password = input("Enter admin's password: ")
    phone_number = input("Enter admin's phone number: ")

    # Ensure user doesn't already exist
    users = read(filename="users.csv")
    if any(user[1] == phone_number for user in users):
        print("Admin with this phone number already exists!")
        return


    new_admin = [len(users) + 1, username, password, "admin", phone_number, 0]
    users.append(new_admin)
    write(filename="users.csv", data=users)
    print(f"Admin {username} created successfully!")



def delete_admin():
    phone_number = input("Enter admin's phone number to delete: ")
    users = read(filename="users.csv")

    admin_to_delete = None
    for user in users:
        if user[1] == phone_number and user[3] == "admin":
            admin_to_delete = user
            break

    if admin_to_delete:
        users.remove(admin_to_delete)
        write(filename="users.csv", data=users)
        print(f"Admin {admin_to_delete[1]} deleted successfully!")
    else:
        print("Admin not found!")



def show_statistics():
    users = read(filename="users.csv")
    total_users = len(users)
    total_admins = len([user for user in users if user[3] == "admin"])
    print(f"Total users: {total_users}")
    print(f"Total admins: {total_admins}")
