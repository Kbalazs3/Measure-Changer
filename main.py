import mass
import length
import speed
import time_changer
import display
import input


def start_menu():
    display.start_menu_display()
    s_menu_c = input.ask_star_menu_command().lower()
    print("\n")
    if s_menu_c in ['s', 'start']:
        main()
    elif s_menu_c in ['d', 'description']:
        program_description()
    elif s_menu_c in ['q', 'quit']:
        quit(0)


def program_description():
    display.program_description_display()
    back_to_main = input.back_to_main_menu()
    if back_to_main == 'back':
        start_menu()


def main():
    original = input.ask_original_measure().lower()
    target = input.ask_target_measure()
    amount_to_change = input.ask_amount()

    # Mass
    if original == ('g' or original == "gram") and target == 'kg':
        gram_kg_result = mass.change_gram_to_kg(amount_to_change)
        display.display_result(gram_kg_result, amount_to_change, original, target)
    elif original == 'kg' and (target == 'g' or target == 'gram'):
        kg_to_gram = mass.change_kg_to_gram(amount_to_change)
        display.display_result(kg_to_gram, amount_to_change, original, target)
    elif original == 'dkg' and target == 'kg':
        dkg_to_kg_result = mass.dkg_to_kg(amount_to_change)
        display.display_result(dkg_to_kg_result, amount_to_change, original, target)
    elif original == 'kg' and target == 'dkg':
        kg_to_dkg_result = mass.kg_to_dkg(amount_to_change)
        display.display_result(kg_to_dkg_result, amount_to_change, original, target)
    # Lengths
    elif original == 'm' and target == 'cm':
        m_to_cm_result = length.m_to_cm(amount_to_change)
        display.display_result(m_to_cm_result, amount_to_change, original, target)
    elif original == 'cm' and target == 'm':
        cm_to_m_result = length.m_to_cm(amount_to_change)
        display.display_result(cm_to_m_result, amount_to_change, original, target)
    elif original == 'cm' and target == 'dm':
        cm_to_dm_result = length.cm_to_dm(amount_to_change)
        display.display_result(cm_to_dm_result, amount_to_change, original, target)
    elif original == 'dm' and target == 'cm':
        dm_to_cm_result = length.dm_to_cm(amount_to_change)
        display.display_result(dm_to_cm_result, amount_to_change, original, target)
    elif original == 'm' and target == 'km':
        m_to_km_result = length.m_to_km(amount_to_change)
        display.display_result(m_to_km_result, amount_to_change, original, target)
    elif original == 'km' and target == 'm':
        km_to_m_result = length.m_to_km(amount_to_change)
        display.display_result(km_to_m_result, amount_to_change, original, target)
    # Speed
    elif original == 'km/h' and target == 'm/sec':
        km_per_hour_to_m_per_sec = speed.km_per_hour_tom_per_sec(amount_to_change)
        display.display_result(km_per_hour_to_m_per_sec, amount_to_change, original, target)
    elif original == 'm/sec' and target == 'km/h':
        m_per_sec_to_km_per_hour = speed.km_per_hour_tom_per_sec(amount_to_change)
        display.display_result(m_per_sec_to_km_per_hour, amount_to_change, original, target)
    # Time
    elif (original == 'sec' or original== 'second') and (target == 'min' or target == 'minute'):
        sec_to_min_result = time_changer.sec_to_minute(amount_to_change)
        display.display_result(sec_to_min_result, amount_to_change, original, target)
    elif (original == 'min' or original == 'minute') and (target == 'sec' or target == 'second'):
        min_to_sec_result = time_changer.minute_to_sec(amount_to_change)
        display.display_result(min_to_sec_result, amount_to_change, original, target)
    elif original in ['quit', 'Quit'] or target in ['quit', 'Quit']:
        exit(0)


if __name__ == '__main__':
    start_menu()
    main()
