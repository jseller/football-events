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

