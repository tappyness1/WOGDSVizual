import urllib
import json
import csv
import urllib.parse
import urllib.request
import time

egfile = open('agency1.csv')
egReader= csv.reader(egfile)
egData = list(egReader)

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
apikey = input("Please key in your api key: "
for row in egData[1:]:
    address = row[6] + " Singapore"
    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address}) + "&key=" + apikey
    print (url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    js = json.loads(data.decode("utf-8"))
    print (json.dumps(js, indent=4))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    location = js['results'][0]['formatted_address']
    print (location)
    print ('lat',lat,'lng',lng)
    del row[7]
    row.insert(7, lat)
    del row[8]
    row.insert(8, lng)
    time.sleep(1)
for item in egData:    
    print (item)


egfile.close()

with open('latlon.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(egData)