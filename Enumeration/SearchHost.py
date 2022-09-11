from API import *

try:
    results = api.search('apache')
    print('Result found : {}'.format(results['total']))
    for result in results['matches']:
        print("IP : {}".format(result['ip_str']))
        # print(result['data'])
        print('')
except shodan.APIError as e:
    print("Error : {}".format(e))