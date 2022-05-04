from input_validation import *


class Account:
    __website = None
    __login_url = None
    __username = None
    __password = None
    __date_password_changed = None


    def __init__(self, website, login_url, username, password, date_password_changed):
        self.__website = website
        self.__login_url = login_url
        self.__username = username
        self.__password = password
        self.__date_password_changed = date_password_changed


    def run(self):
        pass


if __name__ == "__main__":
    app =



