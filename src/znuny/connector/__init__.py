import json
import xml.dom.minidom
import requests
import urllib.request
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
import pickle
import time

from bs4 import BeautifulSoup


class ZnunyConnectorException(Exception):
    pass


class ZnunyConnector:

    def __init__(self, protocol="http", host=None, login=None, password=None):
        self.login = login
        self.password = password
        self.host = host
        self.protocol = protocol
        self.base_url = self.protocol + "://" + self.host + "/otrs/nph-genericinterface.pl/Webservice"

    # Template of rest request
    def get_ticket_info_rest(self, ticket_id, webServicePath, __params=""):
        link = self.base_url + "/" + webServicePath + "/" + str(
            ticket_id) + "?UserLogin=" + self.login + "&Password=" + self.password + str(__params)
        with urllib.request.urlopen(link) as response:
            data = json.loads(response.read())

        if "Error" in data:
            return data["Error"]["ErrorMessage"]
        else:
            return data

    # Template of soap request
    def get_ticket_info_soap(self, ticket_id, webServicePath, method_name='', pretty_printing=False):
        endpoint = self.protocol + '://' + self.host + '/otrs/nph-genericinterface.pl/Webservice/' + webServicePath
        body = ('<?xml version="1.0" encoding="utf-8"?> '
                + '<soap:Envelope '
                + 'xmlns:soap="http://www.w3.org/2003/05/soap-envelope"  xmlns:m="' + self.protocol + '://' + self.host + '/otrs/nph-genericinterface.pl/Webservice/' + webServicePath + '" '
                + 'soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding"> '
                + '  <soap:Body> '
                + '    <m:' + method_name + '> '
                + '        <TicketID>' + str(ticket_id) + '</TicketID> '
                + '        <UserLogin>' + self.login + '</UserLogin> '
                + '        <Password>' + self.password + '</Password> '
                + '    </m:' + method_name + '> '
                + '  </soap:Body> '
                + '</soap:Envelope> ')
        body.encode('utf-8')
        session = requests.session()
        session.headers = {"Content-Type": "text/xml; charset=utf-8"}
        session.headers.update({"Content-Length": str(len(body))})
        response = session.post(url=endpoint, data=body, verify=False)
        if pretty_printing:
            OriginalXml = response.content
            temp = xml.dom.minidom.parseString(OriginalXml)
            new_xml = temp.toprettyxml()
            return new_xml
        else:
            return response.content

    def sql_execute(self, sql, limit):

        session = requests.Session()

        start_session = self.protocol + '://' + self.host + "/otrs/index.pl"

        login_data = {
            "Action": "Login",
            "Lang": "en",
            "TimeZoneOffset": "-180",
            "User": self.login,
            "Password": self.password
        }

        response = session.post(start_session, data=login_data)

        soup = BeautifulSoup(response.content, 'html.parser')

        ChallengeToken = soup.find("input", {"name": "ChallengeToken"}).get("value")

        query = self.protocol + '://' + self.host + '/otrs/index.pl?ChallengeToken=' + ChallengeToken + '&Action=AdminSelectBox&Subaction=Select&SQL=' + sql + '&Max=' + str(
            limit) + '&ResultFormat=HTMl'

        response = session.get(query)

        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find("table", {"id": "Results"})
        #
        headers = [header.text for header in table.find_all('th')]
        #
        data = []
        rows = table.find_all('tr')[1:]
        for row in rows:
            cells = row.find_all('td')
            data.append({headers[i]: cell.text for i, cell in enumerate(cells)})

        return data
