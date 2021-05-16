import requests
from utility import get_eu_overview
from eu_map import get_map_template

URL = 'https://opendata.ecdc.europa.eu/covid19/vaccine_tracker/json'
OUTPUT_FILE_NAME = 'index.html'

def read_data_from_web(url):
    try:
        response = requests.get(url, allow_redirects=True)
        response.raise_for_status()
    except Exception as e:
        print("Could not fetch data, see error message: ", e)
    else:
        return response.json()

def process_data(data):
    overview_data = get_eu_overview(data)
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