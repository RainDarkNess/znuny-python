# Znuny-python

Znuny-python is a simple tool for working with znuny in python.

## Installation
To install that library, you can use it:
```bash
pip install git+https://github.com/RainDarkNess/znuny-python.git 
```
## Usage
```python
from src.znuny.connector import ZnunyConnector

# Login
connector = ZnunyConnector("http", "***", "***", "***")

# Get ticket or ticket-info by ticket id by rest (depending on your webservice)
data = connector.get_ticket_info_rest(1, "GetHistory/GetHistory") 

# Get ticket or ticket-info by ticket id by soap (depending on your webservice)
data = connector.get_tickets_soap(1, "soap_test", 'GetTicket', True)

# Execute sql query in znuny
data = connector.sql_execute("SELECT * FROM ticket_flag", 20)
```

## Exceptions
Library return Exception by znuny

## License
[MIT](https://choosealicense.com/licenses/mit/)