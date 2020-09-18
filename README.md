# football-events

ACME Sports wants to develop a dynamic process to return a list of NFL events
in JSON format. It’s dynamic because the process will pull the NFL event data from a remote
API that is frequently updated.

* The API endpoint URLs with the NFL data are below. Please assume that the API
provides no other functionality other than to return the data in JSON format
  
  - Scoreboard: /scoreboard/{league}/{start_date}/{end_date}
  https://delivery.chalk247.com/scoreboard/NFL/<YYYY-MM-DD>/<YYYY-MM-DD>.json?api_key=74db8efa2a6db279393b433d97c2bc843f8e32b0
  https://delivery.chalk247.com/scoreboard/NFL/2020-09-02/2020-09-04.json?api_key=74db8efa2a6db279393b433d97c2bc843f8e32b0

  - Team Rankings: /team_rankings/{league}
  https://delivery.chalk247.com/team_rankings/NFL.json?api_key=74db8efa2a6db279393b433d97c2bc843f8e32b0

* You can assume the API will always return the data in the exact same format, with the
exact same field names and data types.

1. For each event, combine responses from both endpoints to produce the following data
(see example date range and response on page 3):

| Response Label  | Source Label  | Source Endpoint  | Format  |
|---|---|---|---|
| event_id | event_id | scoreboard |  | 
| event_date | event_date | scoreboard | DD-MM-YYYY |  
| event_time | event_date | scoreboard | HH:MM |  
| away_team_id | away_team_id | scoreboard |  |
| away_nick_name | away_nick_name | scoreboard |  |
| away_city | away_city | scoreboard |  | 
| away_rank | rank | team_rankings |  | 
| away_rank_points | adjusted_points | team_rankings | Round up to 2 decimal places | 
| home_team_id | home_team_id | scoreboard |  | 
| home_nick_name | home_nick_name | scoreboard |  |  
| home_city | home_city | scoreboard |  | 
| home_rank | rank | team_rankings |  | 
| home_rank_points | adjusted_points | team_rankings | Round up to 2 decimal places | 


# Functional Requirements

1. Data provider gets scoreboard api data with token - https://github.com/jseller/football-events/issues/2
2. data provider gets rankings api data with token - https://github.com/jseller/football-events/issues/2

3. data provider saves api data in cache
4. data provider updates cached data daily

5. spread analyzer combines scoreboard data and team rankings between dates - https://github.com/jseller/football-events/issues/3

events api returns spread analyzer data between dates
events api returns cached data for 

# Cross functional requirements

## Usability
events api returns standard json data

## Performance
events api should cache api data for 24 hour window
- using live api introduces latency and incurrs expense for redundant requests. To alliviate this the api has 2 levels of cache. This is implemented as a lazy realization, but could be enhanced to pre-fetch data based on availablity of data to provide a consistent response time
-- calls to dependent apis are cached according to the provider
-- results from events api are cached once they are created as underlying data will not change once set


## Security
events api provide ssl connection
events api use tls (ssl connection with dependencies)

events api use authentication
  - user accounts

events api use authorization
  events api check permissions for data
  events api use customer accounts

events api provide oauth2 authentication



# Development
pipenv run pytest tests
pipenv run flake8

pipenv run flask run


# Deployment

docker compose up
- runs on port 5000

http://127.0.0.1:5000/events?from_date=2020-09-09&to_date=2020-09-11

