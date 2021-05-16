import math
from itertools import groupby
from datetime import date

COUNTRIES = ["AT", "BE", "BG", "CY", "CZ", "DE", "DK", "EE", "ES", "FI", "FR", "HR", "HU", "IE", "IS", "IT", "LI", "LT", "LU", "LV", "NL", "NO", "PL", "PT", "RO", "SK", "SI", "SE"]
COLORS = ['#d7ffec', '#caf4e1', '#c1ecd9', '#b5e2cf', '#a4d4c1', '#9ecfbc', '#98c9b6', '#89bca9', '#81b5a2', '#79ae9b', '#6ca28f', '#5c9482', '#508977', '#4c8674', '#488270', '#447e6c', '#3a7563', '#326e5c', '#236250', '#135442', '#004432']
NO_DATA_COLOR = "#E5E7EB"

def generate_color_for_country(rate):
    color_index = min(math.ceil(rate/(100/(len(COLORS)-1))), math.ceil(100/(100/(len(COLORS)-1))))
    return COLORS[color_index]

def generate_overview(country, rate, color, overview):
    if country in COUNTRIES:
        overview[f'{country.lower()}_color'] = color
        overview[f'{country.lower()}_summary'] = f'{country}: {rate}%'
    return overview

def get_eu_overview(records):
    overview = {}
    today = date.today().strftime("%b %d %Y")
    overview['date'] = today
    overview['no_data_color'] = NO_DATA_COLOR
    for country, record in groupby(records, lambda record: record['ReportingCountry']):
        second_dose = 0
        for record in list(record):
            second_dose += record["SecondDose"]
            population = record["Population"]
        rate = round(second_dose/ int(population) * 100)
        color = generate_color_for_country(rate)
        generate_overview(country, rate, color, overview)
    return overview

