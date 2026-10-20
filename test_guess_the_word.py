# Dale Rubenstein
# CIS256 Fall 2026
# Programming Assignment 4.test_guess_the_word

"""
Test program to test the guess_the_word program.  It took a while to set
up the envrionment properly along with using git. Found good reference
material for pytest at: https://docs.pytest.org/en/6.2.x/capture.html.

Note: pytest -vv provides more feedback, specifies which tests pass or fail
"""

from guess_the_word import show_secret, user_guess, get_the_letters, chosen_word, words
import pytest


#Testing to see if the random word is in words, should pass
def test_chosen_word():
    result = chosen_word(words)
    assert result in words


"""
using 'capsys', a built in pytest fixture that captures what the
test writes to output. Had to do some digging
"""
#test 1: pass
def test_show_secret(capsys):
    show_secret("DOG", ["D","G"])

    captured = capsys.readouterr() # retrieves the captured output
    assert captured.out == "D _ G\n\n" # asserts the output matches 

#Test 2 should pass
def test_user_guess():
    secret = "DRACULA"
    guess = "X"
    assert user_guess(guess, secret) is False, \
        f"Expected True for '{guess}' in '{secret}', got {user_guess(guess, secret)}"

#test 3 should fail
def test_user_guess_1():
    secret = "DRACULA"
    guess = "X"
    assert user_guess(guess, secret) is True, \
        f"Expected True for '{guess}' in '{secret}', got {user_guess(guess, secret)}"


# Test 4 should fail & not raise the ValueError
def test_multi_letter_guess():
    with pytest.raises(ValueError, match="Single letters only please."):
        user_guess("a", "secret")

# Test 5 should pass & raise the ValueError
def test_multi_letter_guess_1():
    with pytest.raises(ValueError, match="Single letters only please."):
        user_guess("ab", "secret")
  

#Test 6, Testing numbers, should raise ValueError
def test_non_alpha_guess():
    with pytest.raises(ValueError, match="Single letters only please."):
        user_guess("123", "secret")
   
# Test 7, Testing symbols should raise ValueError
def test_non_alpha_guess_1():
    with pytest.raises(ValueError, match="Single letters only please."):
        user_guess("@", "secret")

#Test 8, expect to pass empty string & pass
def test_empty_string():
    assert get_the_letters("") == ""

# Test 9, expect to pass a string & fail
def test_empty_string_1():
    assert get_the_letters("A") == ""

# Test 10, expect to pass
def test_all_unique_letters():
    word = "banana"
    result = get_the_letters(word)
    assert set(result) == {"a", "b", "n"}


# Test 11, expect to fail
def test_all_unique_letters():
    word = "banana"
    result = get_the_letters(word)
    assert set(result) == {"a", "b", "n", "c"}