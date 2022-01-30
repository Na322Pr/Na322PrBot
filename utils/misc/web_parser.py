import requests
from bs4 import BeautifulSoup

HERO = ['Ogre Magi',
        'Pudge',
        'Rubick',
        'Juggernaut',
        'Monkey King',
        'Zeus',
        'Crystal Maiden',
        'Phantom Assassin',
        'Shadow Fiend',
        'Techies',
        'Terrorblade',
        'Legion Commander',
        'Lina']

ARCANA_NAME = {
    'Ogre Magi': "Flockheart's Gamble",
    'Pudge': 'Feast of Abscession',
    'Rubick': 'The Magus Cypher',
    'Juggernaut': 'Bladeform Legacy',
    'Monkey King': "Great Sage's Reckoning",
    'Zeus': 'TempestHelm of the Thundergod',
    'Crystal Maiden': 'Frost Avalanche',
    'Phantom Assassin': 'Manifold Paradox',
    'Shadow Fiend': 'Demon Eater',
    'Techies': 'Swine of the Sunken Galley',
    'Terrorblade': 'Fractal Horns of Inner Abysm',
    'Legion Commander': 'Blades of Voth Domosh',
    'Lina': 'Fiery Soul of the Slayer'
}

ARCANA_LINK = {
    'Ogre Magi': "ogre_magi",
    'Pudge': 'pudge',
    'Rubick': 'rubick',
    'Juggernaut': 'juggernaut',
    'Monkey King': "monkey_king",
    'Zeus': 'zuus',
    'Crystal Maiden': 'crystal_maiden',
    'Phantom Assassin': 'phantom_assassin',
    'Shadow Fiend': 'nevermore',
    'Techies': 'techies',
    'Terrorblade': 'terrorblade',
    'Legion Commander': 'legion_commander',
    'Lina': 'lina'
}

ARCANA_PRICE = {
    'Ogre Magi': 0,
    'Pudge': 0,
    'Rubick': 0,
    'Juggernaut': 0,
    'Monkey King': 0,
    'Zeus': 0,
    'Crystal Maiden': 0,
    'Phantom Assassin': 0,
    'Shadow Fiend': 0,
    'Techies': 0,
    'Terrorblade': 0,
    'Legion Commander': 0,
    'Lina': 0
}


def get_html(url, params=None):
    return requests.get(url, params=params)


def set_data():
    for hero in HERO:
        url = 'https://steamcommunity.com/market/search?q=&category_570_Hero%5B%5D=tag_npc_dota_hero_' + ARCANA_LINK[
            hero] + '&category_570_Slot%5B%5D=any&category_570_Type%5B%5D=any&category_570_Rarity%5B%5D=tag_Rarity_Arcana&appid=570#p1_price_asc'
        html = get_html(url)

        if html.status_code == 200:
            print(f'Ok with {hero}')
            soup = BeautifulSoup(html.text, 'html.parser')
            items = soup.find_all('div',
                                  class_='market_listing_row market_recent_listing_row market_listing_searchresult')

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
                ARCANA_PRICE[hero] = min(prices)
            except:
                ARCANA_PRICE[hero] = 30.17
        else:
            print(f'Error with {hero}')


def get_hero_arcana_price(hero):
    if hero in HERO:
        return hero + ': ' + str(ARCANA_PRICE[hero])
    else:
        print('Error')


def get_all_arcana_prices():
    lst = []
    for hero in HERO:
        lst.append(f'Цена арканы на {hero}: {ARCANA_PRICE[hero]}$')
    return lst
