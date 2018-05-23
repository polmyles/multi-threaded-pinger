import requests
import time
from datetime import datetime
from subprocess import call
from multiprocessing.dummy import Pool as ThreadPool

MIME_TYPE_JSON = 'application/json'
CONTENT_TYPE = 'Content-type'

def api_handler(i):

    response = None

    try:
        begin = datetime.now()
        #call(["host", "google.com", ">", "response"])
        headers = {CONTENT_TYPE: MIME_TYPE_JSON}
        #response = requests.get("https://www.google.com/logos/doodles/2016/2016-doodle-fruit-games-day-8-5666133911797760.3-hp.gif", headers=headers)
        response = requests.get("http://ruby-hello-world-polmyles-dev.webplatformsnonprod.umich.edu", headers=headers)

        end = datetime.now()
        diff = end - begin
        print str(i) + " execution time: " + str(diff.total_seconds())

        if diff.total_seconds() > 3:
           print "clock time: " + str(end)
        print call(["host", "-v", "http://ruby-hello-world-polmyles-dev.webplatformsnonprod.umich.edu"])
#   except (requests.exceptions.RequestException, Exception) as exception:
    except (Exception) as exception:
        raise exception

    return response


print 'started at: ' + str(datetime.now())

def smash(i):
    while True:
        api_handler(i)

pool = ThreadPool(12)
results = []
results = pool.map(smash, range(1, 100000))

print 'ended at: ' + str(datetime.now())
