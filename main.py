import requests
from utilities import get_eu_overview
from eu_map import get_map_template

URL = 'https://opendata.ecdc.europa.eu/covid19/vaccine_tracker/json'
OUTPUT_FILE_NAME = 'index.html'
COUNTRIES = ["AT", "BE", "BG", "CY", "CZ", "DE", "DK", "EE", "ES", "FI", "FR", "HR", "HU", "IE", "IS", "IT", "LI", "LT", "LU", "LV", "NL", "NO", "PL", "PT", "RO", "SK", "SI", "SE"]
COLORS = ['#d7ffec', '#caf4e1', '#c1ecd9', '#b5e2cf', '#a4d4c1', '#9ecfbc', '#98c9b6', '#89bca9', '#81b5a2', '#79ae9b', '#6ca28f', '#5c9482', '#508977', '#4c8674', '#488270', '#447e6c', '#3a7563', '#326e5c', '#236250', '#135442', '#004432']
NO_DATA_COLOR = "#E5E7EB"

def read_data_from_web(url):
    try:
        response = requests.get(url, allow_redirects=True)
        response.raise_for_status()
    except Exception as e:
        print("Could not fetch data, see error message: ", e)
    else:
        return response.json()

def process_data(data):
    overview_data = get_eu_overview(data, COUNTRIES, COLORS, NO_DATA_COLOR)
    # Generate map in html
    output = get_map_template(overview_data)
    return output

def write_data_to_file(data):
    with open(OUTPUT_FILE_NAME,'w') as f:
        f.write(data)

def main():
    data = read_data_from_web(URL)["records"]
    modified_data = process_data(data)
    write_data_to_file(modified_data)

if __name__ == '__main__':
    main()