

def ask_amount():
    amount = input("Enter the amount to change: ")
    return amount

    # def amount_validator(amount_to_check, checking_of_amount=None):


def ask_original_measure():
    or_measure = input("original: ")
    return or_measure


def ask_target_measure():
    measure = input("add measure:")
    return measure


def change_gram_to_kg(gram):
    return int(gram) / 1000


def dkg_to_kg(dkg):
    return dkg * 100


def dkg_to_gram(dkg):
    return dkg * 10


def display_result(result):
    print(result)


def main():
    original = ask_original_measure()
    target = ask_target_measure()
    amount = ask_amount()
    if original == ('g' or original == "gram") and target == 'kg':
        gram_kg_result = change_gram_to_kg(amount)
        display_result(gram_kg_result)


if __name__ == '__main__':
    main()
