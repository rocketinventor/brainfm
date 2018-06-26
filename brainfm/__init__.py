import requests


__version__ = "0.3.0"

__all__ = [
    "BROWSER",
    "DEFAULT_USER_AGENT",
    "Connection",
    "build_stream_url",
]

# http://www.useragentstring.com/index.php?id=19841
BROWSER = (
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/40.0.2214.85 Safari/537.36 ")
DEFAULT_USER_AGENT = "github.com/numberoverzero/brainfm v" + __version__


def build_stream_url(token):
    return "https://stream.brain.fm/?tkn=" + token


def endpoint(path):
    if not path.startswith("/"):
        path = "/" + path
    return "https://www1.brain.fm" + path


class Connection:
    """Low-level operation mapping and parameter validation.

    If brain.fm starts filtering on user-agent,
    set :attr:`Connection.user_agent` to :data:`brainfm.BROWSER`.
    """

    def __init__(self, sid=None, user_agent=DEFAULT_USER_AGENT):
        self.session = requests.Session()
        self.user_agent = user_agent
        self.sid = sid

    @property
    def user_agent(self):
        return self.session.headers["User-Agent"]

    @user_agent.setter
    def user_agent(self, value):
        self.session.headers["User-Agent"] = value

    @property
    def sid(self):
        return self.session.cookies["connect.sid"]

    @sid.setter
    def sid(self, value):
        self.session.cookies["connect.sid"] = value

    @sid.deleter
    def sid(self):
        del self.session.cookies["connect.sid"]

    def login(self, email, password):
        del self.sid
        payload = {"email": email, "password": password, "type": "LOGIN"}
        r = self.session.post(endpoint("/login"), json=payload)
        r.raise_for_status()

    def get_stations(self):
        r = self.session.get(endpoint("/stations"))
        r.raise_for_status()
        return r.json()["stations"]

    def get_token(self, station_id):
        r = self.session.post(endpoint("/tokens"), json={"stationId": station_id})
        r.raise_for_status()
        songs = r.json()["songs"]
        return songs[0]["token"]
