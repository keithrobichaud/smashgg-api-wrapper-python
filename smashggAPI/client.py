from sgqlc.endpoint.http import HTTPEndpoint
import os
import json

url = 'https://api.smash.gg/gql/alpha'

class MissingAPIKeyError(Exception):
	pass

SMASHGG_API_KEY = os.environ.get('SMASHGG_API_KEY', None)
if SMASHGG_API_KEY is None:
	raise MissingAPIKeyError('''
			All requests require an API key.
			See https://developer.smash.gg for more info.
		'''
	)

class client(object):
	def __init__(self, apiKey):
		pass

	def query(query, variables):
		headers = {'Authorization': 'Bearer ' + SMASHGG_API_KEY}

		endpoint = HTTPEndpoint(url, headers)
		data = endpoint(query, variables)

		if 'errors' in data:
			raise Exception(data['errors'])

		return data
