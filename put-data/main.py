from google.cloud import datastore
import json
import random
import time

def get_nonce():
    pass
    t = time.time()
    t = int(t*1000)
    return str(t)

def put_data(request, body=None):
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


    print(request.get_json(silent=True))
    print(request.args.to_dict(flat=False))
    
    if request:
        args = request.get_json(silent=True)
        if 'signs' in args and len(args['signs']) > 0 and 'fate' in args:
            signs = args['signs']
            fate = str(args['fate'])
            db = datastore.Client()
            new_horror = datastore.Entity(datastore.Key('horrorscope', get_nonce(), project='my-horrorscopes'))
            new_horror['signs'] = signs
            new_horror['fate'] = fate
            new_horror['sanitized'] = False
            new_horror['reported'] = False
            print(signs)
            db.put(new_horror)

    return (json.dumps({'message': 'thanks'}), 200, headers)