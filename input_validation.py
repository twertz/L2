# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def input_int(prompt=None, error=None, gt=None, ge=None, lt=None, le=None):
    if prompt is None:
        prompt = "Please enter an integer: "
    if error is None:
        error = "That is not an integer."

    while True:
        try:
            whole_number = int(input(prompt))
            if gt is not None and whole_number <= gt:
                print(F"Number must be greater than {gt}.")
                continue
            if ge is not None and whole_number < ge:
                print(F"Number must be greater than or equal to {ge}.")
                continue
            if lt is not None and whole_number >= lt:
                print(F"Number must be less than {lt}.")
                continue
            if le is not None and whole_number > le:
                print(F"Number must be less than or equal to {le}.")
                continue
            return whole_number
        except ValueError:
            print(error)


def input_float(prompt=None, error=None, gt=None, ge=None, lt=None, le=None):
    if prompt is None:
        prompt = "Please enter a float: "
    if error is None:
        error = "That is not a float."

    while True:
        try:
            float_number = float(input(prompt))
            if gt is not None and float_number <= gt:
                print(F"Number must be greater than {gt}.")
                continue
            if ge is not None and float_number < ge:
                print(F"Number must be greater than or equal to {ge}.")
                continue
            if lt is not None and float_number >= lt:
                print(F"Number must be less than {lt}.")
                continue
            if le is not None and float_number > le:
                print(F"Number must be less than or equal to {le}.")
            return float_number
        except ValueError:
            print(error)


def input_string(prompt=None, error=None, is_valid=None):
    if prompt is None:
        prompt = "Please enter a : "
    if error is None:
        error = "That doesn't seem like your favorite color."

    while True:
        string_input = input(prompt)
        if is_valid is None:
            while len(string_input.strip()) == 0:
                print(error)
                return input_string(prompt, error, is_valid)
            return string_input
        else:
            while not is_valid(string_input):
                print(error)
                return input_string(prompt, error, is_valid)
            return string_input


def y_or_n(prompt=None, error=None):
    if prompt is None:
        prompt = "Do you like turtles? (y)es/(n)o: "
    if error is None:
        error = "Please enter (y)es or (n)o"

    answers = ["yes", "y", "no", "n"]

    y_or_n_input = input(prompt).lower().strip()
    if y_or_n_input in answers:
        if y_or_n_input[0] == 'y':
            return True
        elif y_or_n_input[0] == 'n':
            return False
    else:
        print(error)
        return y_or_n(prompt, error)


def select_item(choices=None, prompt=None, error=None, dict=None):
    if prompt is None:
        prompt = "Please choose one item from the list."
    if choices is None:
        choices = ["Monday", "Tuesday", "Wednesday", "Thursday",
                   "Friday", "Saturday", "Sunday"]
    if error is None:
        error = "That isn't an available choice"

    print(choices)
    item_choice = input("Please choose an item from the list: ")
    while item_choice.lower() not in map(lambda x: x.lower(), choices):
        print(error)
        return select_item(choices, prompt, error)
    return item_choice


def input_value(input_type, **kwargs):
    if input_type == "int":
        input_int(**kwargs)
    if input_type == "float":
        input_float(**kwargs)
    if input_type == "str":
        input_string(**kwargs)
    if input_type == "y_or_n":
        y_or_n(**kwargs)
    if input_type == "list":
        select_item(**kwargs)
