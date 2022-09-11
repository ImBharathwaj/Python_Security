from turtle import goto
from API import *
import sys

if len(sys.argv) == 1:
    print("Usage: %s <search query>" % sys.argv[0])
    sys.exit(1)

try:
    query = " ".join(sys.argv[1])
    result = api.search(query=query)
    
    for service in result["matches"]:
        # if service['ip_str'] == '115.99.14.163':
        #     print('found')
        print(service['ip_str'])
except Exception as e:
    print("Error : %s " % e)
    sys.exit(1)