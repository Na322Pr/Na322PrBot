import asyncio

import aiohttp
from bs4 import BeautifulSoup

arcanas_data = {
    'Ogre Magi': {'price': 200.0, 'link': 'ogre_magi'},
    'Pudge': {'price': 200.0, 'link': 'pudge'},
    'Rubick': {'price': 200.0, 'link': 'rubick'},
    'Juggernaut': {'price': 200.0, 'link': 'juggernaut'},
    'Monkey King': {'price': 200.0, 'link': 'monkey_king'},
    'Zeus': {'price': 200.0, 'link': 'zuus'},
    'Crystal Maiden': {'price': 200.0, 'link': 'crystal_maiden'},
    'Phantom Assassin': {'price': 200.0, 'link': 'phantom_assassin'},
    'Shadow Fiend': {'price': 200.0, 'link': 'nevermore'},
    'Techies': {'price': 200.0, 'link': 'techies'},
    'Terrorblade': {'price': 200.0, 'link': 'terrorblade'},
    'Legion Commander': {'price': 200.0, 'link': 'legion_commander'},
    'Lina': {'price': 200, 'link': 'lina'}
}


async def get_page_data(session, hero):
    url = f'https://steamcommunity.com/market/search?q=&category_570_Hero%5B%5D=tag_npc_dota_hero_{arcanas_data[hero]["link"]}&category_570_Slot%5B%5D=any&category_570_Type%5B%5D=any&category_570_Rarity%5B%5D=tag_Rarity_Arcana&appid=570#p1_price_asc'

    async with session.get(url=url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_='market_listing_row market_recent_listing_row market_listing_searchresult')

        prices = []

        for item in items:
            name = item.find('span', class_='market_listing_item_name').get_text()
            price = float(
                item.find('span', class_='market_table_value normal_price').find('span',
                                                                                 class_='normal_price').get_text()[
                1:-4].replace(',', ''))

            if 'Voice' not in name and 'Bundle' not in name and 'Call' not in name:
                prices.append(price)
        try:
            arcanas_data[hero]['price'] = min(prices)
        except:
            pass
        print(f'Ok {hero}')


async def gather_data():
    async with aiohttp.ClientSession() as session:
        tasks = []

        for hero in arcanas_data.keys():
            task = asyncio.create_task(get_page_data(session, hero))
            tasks.append(task)

        await asyncio.gather(*tasks)


def get_hero_arcana_price(hero):
    try:
        return arcanas_data[hero]['price']
    except:
        pass
