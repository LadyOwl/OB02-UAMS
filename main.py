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


