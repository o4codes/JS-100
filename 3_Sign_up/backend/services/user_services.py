import json
from schema.user import User

# note: emails will be unique


class UserServices:
    def __init__(self, db_path):
        self.__db_path = db_path

    def get_db_path(self):
        return self.__db_path

    def set_db_path(self, db_path):
        self.__db_path = db_path

    def read_db(self, email:str = None):
        """Reads the content of the user db

        Args:
            email (str, optional): [description]. Defaults to None.

        Returns:
            [list]: list of users when no email is supplied
            [dict]: user object when email is supplied
        """
        try:
            with open(self.__db_path, "r") as file:
                users = json.load(file)
                if email:
                    user = list(filter(lambda user: user["email"] == email, users))
                    if user == []:
                        return None
                    return user[0]
                return users
                
        except FileNotFoundError:
            users = []
            with open(self.__db_path, "w") as file:
                json.dump(users, file)
                return users
            
    def sign_up(self, user: User):
        """Signs up a user

        Args:
            user (User): user object
            
        Returns:
            [bool]: True if user is signed up, False otherwise
        """
        users = self.read_db()
        user_read = self.read_db(email=user.email)
        if user_read:
            return False

        users.append(user.dict())
        with open(self.__db_path, "w") as file:
            json.dump(users, file)
            return True
            
