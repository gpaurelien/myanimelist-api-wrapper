from src.mal import Mal
from src.settings import Identifier

mal = Mal()

items = mal.items.search('https://api.myanimelist.net/v2/anime', {'Authorization': f'Bearer {Identifier.ACCESS_TOKEN}'}, {'q': 'Naruto', 'limit': 10})