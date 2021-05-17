import math
from itertools import groupby
from datetime import date

def generate_color_for_country(rate, colors):
    color_index = min(math.ceil(rate/(100/(len(colors)-1))), math.ceil(100/(100/(len(colors)-1))))
    return colors[color_index]

def generate_overview(country, countries, rate, color, overview):
    if country in countries:
        overview[f'{country.lower()}_color'] = color
        overview[f'{country.lower()}_summary'] = f'{country}: {rate}%'
    return overview

def get_eu_overview(records, countries, colors, default_color):
    overview = {}
    today = date.today().strftime("%b %d %Y")
    overview['date'] = today
    overview['no_data_color'] = default_color
    for country, record in groupby(records, lambda record: record['ReportingCountry']):
        second_dose = 0
        for record in list(record):
            if record["TargetGroup"] == "ALL":
                second_dose += record["SecondDose"]
                population = record["Population"]
        rate = round(second_dose/ int(population) * 100)
        color = generate_color_for_country(rate, colors)
        generate_overview(country, countries, rate, color, overview)
    return overview

