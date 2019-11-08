import click
import urllib3
import json
import time

from .formatters import Formatter
from .validators import Validators

# https://raw.githubusercontent.com/openstreetmap/Nominatim/master/data/country_name.sql
# https://nominatim.openstreetmap.org/search?country=bulgaria&format=geojson&polygon_geojson=0


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

    countries = {}

    # Compare with countries list from nominatim
    with open("externals/nomatium/data/country_name.sql") as f:
        for line in f.readlines():
            if '"name"=>' not in line:
                continue

            # Get country code
            code = line.split('\t')[0]
            line = line.split('\t')[1]
            try:
                Validators.validate(code)
            except ValueError:
                continue

            # Create empty dictionary
            data = {}

            # Get english name
            if code in [x.lower() for x in list(names['en'].keys())]:
                data['name_en'] = names['en'][code.upper()]
            else:
                for name in line.split(', '):
                    if '"name"=>' in name:
                        data['name_en'] = name.split('=>')[1].replace('"', '')
                    elif '"name:en"=>' in name:
                        data['name_en'] = name.split('=>')[1].replace('"', '')
                print("Missing country in country-list/en: \'{}\'. Using: \'{}\'".format(code, data['name_en']))

            # Get bulgarian name
            if code in [x.lower() for x in list(names['bg'].keys())]:
                data['name_bg'] = names['bg'][code.upper()]
            else:
                for name in line.split(', '):
                    if '"name"=>' in name:
                        data['name_bg'] = name.split('=>')[1].replace('"', '')
                    elif '"name:bg"=>' in name:
                        data['name_bg'] = name.split('=>')[1].replace('"', '')
                print("Missing country in country-list/bg: \'{}\'. Using: \'{}\'".format(code, data['name_en']))

            # Get geojson
            http = urllib3.PoolManager(headers={
                'User-Agent': '	Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'
            })
            ret: urllib3.response.HTTPResponse = http.request(
                'GET',
                "https://nominatim.openstreetmap.org/search?country={}&format=geojson&polygon_geojson=1".format(
                    data['name_en'].replace(' ', '%20').replace('&', 'and').lower()
                )
            )

            print("{} : {} -> {}".format(code, data['name_en'], data['name_bg']))
            j = json.loads(ret.data.decode())

            if len(j['features']) == 0:
                print("Missing features!")
                continue

            if len(j['features']) > 1:
                for feature in j['features']:
                    name = feature['properties']['display_name'].lower()
                    if name != data['name_en'].lower():
                        j['features'].remove(feature)
                        continue

            data['geojson'] = j
            countries[code] = data
            time.sleep(1)

    with open(kwargs['output'], 'w') as f:
        json.dump(countries, f)



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
