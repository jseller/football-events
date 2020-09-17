
from football.events.data_provider import ranking_data, scoreboard_data


def test_data_provider_scoreboard_data():
    from_date = '2020-01-01'
    to_date = '2020-01-08'
    response = scoreboard_data(from_date, to_date)
    assert response.get('hash') is not None


def test_data_provider_ranking_data():
    response = ranking_data()
    assert response.get('hash') is not None
