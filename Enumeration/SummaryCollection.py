from API import *
import sys

FACETS = [
    "org",
    "domain",
    "port",
    "asn",
    ("country", 3),
]

FACET_TITLES = {
    "org": "Top 5 Organizations",
    "domain": "Top 5 Domains",
    "port": "Top 5 Ports",
    "asn": "Top 5 Autonomous System",
    "country": "Top 3 Countries",
}

if len(sys.argv) == 1:
    print("Usage : %s <search query>" % sys.argv[0])
    sys.exit(1)

try:
    query = " ".join(sys.argv[1])
    result = api.search(query, facets=FACETS)

    print("Shodan summary Information")
    print("Query : %s" % query)
    print("Total Results : %s\n" % result["total"])

    for facet in result["facets"]:
        print(FACET_TITLES[facet])
        for term in result["facets"][facet]:
            print("%s : %s" % (term["value"], term["count"]))
        print("")
except Exception as e:
    print("Error :%s ".format(e))
    sys.exit(1)
