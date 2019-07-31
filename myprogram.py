import argparse
parser = argparse.ArgumentParser(description='Request from a url.')
parser.add_argument('url', metavar='N', type=String, nargs='+', help='the url you wish to request from')
args = parser.parse_args()
print args.url
