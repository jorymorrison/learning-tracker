import configparser
import argparse

#parser = argparse.ArgumentParser(description='Request from a site.')
#parser.add_argument('site', metavar='N', type=str, nargs='+', help='the site you wish to request from')
#args = parser.parse_args()

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
Client = ConfigSectionMap("udemy")['client id']
Secret = ConfigSectionMap("udemy")['secret id']
Org = ConfigSectionMap("udemy")['org id']

print("Name of site: " + Name)
print("Site URL: " + Url)
print("Client id: " + Client)
print("API key: " + Secret)
print("Org id: " + Org)
