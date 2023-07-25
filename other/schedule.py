def decode_schedule(schedule):
    # Convert the schedule to binary, remove the "0b" prefix, and pad with zeros to get 7 bits
    binary_schedule = bin(schedule)[2:].zfill(7)

    # Define the days of the week
    days = ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "НД"]

    # Decode the schedule
    decoded_schedule = {day: ("+" if bit == "1" else "-") for day, bit in zip(days, binary_schedule)}

    return decoded_schedule


for schedule in range(0,128):
    decoded_schedule = decode_schedule(schedule)
    print(f'schedule = {schedule}: {decoded_schedule}')