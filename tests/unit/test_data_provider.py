
from football.events.data_provider import ranking_data, scoreboard_data


def test_data_provider_scoreboard_data():
    from_date = '2020-01-01'
    to_date = '2020-01-08'
    token = '74db8efa2a6db279393b433d97c2bc843f8e32b0'
    response = scoreboard_data(from_date, to_date, token)
    assert response.get('hash') is not None


def test_data_provider_ranking_data():
    token = '74db8efa2a6db279393b433d97c2bc843f8e32b0'
    response = ranking_data(token)
    assert response.get('hash') is not None
