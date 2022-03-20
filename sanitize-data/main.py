from google.cloud import datastore
import json
import random
import time

bad_words = [
    'hitler',
]

def get_nonce():
    pass
    t = time.time()
    t = int(t*1000)
    return str(t)

def sanitize_data(request=None, body=None):
    pass
    to_be_deleted = []
    db = datastore.Client()
    query = db.query(kind='horrorscope')
    query.add_filter('sanitized', '=', False)
    results = query.fetch()
    for r in results:
        pass
        if r['fate'] in bad_words:
            pass
            to_be_deleted.append(r)
            results.remove(r)
        else:
            pass
            r['sanitized'] = True
            db.put(r)
    
    db.delete_multi(to_be_deleted)