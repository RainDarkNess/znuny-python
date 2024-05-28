import requests
class ZnunyConnectorException(Exception):
    pass


class ZnunyConnector:
    def __init__(self, login=None, password=None, host=None, protocol="http"):
        self.login = login
        self.password = password
        self.host = host
        self.protocol = protocol
        self.base_url = self.protocol + "://" + self.host + "/otrs/nph-genericinterface.pl/Webservice"

    def get_ticket(self, ticket_id, webServisePath=[]):
        link = self.base_url + "/".join(
            webServisePath) + "/" + ticket_id + "?Password=" + self.password + "&DynamicFields=0&UserLogin=" + self.login + "&AllArticles=0"
        res = requests.post(self.base_url)
