from API import *

host = api.host('115.99.14.163')
print("""
    IP : {}
    Organization : {}
    Operating System : {}
""".format(host['ip_str'], host.get('org', 'n/a'), host.get('os','n/a')))
for item in host['data']:
    print("""
        Port : {}
        Banner : {}
    """.format(item['port'], item['data']))