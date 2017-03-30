# -*- coding: utf-8 -*-
import http.client
from urllib.parse import urlencode
import json
from dao import *
from urllib import request

# reverse geocoding
API_KEY = "iOU3YvIBmvewqGiyyF9EEdx7CFfoJkKT"

try:
    db = DAO()
    db.execute("Select numero, adresse, ville from installation where latitude=47")

    for row in db:

        numero = str(row[0])
        adresse = row[1] + " " + row[2]

        print(adresse)

        location = input('Entrez une adresse : ')

        urlParams = {'location': location, 'key': API_KEY, 'inFormat':'kvp', 'outFormat':'json'}
        url = "/geocoding/v1/address?" + urlencode(urlParams)

        proxy_host = 'proxyetu.iut-nantes.univ-nantes.prive:3128'
        req = request.Request(url)
        req.set_proxy(proxy_host, 'http')


        #conn = http.client.HTTPConnection("www.mapquestapi.com")
        #conn.request("GET", url)

        res = conn.getresponse()
        print(res.status, res.reason)


        data = res.read()
        response = request.urlopen(req)
        data = response.read().decode('utf8')
        jsonData = json.loads(data)

        # FIXME le print n'est pas très secure...
        print(jsonData['results'][0]['locations'][0]['latLng'])
        longitude = str(jsonData['results'][0]['locations'][0]['latLng']['lng'])
        latitude = str(jsonData['results'][0]['locations'][0]['latLng']['lat'])

        db.execute("Update installation SET longitude = "+ longitude +"where numero ="+numero)
        db.execute("Update installation SET latitude = "+ longitude +"where numero ="+numero)


except Exception as err:
    print("Unexpected error: {0}".format(err))
finally:
    conn.close()
