import requests
import urllib3

# SSL 경고 메시지 비활성화
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class HttpClient:
    def __init__(self):
        self.session = requests.Session()

    def __del__(self):
        self.session.close()

    def post(self, url: str, headers: dict = None, data: dict = None) -> requests.Response:
        session_headers = self.session.headers.copy()
        if headers:
            session_headers.update(headers)
        res = self.session.post(url, headers=session_headers, data=data, timeout=30, allow_redirects=True, verify=False)
        res.raise_for_status()
        return res

    def get(self, url: str, headers: dict = None, params: dict = None) -> requests.Response:
        session_headers = self.session.headers.copy()
        if headers:
            session_headers.update(headers)
        res = self.session.get(url, headers=session_headers, params=params, timeout=30, verify=False)
        res.raise_for_status()
        return res

class HttpClientSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if HttpClientSingleton._instance is None:
            HttpClientSingleton._instance = HttpClient()
        return HttpClientSingleton._instance