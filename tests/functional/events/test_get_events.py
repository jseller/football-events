from http import HTTPStatus

EXPECTED_FIELDS = [
    'id',
    'image',
    'design',
    'permissions'
]


def test_can_get_events(testapp):
    res = testapp.get('/events')
    assert res.status_code == HTTPStatus.OK
