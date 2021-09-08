

def display_result(result, amount, original_measure, target_measure):
    print(str(amount) + original_measure + " = " + str(float(result)) + target_measure)


def start_menu_display():
    to_middle = "\t\t\t\t"
    print(to_middle + to_middle +
          "Measure Changer" + "\n" + "START MENU" + "\n\n" + "Start -> Press S" + "\n"
          + "Description -> Press D" + "\n"
          "Quit -> Press Q" + "\n\n")
