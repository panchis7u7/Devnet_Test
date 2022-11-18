# Meraki Sandbox: https://api.meraki.com/api/v1

import meraki

# Constant block.
###########################################################################
BASE_URL = "https://n1.meraki.com/"

MERAKI_DASHBOARD_API_KEY="35d59e9eb68a273997cdbc0c60c0150ce0eee1f2"

# Entry Point.
###########################################################################
def main():
    dashboard = meraki.DashboardAPI(
        base_url=BASE_URL,
        api_key=MERAKI_DASHBOARD_API_KEY,
        output_log=False
    )
    
    orgs = dashboard.organizations.getOrganizations()
# --------------------------------------------------------------------------

# It's boilerplate code that protects users from accidentally invoking the script 
# when they didn't intend to.
###########################################################################
if __name__ == "__main__":
    main()