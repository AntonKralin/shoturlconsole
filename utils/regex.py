import re


class WebParser:
    def __init__(self, http: str):
        self._http = http

    @property
    def http(self):
        return self.http

    @http.setter
    def http(self, http):
        self._http = http

    def get_alias(self) -> str:
        try:
            buf_rez = re.search(r'//.*?/', self._http).group()
            if re.match(r'//www.', buf_rez):
                buf_rez = re.sub(r'www.', '', buf_rez)
            dot_pos = re.search(r'[.]', buf_rez)
            result = buf_rez[2:dot_pos.start()]
            return result
        except Exception:
            return ""

    def get_homepage(self) -> str:
        try:
            result = re.match(r'http.?://.*?/', self._http).group()
            return result
        except Exception:
            return ""
