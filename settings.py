# ノーマル、炎、水、草、電気、氷、格闘、毒
# 地面、飛行、エスパー、虫、岩、ゴースト、ドラゴン、悪、鋼、フェアリー
pokemon_types = [
  {
    'index': 1,
    'en': 'normal',
    'ja': 'ノーマル'
  },
  {'index': 2, 'en': 'fire', 'ja': '炎'},
  {'index': 3, 'en': 'water', 'ja': '水'},
  {'index': 4, 'en': 'grass', 'ja': '草'},
  {'index': 5, 'en': 'electric', 'ja': '電気'},
  {'index': 6, 'en': 'ice', 'ja': '氷'},
  {'index': 7, 'en': 'fighting', 'ja': '格闘'},
  {'index': 8, 'en': 'poison', 'ja': '毒'},
  {'index': 9, 'en': 'ground', 'ja': '地面'},
  {'index': 10, 'en': 'flying', 'ja': '飛行'},
  {'index': 11, 'en': 'psychic', 'ja': 'エスパー'},
  {'index': 12, 'en': 'bug', 'ja': '虫'},
  {'index': 13, 'en': 'rock', 'ja': '岩'},
  {'index': 14, 'en': 'ghost', 'ja': 'ゴースト'},
  {'index': 15, 'en': 'dragon', 'ja': 'ドラゴン'},
  {'index': 16, 'en': 'dark', 'ja': '悪'},
  {'index': 17, 'en': 'steel', 'ja': '鋼'},
  {'index': 18, 'en': 'fairy', 'ja': 'フェアリー'} 
]

types_compatibilities = [
  {1:
    {
      'compatible': [],
      'incompatible': [7],
      'none': [14]
    }
  },
]