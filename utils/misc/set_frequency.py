from data.temporary_database import one_hour, three_hour, six_hour, twelve_hour, one_day, two_day, arcanas


def set_frequency(frequency, user_id):
    if user_id in one_hour:
        one_hour.remove(user_id)
    if user_id in three_hour:
        three_hour.remove(user_id)
    if user_id in six_hour:
        six_hour.remove(user_id)
    if user_id in twelve_hour:
        twelve_hour.remove(user_id)
    if user_id in one_day:
        one_day.remove(user_id)
    if user_id in two_day:
        two_day.remove(user_id)

    if frequency == '1 hour':
        one_hour.append(user_id)
    if frequency == '3 hour':
        three_hour.append(user_id)
    if frequency == '6 hour':
        six_hour.append(user_id)
    if frequency == '12 hour':
        twelve_hour.append(user_id)
    if frequency == '1 day':
        one_day.append(user_id)
    if frequency == '2 day':
        two_day.append(user_id)
