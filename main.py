import requests
from utility import get_country_list, get_eu_overview
from eu_map import get_map_template
from datetime import date

def read_data_from_web(url):
    try:
        response = requests.get(url, allow_redirects=True)
        response.raise_for_status()
    except Exception as e:
        print("Could not fetch data, see error message: ", e)
    else:
        return response.json()

def process_data(data):
    records = (data["records"])
    countries_list = []
    eu_data_list = []
    today = date.today().strftime("%b %d %Y")

    get_country_list(records, countries_list)
    overview_data = get_eu_overview(records, countries_list, eu_data_list)
     # Generate map in html
    output = get_map_template(today, overview_data)
    return output

def write_data_to_file(data):
    with open('index.html','w') as f:
        html = data
        f.write(html)

def main():
    # fetch data (json) from website
    url = 'https://opendata.ecdc.europa.eu/covid19/vaccine_tracker/json'
    data = read_data_from_web(url)
    map = process_data(data)
    write_data_to_file(map)

if __name__ == '__main__':
    main()