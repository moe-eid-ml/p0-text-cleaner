from clean import basic_clean

def test_basic_clean_removes_punct_and_emoji():
    assert basic_clean("Hello, World! 😊") == "hello world"

def test_basic_clean_handles_nonstring():
    assert basic_clean(123) == 123

def test_basic_clean_keep_emoji_true():
    # when keep_emoji=True, emoji should remain
    from clean import basic_clean
    assert basic_clean("Hi 😊!", keep_emoji=True) == "hi 😊"
