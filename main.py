class User:
    def __init__(self, user_id, name ):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = "user"

    def get_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, new_name):
        self.__name = new_name

    def set_id(self, new_id):
        self.__user_id = new_id

    def __str__(self):
        return f"User ID: {self.__user_id}\nName: {self.__name}\nAccess Level: {self.__access_level}\n"

class Admin(User):
    def __init__(self, user_id, name, admin_level):
        super().__init__(user_id, name)
        self.__admin_level = admin_level
        self.__access_level = "admin"

    def get_admin_level(self):
        return self.__admin_level

    def get_access_level(self):
        return self.__access_level

    def set_admin_level(self, level):
        self.__admin_level = level

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"Admin {self.get_name()} added user {user.get_name()} with ID {user.get_id()}")

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_id() == user_id:
                user_list.remove(user)
                print(f"Admin {self.__name} removed user with ID {user_id}")
                return
        print(f"User with ID {user_id} not found")

    def __str__(self):
        return f"User ID: {self.__user_id}\nName: {self.__name}\nAccess Level: {self.__access_level}\nAdmin Level: {self.__admin_level}\n"



user_list = []

user1 = User(1, "Anastasya")
user2 = User(2, "Valeriy")
user3 = User(3, "Alexandr")
user4 = User(4, "Irina")

user_list.append(user1)
user_list.append(user2)
user_list.append(user3)
user_list.append(user4)

print("User list:")
for user in user_list:
    print(user)