# This is a script that needs to be run after route add
# Adds route to routes.json used in page script

# Route is route.json which defines object
# {
#   name:
#   date:
#   idea:
#   purpose: [ trailrunning, easymtb, familytrip]
# }

import os, json


def readroute(dir):
    try:
        with open(dir+'/route.json') as f:
            data = json.load(f)
            return data or {}
    except:
        return None

def build():
    routes = []
    for dir in os.listdir('.'):
        route = readroute(dir)
        if route != None: routes.append(route)

    with open('routes.json', 'w') as f:
        json.dump(routes, f)

build()