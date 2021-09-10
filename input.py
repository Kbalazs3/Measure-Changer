

def ask_amount():
    amount = input("\t\t\t\t\t\t\t\t\t\tEnter the amount to change: ")
    return amount


def ask_original_measure():
    or_measure = input("\t\t\t\t\t\t\t\t\t\tPlease enter the original measure: ")
    return or_measure


def ask_target_measure():
    target_measure = input("\t\t\t\t\t\t\t\t\t\tPlease enter the target measure: ")
    return target_measure


def ask_star_menu_command():
    start_menu_command = input("\t\t\t\t\t\t\t\t\t\tStart Menu command: ")
    return start_menu_command


def back_to_main_menu():
    back_to_menu = input('\t\t\t\t\t\t\t\t\t\tYou can step back to the main menu by entering "back": ').lower()
    return back_to_menu
