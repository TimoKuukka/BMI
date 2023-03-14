# questions.py tests can be found here
# ------------------------------------

import questions

# Test static conversion method to integer using monkeypathc
def test_ask_user_integer(monkeypatch):
    user_input = '100'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    assert questions.Question.ask_user_integer(
        'Anna kokonaisluku', False) == (100, 'OK', 0, 'Conversion successful')

# Test if conversion to float works as expected
def test_ask_user_float(monkeypatch):
    user_input = '1.5'
    # Use anonymous function to create input from variable
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    assert questions.Question.ask_user_float('Anna liukuluku: ', False) == (
        1.5, 'OK', 0, 'Conversion successful')

# Test an error condition when user adds a unit to a floating point number
def test_ask_user_float2(monkeypatch):
    user_input = '1.5v'
    # Use anonymous function to create input from variable
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    assert questions.Question.ask_user_float('Anna kokonaisluku: ', False) == (
        0, 'Error', 1, "could not convert string to float: '1.5v'")

# Test an error condition when user uses comma instead of dot as decimal separator
def test_ask_user_float3(monkeypatch):
    user_input = '74,6'
    # Use anonymous function to create input from variable
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna kokonaisluku')
    assert questions.Question.ask_user_float('Anna kokonaisluku: ', False) == (
        0, 'Error', 1, "could not convert string to float: '74,6'")

# Test conversion to boolean: case Y
def test_ask_user_boolean(monkeypatch):
    user_input = 'y'
    # Use anonymous function to create input from variable
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    assert questions.Question.ask_user_boolean('Haluatko jatkaa', 'Y', 'N', False) == (
        True, 'OK', 0, 'Conversion successful')

# Test conversion to boolean: case N


# Simulate user input using Monkeypathc library
def test_ask_user_boolean2(monkeypatch):
    user_input = 'n'
    # Use anonymous function to create input from variable
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    assert questions.Question.ask_user_boolean('Haluatko jatkaa', 'Y', 'N', False) == (
        False, 'OK', 0, 'Conversion successful')

# Test an error condition
def test_ask_user_boolean3(monkeypatch):
    user_input = 'v'
    # Use anonymous function to create input from variable
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    assert questions.Question.ask_user_boolean('Haluatko jatkaa: ','Y', 'N', False) == (
        'N/A', 'Error', 1, 'unable to convert to boolean')


