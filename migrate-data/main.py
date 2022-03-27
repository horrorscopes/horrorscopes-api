from google.cloud import datastore
import time

def get_nonce():
    pass
    t = time.time()
    t = int(t*1000)
    return str(t)

def sanitize_data():
    pass
    db = datastore.Client()
    to_be_deleted = []
    query = db.query(kind='horrorscope')
    batch = db.batch()
    batch.begin()
    results = query.fetch()
    for r in results:
        pass
        r['sanitized'] = True
        batch.put(r)
    batch.commit()

def migrate_data(request=None, body=None):
    pass
    # Add your migrations below. Include a comment with the date, and what its meant to do.
    # Commented functions have already run on the date of the comment
    # 27.03.2022 - adds sanitized column to data
    sanitize_data()