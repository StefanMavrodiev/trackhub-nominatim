import re


class CountryCode(object):

    @staticmethod
    def validate(data: str) -> None:
        """
        Validate country code based on ISO 3166-1 codes

        :param data: string to validate
        :return: None
        :raise: ValueError on failure
        """
        # Country code should be exactly two characters
        if len(data) != 2:
            raise ValueError("Country code should be two characters long")

        # Country code should be lower-case
        if re.match('^[a-z]{2}', data) is None:
            raise ValueError("Invalid country code: \"{}\"".format(data))
