

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


def change_gram_to_kg(gram):
    return int(gram) / 1000


def change_kg_to_gram(kg):
    return int(kg) * 1000


def dkg_to_kg(dkg):
    return int(dkg) / 100


def dkg_to_gram(dkg):
    return dkg * 10


def display_result(result, amount, original_measure, target_measure):
    print(str(amount) + original_measure + " = " + str(int(result)) + target_measure)


def main():
    original = ask_original_measure()
    target = ask_target_measure()
    amount = ask_amount()
    if original == ('g' or original == "gram") and target == 'kg':
        gram_kg_result = change_gram_to_kg(amount)
        display_result(gram_kg_result, amount, original, target)
    elif original == 'kg' and (target == 'g' or target == 'gram'):
        kg_to_gram = change_kg_to_gram(amount)
        display_result(kg_to_gram, amount, original, target)
    elif original == 'dkg' and target == 'kg':
        dkg_to_kg_result = dkg_to_kg(amount)
        display_result(dkg_to_kg_result, amount, original, target)


if __name__ == '__main__':
    main()
