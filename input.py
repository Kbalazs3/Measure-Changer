
def ask_amount():
    amount = input("Enter the amount to change: ")
    return amount

    # def amount_validator(amount_to_check, checking_of_amount=None):


def ask_original_measure():
    or_measure = input("Please enter the original measure: ")
    return or_measure


def ask_target_measure():
    target_measure = input("Please enter the target measure: ")
    return target_measure


def ask_star_menu_command():
    start_menu_command = input("Start Menu command: ")
    return start_menu_command


def back_to_main_menu():
    back_to_menu = input('You can step back to the main menu by entering "back": ').lower()
    return back_to_menu
