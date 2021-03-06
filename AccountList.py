from Account import Account, TwoFactorAccount
import datetime


class AccountList:
    __list_name = None
    __security_scale = None

    def __init__(self, list_name, security_scale):
        self.account_list = []
        self.__list_name = list_name
        self.__security_scale = security_scale

    def add_account(self, account):
        self.account_list.append(account)

    def show_account_list(self):
        print(f"The {self.__list_name} list with security importance {self.__security_scale} contains the following "
              f"accounts: ")
        for item in self.account_list:
            print(item)


if __name__ == "__main__":
    list1 = AccountList("work", 7)
    app = Account("google", "www.gmail.com", "twertz", "checkmeout", datetime.datetime.now())
    app2 = TwoFactorAccount("pin", 241015, "hotmail", "www.hotmail.com", "wertzt", "outmecheck",
                            datetime.datetime.now())
    list1.add_account(app)
    list1.add_account(app2)
    list1.show_account_list()

    print(app2.get_password())
