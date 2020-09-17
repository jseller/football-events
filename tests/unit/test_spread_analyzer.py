import logging

from football.events.spread_analyzer import combined_spreads


def test_combined_spreads_data():
    from_date = '2020-09-09'
    to_date = '2020-09-11'
    result = combined_spreads(from_date, to_date)
    assert result is not None
    logging.info(result)
    assert len(result) == 1
