from smashggAPI import client
import pytest

def test_tournament_info():
	"""Tests an API call to get a Tournament's info"""

	result = client.query('''
		query TournamentInfo ($slug: String!) {
			tournament(slug: $slug) {
				id
				name
			}
		}
	''',
	{
		"slug": "genesis-6"
	})

	assert isinstance(result, dict)
	assert result['data']['tournament']['name'] == "Genesis 6", "The name should be in the response"

def test_tournament_error():
	"""Tests a bad API call"""

	with pytest.raises(Exception):
		client.query('''
			query TournamentInfo ($slug: String!) {
				tournament(slug: $slug) {
					id
					name
				}
			}
		''', {})
