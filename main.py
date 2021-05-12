import requests
from datetime import date
from utility import get_country_list, get_eu_overview, get_overview_by_contry

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

    # Output html file

    with open('index.html','w') as f:

        html = '''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="style.css">
                <title>%s Vaccination Rate</title>
            </head>
            <body>
                <h1 style="text-align: center">Date: %s</h1>
                <div class="chart_wrapper">
                    <div class="chart">
                        <h2>%s Vaccination Rate</h2>
                        <h3>Amount: %s</h3>
                        <h3>Percentage: %d%%</h3>
                        <div class="chart__container">
                            <div class="chart__inner-container">
                                <svg viewBox="0 0 64 64" class="pie" style="background: #c4c4c4">
                                    <circle
                                    class="absent-docs"
                                    r="25%%"
                                    cx="50%%"
                                    cy="50%%"
                                    style="stroke-dasharray: %d 100"
                                    ></circle>
                                    <circle
                                    class="available-docs"
                                    r="25%%"
                                    cx="50%%"
                                    cy="50%%"
                                    style="stroke-dasharray: %d 100; stroke-dashoffset: -%d"
                                    ></circle>
                                </svg>
                            </div>
                        </div>
                    </div>
                </div>
            </body>
            </html>'''

        content = html % (country, today, country, country_data["data"]["total dose"], country_vaccination_pct, country_vaccination_pct, country_not_vaccination_pct, country_vaccination_pct) 
        f.write(content)