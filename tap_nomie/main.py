import couchdb
import singer
import json

REQUIRED_CONFIG_KEYS = ["endpoint", "api_key"]

def main():

  args = singer.utils.parse_args(REQUIRED_CONFIG_KEYS)

  config = args.config

  db_full_url = 'https://' + config['endpoint'] + ':' + config['api_key'] + '@' + config['endpoint'] + '.cloudantnosqldb.appdomain.cloud'

#  session = client.session()
#  db_name = client.all_dbs()[0]
#  nomie_db = client[db_name]
#  import pdb;pdb.set_trace()

  couch = couchdb.Server(db_full_url)

  db = couch['nomie-db']

  schema = {'type': 'object',
    'properties':
      {
        '_id': {'type': 'integer'},
      }}

  singer.write_schema('books', schema, 'id')

  for book in db:
    if 'books' in book and not book.endswith('_last'):
      data = db[book]['data']
      singer.write_records('books', data)


main()
