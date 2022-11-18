# Important note, when creating a virtual environment for macOS,
# use the --copies option.
# python3 -m venv --copies venv

import requests
from requests.auth import HTTPBasicAuth

# Constant block.
###########################################################################
BASE_URL="https://sandboxdnac.cisco.com"
SYSTEM_BASE_URL= BASE_URL+"/dna/system/api/v1"
INTENT_BASE_URL= BASE_URL+"/dna/intent/api/v1"
USERNAME= "devnetuser"
PASSWORD= "Cisco123!"

# URLs or Endpoints.
AUTH_API_URL="/auth/token"
GET_DEVICES_URL="/network-device"

# Request headers.
headers={'content-type': 'application/json'}

# Utility functions.
###########################################################################

# Authenticate to DNA Center from Basic Authentication (user, pass) in order
# to obtain JWT access token.
# Source -> https://developer.cisco.com/docs/dna-center/#!api-quick-start/authentication
# --------------------------------------------------------------------------
def get_token():
    try:
        token = requests.post(
            SYSTEM_BASE_URL + AUTH_API_URL,
            auth=HTTPBasicAuth(username=USERNAME, password=PASSWORD),
            headers=headers,
            verify=False
        )
        token.raise_for_status() # <-- Let HTTP errors raise exceptions.
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    except requests.exceptions.Timeout:
        print("[Error]: Timeout ocurred!")
        # Maybe set up for a retry, or continue in a retry loop
    except requests.exceptions.TooManyRedirects:
        print("[Error]: Too many redirects!")
        # Tell the user their URL was bad and try a different one
    except requests.exceptions.RequestException:
        print("[Error]: The request is poorly structured!")
        # catastrophic error.
    
    # Parse response to json.
    data = token.json()
    return data['Token']
# --------------------------------------------------------------------------

# Return information of the devices that are part of the network.
# Source -> https://developer.cisco.com/docs/dna-center/#!devices/devices-guide
# --------------------------------------------------------------------------
def get_devices(token: str):
    try:
        response = requests.get(
            INTENT_BASE_URL + GET_DEVICES_URL,
            headers={**headers, **{'X-Auth-Token': token}},
            verify=False
        )
        response.raise_for_status() # <-- Let HTTP errors raise exceptions.
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    
    return response.json()['response']
# --------------------------------------------------------------------------

# Entry Point.
###########################################################################
def main():
    token = get_token()
    devices = get_devices(token)
    
    for index,device in enumerate(devices):
        print(f"#{index}[{device['hostname']}]: ID: {device['id']}, Management IP: {device['managementIpAddress']}")

# It's boilerplate code that protects users from accidentally invoking the script 
# when they didn't intend to.
###########################################################################
if __name__ == "__main__":
    main()