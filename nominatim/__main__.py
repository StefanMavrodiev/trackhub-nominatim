import click
import urllib3
import json

from .formatters import Formatter
from .validators import Validators

# https://raw.githubusercontent.com/openstreetmap/Nominatim/master/data/country_name.sql
# https://nominatim.openstreetmap.org/search?country=bulgaria&format=geojson&polygon_geojson=1

http = urllib3.PoolManager()


@click.command()
@click.argument("output")
def cli(**kwargs):

    countries = {}
    names = {}

    # Load country list
    with open("externals/country-list/data/en/country.json", 'r') as f:
        names['en'] = json.load(f)

    with open("externals/country-list/data/bg/country.json", 'r') as f:
        names['bg'] = json.load(f)

    # Compare with countries list from nominatim
    with open("externals/nomatium/data/country_name.sql") as f:
        for line in f.readlines():
            if '"name"=>' not in line:
                continue

            # Get country code
            code = line.split()[0]
            line = line[len(code):]
            try:
                Validators.country_code(code)
            except ValueError:
                continue

            data = {}

            if code in [x.lower() for x in list(names['en'].keys())]:
                data['name_en'] = names['en'][code.upper()]
            else:
                for name in line.split(', '):
                    if '"name"=>' in name:
                        data['name_en'] = name.split('=>')[1].replace('"', '')
                    elif '"name:en"=>' in name:
                        data['name_en'] = name.split('=>')[1].replace('"', '')

            if code in [x.lower() for x in list(names['bg'].keys())]:
                data['name_bg'] = names['bg'][code.upper()]
            else:
                for name in line.split(', '):
                    if '"name"=>' in name:
                        data['name_bg'] = name.split('=>')[1].replace('"', '')
                    elif '"name:bg"=>' in name:
                        data['name_bg'] = name.split('=>')[1].replace('"', '')

            countries[code] = data

    print(countries)





    # ret: urllib3.response.HTTPResponse = http.request(
    #     'GET',
    #     "https://raw.githubusercontent.com/openstreetmap/Nominatim/master/data/country_name.sql"
    # )
    #
    # data: str = ret.data.decode()
    # # print(data)
    #
    # # Parse data
    # formatter = Formatter.json(format={
    #     'id': str,
    #     'geojson': str,
    #     'name_en': str,
    #     'name_bg': str,
    # })
    #
    # for line in data.split('\n'):
    #     if '\"name\"=>' not in line:
    #         continue
    #
    #     country = {}
    #
    #     # Get country code
    #     code = line.split()[0]
    #     line = line[len(code):]
    #     print(line)
    #     for l in line.split(', '):
    #         print(l)
    #     Validators.country_code(code)
    #
    #
    #
    #     return



if __name__ == '__main__':
    cli()
