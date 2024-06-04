# from znuny.connector import ZnunyConnector
from src.znuny.connector import ZnunyConnector

if __name__ == '__main__':
    connector = ZnunyConnector('http', '10.0.241.114', 'root@localhost', 'GkuGs9I3QKqHkDNB')

    # data = connector.get_ticket_info_rest(1, "GetHistory/GetHistory")
    # data = connector.get_ticket_info_soap(1, "soap_test", 'GetTicket', True)
    data = connector.sql_execute("SELECT * FROM ticket_flag", 20)
    print(data)
