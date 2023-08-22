"""module for parsing web url"""
import re


class WebParser:
    """class for parsing web url"""
    def __init__(self, http: str):
        self._http = http

    @property
    def http(self) -> str:
        """return http address

        Returns:
            str: http address
        """
        return self._http

    @http.setter
    def http(self, http: str) -> None:
        """set http address

        Args:
            http (str): http address
        """
        self._http = http

    def get_alias(self) -> str:
        """get alias from http

        Returns:
            str: alias
        """
        try:
            temp_result = re.search(r'//.*?/', self._http).group()
            if re.match(r'//www.', temp_result):
                temp_result = re.sub(r'www.', '', temp_result)
            dot_position = re.search(r'[.]', temp_result)
            result = temp_result[2:dot_position.start()]
            return result
        except AttributeError:
            return ""

    def get_homepage(self) -> str:
        """return homepage from http

        Returns:
            str: homepage
        """
        try:
            result = re.match(r'http.?://.*?/', self._http).group()
            return result
        except AttributeError:
            return ""
