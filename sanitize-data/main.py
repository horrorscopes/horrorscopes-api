from google.cloud import datastore
import json
import random
import time

def get_nonce():
    pass
    t = time.time()
    t = int(t*1000)
    return str(t)

def sanitize_data(request=None, body=None):
    pass

    db = datastore.Client()
    query = db.query(kind='horrorscope')
