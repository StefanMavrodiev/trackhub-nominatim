from .country_code import CountryCode
from .country_exclude import CountryExclude


class Validators(object):
    country_code = CountryCode.validate
    country_exclude = CountryExclude.validate
