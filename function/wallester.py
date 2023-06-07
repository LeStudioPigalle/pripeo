import jwt
import requests
from datetime import datetime


def getToken():
    private_key = b"-----BEGIN RSA PRIVATE KEY-----\n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\n-----END RSA PRIVATE KEY-----"

    now = datetime.now()
    ts = now.timestamp()

    payload = {"api_key": "INCEPVZ0mivg1thjS6cuyazKe14i472XWPAtXljEzXaMnfLlC7qJoYMrTofKDjDarBmcZnx8NRLGPxiYXcR2OvrxZuFhFhleEe2t", "ts": int(ts)}

    token = jwt.encode(payload=payload, key=private_key, algorithm="RS256")

    return token


def getAccountByName(name):
    token = getToken()

    url = "https://api-frontend.wallester.com/v1/accounts"

    querystring = {"from_record": "1", "records_count": "1000", "name": name}

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()


def getAccountById(account_id):
    token = getToken()

    url = f"https://api-frontend.wallester.com/v1/accounts/{account_id}"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.request("GET", url, headers=headers)

    return response.json()

def getCardsByIdAccount(account_id):
    token = getToken()

    url = f"https://api-frontend.wallester.com/v1/accounts/{account_id}/cards"

    querystring = {"from_record": "1", "records_count": "1000"}

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()

def getCardHistory(card_id):
    token = getToken()

    url = f"https://api-frontend.wallester.com/v1/cards/{card_id}/history"

    querystring = {"from_record": "1", "records_count": "1000"}

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()

def blockCard(card_id):
    token = getToken()

    url = f"https://api-frontend.wallester.com/v1/cards/{card_id}/block"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.request("GET", url, headers=headers)

    return response.json()

def unblockCard(card_id):
    token = getToken()

    url = f"https://api-frontend.wallester.com/v1/cards/{card_id}/unblock"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.request("GET", url, headers=headers)

    return response.json()


def downloadStatementById(account_id, from_date, to_date, statement_file_type):
    token = getToken()

    url = f"https://api-frontend.wallester.com/v1/accounts/{account_id}/download-statement"

    querystring = {"from_date": from_date, "to_date": to_date, 'statement_file_type': statement_file_type}

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()


print(getCardsByIdAccount("697dcdbe-950a-45d6-acec-e624adf0b7f1"))