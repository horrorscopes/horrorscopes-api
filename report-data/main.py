from google.cloud import datastore
import json
import random
import time

def get_nonce():
    pass
    t = time.time()
    t = int(t*1000)
    return str(t)

def report_data(request, body=None):
    pass
    
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    if request.method == 'OPTIONS':
        # Allows POST requests from origin * with
        # Accept header
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'content-type'
        }
        return ('', 204, headers)
    
    if request:
        args = request.get_json(silent=True)
        if 'fate' in args:
            fate = str(args['fate'])
            db = datastore.Client()
            batch = db.batch()
            batch.begin()
            query = db.query(kind='horrorscope')
            query.add_filter('fate', '=', fate)
            results = query.fetch()
            for r in results:
                pass
                r['reported'] = True
                batch.put(r)
            batch.commit()

    return (json.dumps({'message': 'thanks'}), 200, headers)