from google.cloud import datastore
import time

bad_words = [
    'hitler',
    'hilter',
    'nigger',
    'niger',
    'nigga',
    'cunt',
    'gangbang',
    'rape',
    'hore',
    'hoar',
    'nazi',
    'swastika',
    'tranny',
    'whitepower'
]

def get_nonce():
    pass
    t = time.time()
    t = int(t*1000)
    return str(t)

def sanitize_data(request=None, body=None):
    pass
    db = datastore.Client()
    to_be_deleted = []
    query = db.query(kind='horrorscope')
    batch = db.batch()
    batch.begin()
    query.add_filter('sanitized', '=', False)
    results = query.fetch(limit=10)
    for r in results:
        pass
        for bad_word in bad_words:
            pass
            if bad_word in r['fate'].lower() and r.key not in to_be_deleted:
                pass
                batch.delete(r.key)
                to_be_deleted.append(r.key)
        if r.key not in to_be_deleted:
            pass
            r['sanitized'] = True
            batch.put(r)
    batch.commit()