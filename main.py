class User():
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

    


