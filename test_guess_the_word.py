# Dale Rubenstein
# CIS256 Fall 2026
# Programming Assignment 4.test_guess_the_word

"""
Test program to test the guess_the_word program.  It took a while to set
up the envrionment properly along with using git. Found good reference
material for pytest at: https://docs.pytest.org/en/6.2.x/capture.html.
"""

from guess_the_word import show_secret, user_guess, get_the_letters

"""
using 'capsys', a built in pytest fixture that captures what the
test writes to output. Had to do some digging
"""
def test_show_secret(capsys):
    show_secret("DOG", ["D","G"])

    captured = capsys.readouterr() # retrieves the captured output
    assert captured.out == "D _ G\n\n" # asserts the output matches 








