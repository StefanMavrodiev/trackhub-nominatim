import json
import re

import click
import urllib3

from .formatters import Formatter
from .validators import Validators

# https://raw.githubusercontent.com/openstreetmap/Nominatim/master/data/country_name.sql

http = urllib3.PoolManager()


@click.command()
@click.argument("output")
def cli(**kwargs):
    ret: urllib3.response.HTTPResponse = http.request(
        'GET',
        "https://raw.githubusercontent.com/openstreetmap/Nominatim/master/data/country_name.sql"
    )

    data: str = ret.data.decode()
    # print(data)

    # Parse data
    formatter = Formatter.json(format={
        'id': str,
        'geojson': str,
        'name_en': str,
        'name_bg': str,
    })

    for line in data.split('\n'):
        if '\"name\"=>' not in line:
            continue

        country = {}

        # Get country code
        code = line.split()[0]
        line = line[len(code):]
        print(line)
        print(line.split(','))
        Validators.country_code(code)



        return



if __name__ == '__main__':
    cli()
