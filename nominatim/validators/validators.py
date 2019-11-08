from .country_code import CountryCode
from .country_exclude import CountryExclude


class Validators(object):
    country_code = CountryCode.validate
    country_exclude = CountryExclude.validate

    @staticmethod
    def validate(data: str):
        """
        Run all validators

        :param data:
        :return:
        """
        Validators.country_code(data)
        Validators.country_exclude(data)


