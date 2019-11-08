class CountryExclude(object):

    @staticmethod
    def validate(data: str) -> None:
        """
        Check is country should be excluded

        :param data: string to validate
        :return: None
        :raise: ValueError on failure
        """
        # Exclude these countries/islands
        if data in [
            'an',
            'nf',  # North Folks
            'tf',  # French Southern Territories
            'aq',  # Antarctica
            'aw',  # Aruba
            'eh',  # Western Sahara
            'gu',  # Guam
            'hk',  # Hong Kong SAR China
            'mo',  # Macao SAR China
            'pr',  # Puerto Rico
            'ps',  # Palestinian Territory
            'pf',  # French Polynesia
            'mf',  # St. Martin
            'bl',  # St. Barthélemy
            'ax',  # Åland Islands
            'bv',  # Bouvet Island
            'cx',  # Christmas Island
            'hm',  # Heard Island and MaxDonald
            'mp',  # Northern Mariana Islands
            'sj',  # Svalbard & Jan Mayen
            'um',  # U.S. Outlying Islands
            'vi',  # U.S. Virgin Islands
            'yt',  # Mayotte
            'ph',  # Philippines
            'va',  # Vatican City
            'cc',  # Cocos (Keeling) Islands
            'dm',  # Dominica
            'mq',  # Martinique
            'gf',  # French Guiana
            'gp',  # Guadeloupe
            'nc',  # New Caledonia
            're',  # Réunion
            'pm',  # St. Pierre & Miquelon
            'wf',  # Wallis & Futuna
            'cw',  # Curaçao
            'sx',  # Sint Maarten
            'fk',  # Falkland Island
            'mm',  # Myanmar
        ]:
            raise ValueError("Country {} is in the exclude list!")
