

def ask_amount():
    amount = input("Enter the amount to change: ")
    return amount

    # def amount_validator(amount_to_check, checking_of_amount=None):


def ask_original_measure():
    or_measure = input("Please enter the original measure: ")
    return or_measure


def ask_target_measure():
    measure = input("Please enter the target measure: ")
    return measure


def change_gram_to_kg(gram):
    return int(gram) / 1000


def change_kg_to_gram(kg):
    return int(kg) * 1000


def dkg_to_kg(dkg):
    return dkg * 100


def dkg_to_gram(dkg):
    return dkg * 10


def display_result(result):
    print(int(result))


def main():
    original = ask_original_measure()
    target = ask_target_measure()
    amount = ask_amount()
    if original == ('g' or original == "gram") and target == 'kg':
        gram_kg_result = change_gram_to_kg(amount)
        display_result(gram_kg_result)
    elif original == 'kg' and (target == 'g' or target == 'gram'):
        kg_to_gram = change_kg_to_gram(amount)
        display_result(kg_to_gram)


if __name__ == '__main__':
    main()
