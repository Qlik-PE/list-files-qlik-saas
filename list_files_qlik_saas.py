import requests as req
import os

TENANT = 'anjos.us.qlikcloud.com'
TOKEN = os.getenv('KEY')
if TOKEN is None or len(TOKEN) == 0:
    print(
        f"Ops, you are missing a key to access {TENANT}, please take a look at https://qlik.dev/tutorials/generate-your-first-api-key")
    exit

print(f"Let´s see which data files I have access on {TENANT}")

authheader = { 'Authorization': f"Bearer {TOKEN}" }
url_items = f'https://{TENANT}/api/v1/items?resourceType=dataset&limit=100'
while len(url_items):
    response = req.get(url_items, headers=authheader)
    if response.status_code != 200:
        print(f"Ops, I don´t have access. Maybe your key expired?")
        exit
    j_file = response.json()
    for data_file in j_file['data']:
        print(f"id:{data_file['id']},name:{data_file['name']}")
        response = req.get(
            f"https://{TENANT}/api/v1/data-sets/{data_file['resourceId']}", headers=authheader)
        if response.status_code != 200:
            print(f"Ops, something is not right, skipping this file")
        else:
            j_fields = response.json()
            if 'schema' in j_fields:
                for f in j_fields['schema']['dataFields']:
                    print(f"\t{f['name']} : {f['dataType']['type']}")
            else:
                print(f"Was not able to find a schema, skipping this file")                        
    url_items = j_file['links']['next']['href'] if 'next' in j_file['links'] else ''
