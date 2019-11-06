import json


class JsonFormatter(object):
    def __init__(self, format=None):
        # Initialize data
        self._data = dict()

        self._format = format

    def add(self, *args, **kwargs):
        print(args)
        print(kwargs)

    @property
    def data(self) -> str:
        """
        Return encoded JSON data

        :return: json string
        """
        return self._data
