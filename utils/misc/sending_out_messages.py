from loader import bot
from data.temporary_database import one_hour, arcanas
from utils.misc.web_parser import get_hero_arcana_price, set_data


async def send_message():
    set_data()
    for user in one_hour:
        s = ''
        for hero in arcanas[user]:
            s += get_hero_arcana_price(hero) + '\n'
        await bot.send_message(user, s)
