from app.wx_client import complete

def test_complete():
    assert isinstance(complete("Hola", max_tokens=5), str)
