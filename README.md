# smashgg-api-wrapper-python

# How to use:
1. `pip install smashggAPI`
2. Add your public API key as an environmental variable:
  
  In .bashrc/whatever equivalent file:
  ```
  export SMASHGG_API_KEY='your api key here'
  ```
3. 
```
from smashggAPI import client

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
```

# Contributing

## Running tests

1. `python -m pip install -r requirements.txt`
2. `python -m pytest`
