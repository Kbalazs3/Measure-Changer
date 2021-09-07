import mass
import length
import display
import input


def main():
    original = input.ask_original_measure().lower()
    target = input.ask_target_measure()
    amount = input.ask_amount()
    if original == ('g' or original == "gram") and target == 'kg':
        gram_kg_result = mass.change_gram_to_kg(amount)
        display.display_result(gram_kg_result, amount, original, target)
    elif original == 'kg' and (target == 'g' or target == 'gram'):
        kg_to_gram = mass.change_kg_to_gram(amount)
        display.display_result(kg_to_gram, amount, original, target)
    elif original == 'dkg' and target == 'kg':
        dkg_to_kg_result = mass.dkg_to_kg(amount)
        display.display_result(dkg_to_kg_result, amount, original, target)
    elif original == 'kg' and target == 'dkg':
        kg_to_dkg_result = mass.kg_to_dkg(amount)
        display.display_result(kg_to_dkg_result, amount, original, target)
    elif original == 'm' and target == 'cm':
        m_to_cm_result = length.m_to_cm(amount)
        display.display_result(m_to_cm_result, amount, original, target)


if __name__ == '__main__':
    main()
