from loader import bot
from data.temporary_database import one_hour, three_hour, six_hour, twelve_hour, one_day, two_day, arcanas
# from utils.misc.web_parser import get_hero_arcana_price, set_data
from utils.misc.web_parser import get_hero_arcana_price


async def send_out_message(time_counter):
    lst = one_hour[:]
    if time_counter % 3 == 0:
        lst += three_hour
    if time_counter % 6 == 0:
        lst += six_hour
    if time_counter % 12 == 0:
        lst += twelve_hour
    if time_counter % 24 == 0:
        lst += one_day
    if time_counter % 48 == 0:
        lst += two_day

    for user in lst:
        s = ''
        for hero in arcanas[user]:
            s += f'{hero}: {str(get_hero_arcana_price(hero))}\n'
        await bot.send_message(user, s)
