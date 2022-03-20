from google.cloud import datastore
import json
import random

def get_data(request, body=None):
    pass
    
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    if request.method == 'OPTIONS':
        # Allows POST requests from origin * with
        # Accept header
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'content-type'
        }
        return ('', 204, headers)

    if request and request.args and 'sign' in request.args:
        sign = str(request.args['sign'])
        
        db = datastore.Client()
        query = db.query(kind='horrorscope')
        query.add_filter('sanitized', '=', True)
        results = query.fetch()
        fate = ''
        fates = []
        for r in results:
            if sign in r['signs']:
                fates.append(r['fate'])
        if len(fates) > 0:
            fate = random.choice(fates)
        return (json.dumps({'fate': fate}), 200, headers)
    else:
        return (json.dumps({'error': 'No sign or incorrect sign'}), 500, headers)