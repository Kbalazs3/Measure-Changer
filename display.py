

def display_result(result, amount, original_measure, target_measure):
    print(str(amount) + original_measure + " = " + str(float(result)) + target_measure)


def start_menu_display():
    to_middle = "\t\t\t\t\t\t\t\t"
    print(2 * to_middle +
          "Measure Changer" + "\n\n" + 2 * to_middle + "START MENU" + "\n\n"+ 2 * to_middle + "Start -> Press S" + "\n"
          + 2 * to_middle + "Description -> Press D" + "\n"
          + 2 * to_middle + "Quit -> Press Q" + "\n\n")


def program_description_display():
    print("\n\n\nThis program can change, masses, lengths, time, speed\n\n")
