import requests
import logging
import json

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
log.addHandler(handler)

def fetch():
    i = 693
    while True:
        serverurl = "http://bencarle.com/chess/cg/" + str(i) + "/"
        r = requests.get(serverurl)
        if r.status_code == 404:
            break
        f = open("D:/CarleChess/" + str(i) + ".json", 'w')
        json.dump(r.json(), f)
        f.close()
        log.info("Game id " + str(i) + " was saved.")
        i += 1
        
fetch()