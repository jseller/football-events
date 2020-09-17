
from football.events.data_provider import ranking_data, scoreboard_data


def get_event_data(event_data, rankings):
    result = {}
    result['event_id'] = event_data['event_id']
    event_date = event_data['event_date'].split(' ')
    result['event_date'] = event_date[0]
    result['event_time'] = event_date[1]
    away_id = event_data.get('away_team_id')
    result['away_team_id'] = away_id
    result['away_nick_name'] = event_data['away_nick_name']
    home_id = event_data.get('home_team_id')
    result['home_team_id'] = home_id
    result['home_nick_name'] = event_data['home_nick_name']
    for rank in rankings:
        if rank.get('team_id') == home_id:
            result['home_rank'] = rank.get('rank')
            result['home_rank_points'] = round(float(rank.get('adjusted_points')), 2)
        if rank.get('team_id') == away_id:
            result['away_rank'] = rank.get('rank')
            result['away_rank_points'] = round(float(rank.get('adjusted_points')), 2)
    return result


def combined_spreads(from_date, to_date):
    scoreboard = scoreboard_data(from_date, to_date).get('results')
    rankings = ranking_data().get('results').get('data')
    events = []
    for score in scoreboard:
        if scoreboard[score]:
            data = scoreboard[score].get('data')
            for event in data:
                events.append(get_event_data(data[event], rankings))
    return events
