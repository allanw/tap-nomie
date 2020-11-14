import couchdb
import singer
import json

REQUIRED_CONFIG_KEYS = ["endpoint", "api_key"]

schema = {'type': 'object',
  'properties':
    {
      '_id': {'type': 'string'},
      'note': {'type': 'string'},
      'start': {'type': 'integer'},
      'lat': {'type': ['number', 'null']},
      'lng': {'type': ['number', 'null']}
    }}

def get_catalog(schema):
  streams = []

  for schema_name, schema in schema['properties'].items():
    catalog_entry = {
            'stream': schema_name,
            'tap_stream_id': schema_name,
            'schema': schema,
            'metadata': [], 
            'key_properties': 'summary_date' 
    }
    streams.append(catalog_entry) 

  return {'streams': streams}

def do_discover(schema):
  catalog = get_catalog(schema)
  print(json.dumps(catalog, indent=2))

def do_sync(config, schema):

  db_full_url = 'https://' + config['endpoint'] + ':' + config['api_key'] + '@' + config['endpoint'] + '.cloudantnosqldb.appdomain.cloud'

#  session = client.session()
#  db_name = client.all_dbs()[0]
#  nomie_db = client[db_name]
#  import pdb;pdb.set_trace()

  couch = couchdb.Server(db_full_url)

  db = couch['nomie-db']

  singer.write_schema('books', schema, '_id')

  for book in db:
    if 'books' in book and not book.endswith('_last'):
      data = db[book]['data']
      singer.write_records('books', data)

def main():
  args = singer.utils.parse_args(REQUIRED_CONFIG_KEYS)

  if args.discover:
    do_discover(schema)
  else:
    do_sync(args.config, schema)

if __name__ == '__main__':
  main()
