

def to_middle():
    return "\t\t\t\t\t\t\t\t"


def display_result(result, amount, original_measure, target_measure):
    middle = to_middle()
    print("\n" + 2 * middle + str(amount) + original_measure + " = " + str(float(result)) + target_measure)


def start_menu_display():
    middle = to_middle()
    print("\n" + 2 * middle +
          "Measure Changer" + "\n\n" + 2 * middle + "START MENU" + "\n\n"+ 2 * middle + "Start -> Press S" + "\n"
          + 2 * middle + "Description -> Press D" + "\n"
          + 2 * middle + "Quit -> Press Q" + "\n\n")


def program_description_display():
    middle = to_middle()
    print("\n\n\n" + middle + "This program can change, masses, lengths, time, speed\n\n")
