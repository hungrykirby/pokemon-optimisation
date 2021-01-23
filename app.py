import settings


def get_type_info(pokemon_type):
  i = [t for t in settings.pokemon_types if t['index'] == pokemon_type]
  return i[0] if i else None

def get_type_relation(pokemon_type):
  i = [t for t in settings.types_compatibilities if list(t.keys())[0] == pokemon_type]
  if i:
    return i[0][pokemon_type]
  else:
    return None

p_t = 1
print(get_type_info(p_t)['ja'] + 'の弱点は')
cs = get_type_relation(p_t)

for c in cs['incompatible']:
  print(get_type_info(c)['ja'])