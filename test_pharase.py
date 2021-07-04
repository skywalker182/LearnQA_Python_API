def test_short_phrase():
    acceptable_len = 15
    phrase = input("Set a phrase: ")
    assert len(phrase) <= acceptable_len, f"Input phrase longer the {acceptable_len}"
