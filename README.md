## Introduction

**Qlik Cloud File list tool**
 The intention of this is just document how partners and customers can list all data files are stored in a Qlik Cloud Tenant.

**How to use**
You will need Python (I´ve tested using 3.10.5) 
1. Check [this](https://qlik.dev/tutorials/generate-your-first-api-key) to learn and get a key to your tenant
2. Set one environment variable with name KEY and with the content from your step 1
3. Change line 4 of the python script setting your tenant address hostname (drop the https:// part)
4. Run the script :)

This will dump all data files in your tenant and give some basic information about them.

More details about the API [here](https://qlik.dev/apis/rest/data-sets#%23%2Fentries%2Fdata-sets%2F-data-set-id-get)

## Disclaimer
This is NOT for production purposes, only for learning how to connect to Qlik SaaS API´s using pure Python requests

This is not a supported tool by Qlik, Inc 

## Licenses

This script is published under MIT License Model which allows users to easily modify and share with your fellow Developers.  For anyone interested in license please take a look at MIT License [wiki](https://en.wikipedia.org/wiki/MIT_License)

## Code of Conduct.

Qlik Partner Engineering will adopt. [Contributor Covenant Code of Conduct](https://github.com/Qlik-PE/Qlik-Rapid-API-Gateway/blob/master/CODE_OF_CONDUCT.md).  Please act accordingly.