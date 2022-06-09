import Account


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
