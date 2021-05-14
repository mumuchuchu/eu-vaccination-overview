import requests
from utility import get_country_list, get_eu_overview
from eu_map import get_map_template
from datetime import date

# fetch data (json) from website

url = 'https://opendata.ecdc.europa.eu/covid19/vaccine_tracker/json'

try:
    response = requests.get(url, allow_redirects=True)
    data = response.json()
except Exception as e:
    print("Could not fetch data, see error message: ", e)
else:
        
    # sorting data for Netherlands
    records = (data["records"])
    countries_list = []
    eu_data_list = []
    country = 'NL'

    get_country_list(records, countries_list)
    get_eu_overview(records, countries_list, eu_data_list)
    today = date.today().strftime("%b %d %Y")

    country_data = get_overview_by_contry(country, eu_data_list)
    country_vaccination_pct = round(int(country_data["data"]["total dose"])/int(country_data["data"]["population"])*100)
    country_not_vaccination_pct = 100 - country_vaccination_pct

        # Generate map in html
        map = get_map_template(today, eu_data_list)

        # Output html file
        with open('index.html','w') as f:
            html = map
            f.write(html)