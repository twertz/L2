import datetime
import time
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

    def __str__(self):
        return f"Website: {self.__website} has Username: {self.__username} "

    def get_website(self):
        return self.__website

    def set_website(self, website):
        self.__website = website

    def get_login_url(self):
        return self.__login_url

    def set_login_url(self, login_url):
        self.__login_url = login_url

    def get_username(self):
        return self.__username

    def set_username(self, user_name):
        self.__username = user_name

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password
        self.__date_password_changed = datetime.datetime.now()

    def get_date_time(self):
        return self.__date_password_changed.strftime("%m-%d-%Y %H:%M:%S")

class TwoFactorAccount(Account):
    __two_factor_type = None
    __two_factor_answer = None

    def __init__(self, two_factor_type, two_factor_answer, *args, **kwargs):
        self.__two_factor_type = two_factor_type
        self.__two_factor_answer = two_factor_answer
        super().__init__(*args, **kwargs)

    def get_two_factor_type(self):
        return self.__two_factor_type

    def set_two_factor_type(self, two_factor_type):
        self.__two_factor_type = two_factor_type

    def get_two_factor_answer(self):
        return self.__two_factor_answer

    def set_two_factor_answer(self, two_factor_answer):
        self.__two_factor_answer = two_factor_answer


if __name__ == "__main__":
    app = Account("google", "www.gmail.com", "twertz", "checkmeout", datetime.datetime.now())
    app2 = TwoFactorAccount("pin", 241015, "hotmail", "www.hotmail.com", "wertzt", "outmecheck", datetime.datetime.now())
    print(app.get_website())
    print(app.get_login_url())
    print(app.get_username())
    print(app.get_password())
    print(app.get_date_time())
    time.sleep(2)
    app.set_password("updatedShit")
    print(app.get_password())
    print(app.get_date_time())
    print(app2.get_website())
    print(app2.get_login_url())
    print(app2.get_username())
    print(app2.get_password())
    print(app2.get_date_time())
    time.sleep(1)
    print(app2.get_date_time())
    print(app2.get_two_factor_type())
    print(app2.get_two_factor_answer())
    print(app2)