# To use the SDK: pip install dnacentersdk

from dnacentersdk import api

# Constant block.
###########################################################################
BASE_URL="https://sandboxdnac.cisco.com"
USERNAME= "devnetuser"
PASSWORD= "Cisco123!"

###########################################################################

# Entry Point.
# Source -> https://pypi.org/project/dnacentersdk/
# --------------------------------------------------------------------------
def main():
    # Create a DNACenterAPI connection object;
    dnac = api.DNACenterAPI(
        username=USERNAME,
        password=PASSWORD,
        base_url=BASE_URL,
        version='2.3.3.0',
        verify=False
    )

    devices = dnac.devices.get_device_list()
    for index,device in enumerate(devices.response):
        print(f"#{index}[{device['hostname']}]: ID: {device['id']}, Management IP: {device['managementIpAddress']}")
# --------------------------------------------------------------------------

# It's boilerplate code that protects users from accidentally invoking the script 
# when they didn't intend to.
###########################################################################
if __name__ == '__main__':
    main()