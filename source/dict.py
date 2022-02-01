### Dict
d = {'sber.me':['sber', 'сбер', 'сбербанк'], 'gazp.me': ['газ', 'газон'], 'tsla':['тесла', 'маск', 'илон'], '^gspc':['сиплый', 'sp500', 'сипуха'], 'lkoh.me':['лукойл', 'лук', 'лучок'],     'tatn.me':'татнефть',
    'fb': 'facebook' }
def find_key(input_dict, value):
    for key in input_dict.keys():    
        if value in input_dict[key]:
            return key
    for key in input_dict.keys():    
        if not value in input_dict[key]:
            return value 
