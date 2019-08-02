import configparser
import argparse

#parser = argparse.ArgumentParser(description='Request from a site.')
#parser.add_argument('site', metavar='N', type=str, nargs='+', help='the site you wish to request from')
#args = parser.parse_args()

def get_api_token(file):
    with open(file, encoding='utf-8-sig') as json_file:
        r = json.loads(json_file.read())
        return r['results']

def get_base64_encoded_header(client_id, client_secret):
    auth_token = 'Basic' + base64.b64encode("{}:{}".format(client_id, client_secret).encode()).decode('ascii')
    headers = {'Authorization':auth_token}
    return headers

def get_api_response(portal_name, portal_id, client_id, client_secret):
    url = 'https://' + portal_name + '.udemy.com/api-2.0/organizations/' + str(portal_id) + '/courses/list'
    r = requests.request("GET", url, headers=get_base64_encoded_header(client_id, client_secret))
    return r
    
Config = configparser.ConfigParser()
    
#file = input("\nEnter the file location: ")
Config.read(".learning-config")

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

#site = args.site
#print(site)
Name = ConfigSectionMap("udemy")['name']
Url = ConfigSectionMap("udemy")['url']
client_id = ConfigSectionMap("udemy")['client id']
client_secret = ConfigSectionMap("udemy")['secret id']
Org = ConfigSectionMap("udemy")['org id']

print("Name of site: " + Name)
print("Site URL: " + Url)
print("Client id: " + client_id)
print("API key: " + client_secret)
print("Org id: " + Org)
