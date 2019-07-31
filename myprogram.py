import configparser

Config = configparser.ConfigParser()

file = input("\nEnter the file location: ")
Config.read(file)

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

site = input("\nEnter the site you want info from: ")
Name = ConfigSectionMap(site)['name']
Url = ConfigSectionMap(site)['url']
Api = ConfigSectionMap(site)['api']
