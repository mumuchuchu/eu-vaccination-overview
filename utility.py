import math

def get_country_list(records_list, countries_list):  
    for record in records_list:
        country = record["ReportingCountry"]
        if country not in countries_list:
            countries_list.append(country)
    return countries_list

def generate_color_by_index(index):
    switcher = {
        0:'#d7ffec',
        1:'#caf4e1',
        2:'#c1ecd9',
        3:'#b5e2cf',
        4:'#a4d4c1',
        5:'#9ecfbc',
        6:'#98c9b6',
        7:'#89bca9',
        8:'#81b5a2',
        9:'#79ae9b',
        10:'#6ca28f',
        11:'#5c9482',
        12:'#508977',
        13:'#4c8674',
        14:'#488270',
        15:'#447e6c',
        16:'#3a7563',
        17:'#326e5c',
        18:'#236250',
        19:'#135442',
        20:'#004432',
    }
    return switcher.get(index, "#FFFFFF")

def get_eu_overview(records_list, countries_list, data_list):
    for country in countries_list:
        first_dose = 0
        second_dose = 0
        for record in records_list:
            if record["ReportingCountry"] == country:
                first_dose += record["FirstDose"]
                second_dose += record["SecondDose"]
                population = record["Population"]
        rate = round(int(second_dose) / int(population) * 100)
        rate_index = math.ceil(rate/5)
        color = generate_color_by_index(rate_index)
        data_list.append({"country": country, "data": {"second dose": second_dose, "population": population, "rate": rate, "color": color}})
    return data_list

def get_color_by_country(country, data_list):
    return next(filter(lambda item: item["country"] == country, data_list))['data']['color']

def get_summary_by_country(country, data_list):
    rate = next(filter(lambda item: item["country"] == country, data_list))['data']['rate']
    return f'{country}: {rate}%'

