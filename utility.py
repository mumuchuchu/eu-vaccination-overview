def get_country_list(records_list, countries_list):  
    for record in records_list:
        country = record["ReportingCountry"]
        if country not in countries_list:
            countries_list.append(country)
    return countries_list


def get_eu_overview(records_list, countries_list, list_data):
    for country in countries_list:
        first_dose = 0
        second_dose = 0
        for record in records_list:
            if record["ReportingCountry"] == country:
                first_dose += record["FirstDose"]
                second_dose += record["SecondDose"]
                population = record["Population"]
        list_data.append({"country": country, "data": {"first dose": first_dose, "second dose": second_dose, "total dose": first_dose+second_dose, "population": population}})
    return list_data


def get_overview_by_contry(country, list_data):
    return next(filter(lambda item: item["country"] == country, list_data))


