

def can(book,start, end):
    if start==end:
        return True
    elif start==None:
        return False
    g=False
    if start in book:
        for val in book[start]:
            g=g or can(book,val, end)
    return g

book1 = {
    "squirtle" : ["wartortle"],
    "wartortle" : ["blastoise"],
    "blastoise" : [],
    "charmander" : ["charmeleon"],
    "charmeleon" : ["charizard"],
    "charizard" : [],
    "bulbasaur" : ["ivysaur"],
    "ivysaur" : ["venusaur"],
    "venusaur" : []
}

book2 = {
    "eevee" : ["jolteon", "flareon", "vaporeon"],
    "jolteon" : ["zapdos"],
    "vaporeon" : ["articuno"],
    "flareon" : ["moltres"]
}

book3 = {
    'cubone': ['dragonite', 'magmar', 'tangela'],
    'krabby': ['vaporeon', 'chansey', 'zapdos', 'electabuzz'],
    'spearow': ['mewtwo', 'seadra', 'tentacool'],
    'primeape': ['weepinbell', 'hitmonchan', 'mew', 'porygon', 'dewgong'],
    'snorlax': ['moltres', 'dragonair', 'dratini', 'mewtwo', 'mew'],
    'wartortle': ['rattata', 'weepinbell', 'seaking'],
    'flareon': ['porygon', 'dratini', 'articuno'],
    'clefairy': ['staryu'],
    'rattata': ['bellsprout', 'nidorino'],
    'machoke': ['staryu', 'bellsprout'],
    'vileplume': ['doduo', 'victreebel', 'machop', 'starmie', 'kabuto'],
    'dugtrio': ['golem', 'kadabra', 'rapidash', 'hitmonchan', 'aerodactyl'],
    'venusaur': [],
    'bulbasaur': [],
    'onix': ['horsea'],
    'weezing': ['snorlax'],
    'beedrill': ['grimer', 'bellsprout', 'clefable', 'arbok'],
    'butterfree': ['persian', 'dragonair', 'machop', 'starmie', 'dodrio'],
    'charmeleon': ['oddish', 'seel', 'persian', 'seaking', 'poliwrath'],
    'paras': ['seadra'],
    'raticate': ['raichu', 'voltorb', 'sandshrew'],
    'gyarados': ['articuno', 'moltres', 'flareon', 'dratini'],
    'mr.mime': [],
    'kabutops': ['dragonite', 'aerodactyl', 'mewtwo', 'dragonair'],
    'poliwhirl': ['golem', 'graveler', 'magikarp', 'electabuzz', 'mr.mime'],
    'muk': ['tauros', 'omanyte', 'mewtwo', 'electrode', 'cubone'],
    'rapidash': ['gyarados', 'electrode'],
    'golem': [],
    'rhydon': ['jynx'],
    'zapdos': ['dragonair', 'mewtwo', 'dratini'],
    'golduck': ['hypno', 'dewgong', 'jolteon', 'poliwag'],
    'gengar': ['jolteon', 'seaking', 'jynx'],
    'arcanine': [],
    'mew': [],
    'gloom': [],
    'vulpix': ['wigglytuff'],
    'articuno': ['mew', 'zapdos', 'dragonair'],
    'ponyta': ['eevee', 'tauros', 'mr.mime', 'horsea'],
    'pinsir': ['ditto', 'zapdos'],
    'grimer': ['kabutops'],
    'nidoqueen': [],
    'tangela': ['horsea', 'scyther', 'pinsir', 'kabutops', 'mewtwo'],
    'ivysaur': ['marowak', 'krabby', 'growlithe'],
    'electabuzz': ['gyarados', 'ditto', 'kabutops', 'porygon'],
    'weedle': ['raichu', 'mew', 'snorlax', 'voltorb'],
    'omanyte': ['mewtwo', 'zapdos'],
    'magnemite': [],
    'marowak': ['dratini', 'porygon', 'kabutops', 'goldeen'],
    'pidgey': [],
    'dragonair': [],
    'poliwag': [],
    'magikarp': ['articuno', 'kabutops', 'lapras', 'mew'],
    'fearow': ['omastar'],
    'slowpoke': ['koffing', 'farfetchd', 'hypno', 'krabby', 'gengar'],
    'starmie': ['dragonite', 'magikarp', 'scyther'],
    'ekans': ['slowbro', 'paras', 'electrode', 'rapidash'],
    'meowth': ['dodrio', 'poliwrath', 'ditto', 'tentacool', 'aerodactyl'],
    'raichu': [],
    'kabuto': ['aerodactyl', 'articuno', 'kabutops'],
    'charizard': [],
    'oddish': ['flareon', 'horsea', 'drowzee', 'tauros'],
    'wigglytuff': ['dragonite', 'oddish'],
    'pidgeot': ['seel', 'bellsprout'],
    'hitmonlee': ['seaking', 'mew', 'gyarados'],
    'charmander': [],
    'mewtwo': ['mew'],
    'bellsprout': ['tauros', 'gengar', 'electabuzz', 'ponyta'],
    'hypno': ['flareon'],
    'kadabra': [],
    'nidoking': ['venonat', 'muk', 'farfetchd', 'zubat', 'articuno'],
    'sandslash': ['gyarados', 'golbat', 'alakazam', 'mewtwo', 'poliwrath'],
    'diglett': ['graveler'],
    'ditto': ['kabuto', 'vaporeon', 'aerodactyl'],
    'arbok': ['horsea', 'primeape', 'hitmonlee'],
    'abra': ['grimer', 'tangela', 'dragonite'],
    'jigglypuff': [],
    'tentacool': ['weezing', 'mewtwo', 'farfetchd', 'moltres', 'grimer'],
    'tentacruel': ['dodrio'],
    'tauros': ['flareon', 'moltres', 'porygon', 'omanyte'],
    'dodrio': [],
    'exeggcute': [],
    'victreebel': ['tentacruel', 'seaking', 'ditto', 'lapras'],
    'nidoranfemale': ['jynx', 'persian', 'shellder', 'mewtwo'],
    'shellder': ['vaporeon', 'marowak', 'articuno', 'tauros', 'gyarados'],
    'nidorino': ['omanyte', 'gastly', 'magneton', 'marowak', 'paras'],
    'aerodactyl': ['zapdos'],
    'kingler': ['mew', 'cubone', 'mr.mime', 'dratini', 'weezing'],
    'seadra': ['mr.mime', 'scyther', 'jynx', 'electabuzz', 'magmar'],
    'exeggutor': ['mr.mime', 'dragonite', 'hitmonchan', 'flareon', 'gyarados'],
    'koffing': ['weezing', 'chansey', 'omastar'],
    'farfetchd': ['rhyhorn', 'cloyster', 'moltres', 'vaporeon', 'dodrio'],
    'jolteon': ['kabutops', 'snorlax', 'omastar', 'aerodactyl'],
    'sandshrew': ['lickitung', 'nidoranmale', 'clefairy'],
    'magmar': ['snorlax', 'tauros', 'pinsir', 'lapras'],
    'electrode': ['lapras', 'staryu', 'seaking', 'marowak', 'horsea'],
    'dratini': [],
    'mankey': ['farfetchd', 'electrode'],
    'magneton': ['mr.mime', 'kabutops'],
    'staryu': ['ditto', 'dratini'],
    'seaking': ['staryu', 'magikarp', 'starmie', 'dragonite'],
    'caterpie': ['weedle', 'vulpix', 'shellder', 'moltres'],
    'blastoise': ['electrode', 'vileplume', 'gastly', 'goldeen', 'sandslash'],
    'pidgeotto': ['lickitung', 'spearow'],
    'pikachu': ['hitmonlee'],
    'weepinbell': [],
    'gastly': ['seadra', 'mew', 'rhydon', 'horsea', 'tangela'],
    'scyther': ['jynx', 'articuno', 'mew'],
    'porygon': ['aerodactyl', 'mewtwo', 'kabuto'],
    'poliwrath': ['machop', 'victreebel', 'seel', 'gengar', 'vaporeon'],
    'dragonite': ['mewtwo', 'mew'],
    'geodude': ['magneton', 'seel', 'cubone'],
    'hitmonchan': [],
    'lickitung': [],
    'eevee': ['articuno', 'jolteon', 'flareon'],
    'venomoth': [],
    'moltres': ['dragonair'],
    'metapod': [],
    'horsea': ['moltres'],
    'graveler': ['seaking', 'tangela', 'slowpoke'],
    'kangaskhan': ['dragonite', 'kabuto', 'zapdos', 'moltres'],
    'cloyster': ['mr.mime', 'marowak', 'kabutops', 'gengar', 'eevee'],
    'machop': ['staryu', 'machamp', 'slowpoke', 'dodrio'],
    'kakuna': ['scyther', 'zubat'],
    'voltorb': ['porygon', 'pinsir', 'dragonite', 'jolteon', 'moltres'],
    'ninetales': ['farfetchd', 'parasect', 'ponyta', 'mewtwo'],
    'machamp': ['onix', 'marowak'],
    'jynx': ['dratini', 'tauros', 'snorlax'],
    'seel': ['haunter', 'kangaskhan'],
    'dewgong': ['hitmonchan', 'pinsir', 'eevee'],
    'growlithe': ['kabutops', 'shellder', 'farfetchd', 'chansey'],
    'vaporeon': ['porygon', 'jolteon', 'aerodactyl'],
    'haunter': ['koffing', 'rhyhorn', 'aerodactyl'],
    'nidorina': [],
    'alakazam': ['krabby', 'machoke', 'tauros', 'horsea'],
    'venonat': ['magmar', 'drowzee'],
    'nidoranmale': [],
    'omastar': [],
    'golbat': ['scyther', 'parasect', 'oddish'],
    'parasect': ['persian', 'electabuzz'],
    'squirtle': [],
    'drowzee': [],
    'chansey': ['pinsir', 'vaporeon'],
    'slowbro': [],
    'rhyhorn': ['staryu'],
    'clefable': ['golbat', 'ditto'],
    'goldeen': ['magikarp'],
    'zubat': ['eevee', 'gyarados', 'dodrio', 'seadra'],
    'doduo': ['shellder'],
    'lapras': ['omanyte', 'omastar', 'mewtwo'],
    'persian': ['golduck'],
    'psyduck': ['abra'],
}


print(can(book1,'bulbasaur','venusaur'))
print(can(book1,'charmeleon','blastoise'))
print(can(book2,'eevee','articuno'))
print(can(book3,'cubone','charizard'))
print(can(book3,'magikarp','mewtwo'))

# uncomment these lines when you are ready to test
# print("Using book1, can bulbasaur evolve to venusaur?")
# print(can_evolve(book1, "bulbasaur", "venusaur"))
# print("Using book1, can charmeleon evolve to blastoise?")
# print(can_evolve(book1, "charmeleon", "blastoise"))
# print("Using book2, can eevee evolve to articuno?")
# print(can_evolve(book2, "eevee", "articuno"))
# print("Using book3, can cubone evolve to charizard?")
# print(can_evolve(book3, "cubone", "charizard"))
# print("Using book3, can magikarp evolve to mewtwo?")
# print(can_evolve(book3, "magikarp", "mewtwo"))