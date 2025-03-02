import requests

Endpoint = "https://pro-api.solscan.io/v2.0/token/meta"
api_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVkQXQiOjE3Mzk5NjIzNTgzOTUsImVtYWlsIjoiYWhtLm1vbnRhc3NlckBob3RtYWlsLmNvbSIsImFjdGlvbiI6InRva2VuLWFwaSIsImFwaVZlcnNpb24iOiJ2MiIsImlhdCI6MTczOTk2MjM1OH0.lW7tBi2CLyNrWU88xco2g16a4MAwSzMwu1QgCJNrvko"
token_address = "AxriehR6Xw3adzHopnvMn7GcpRFcD41ddpiTWMg6pump"

params={ 
    'address': token_address
}

headers={
    'Accept': 'application/json',
    'token': api_token
}

def fetch_meta_data():
    try:
        response=requests.get(Endpoint,headers=headers,params=params)
        response.raise_for_status()
        data=response.json()
        return data
    except requests.exceptions.RequestsException as e:
        print(f"Error fetching transactions: {e}")
        return None

def Get_No_Holders():
    market_cap_data = fetch_meta_data()
    
    filtered_data = {
        'name': market_cap_data['data']['name'],
        'Symbol': market_cap_data['data']['symbol'],
        'Holder': market_cap_data['data']['holder'],
    }
    print(filtered_data)

Get_No_Holders()
