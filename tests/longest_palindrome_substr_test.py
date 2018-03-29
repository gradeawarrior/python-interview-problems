"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum
length of s is 1000.

Example:

    Input: "babad"
    Output: "bab"

    Note: "aba" is also a valid answer.

Example:

    Input: "cbbd"
    Output: "bb"
"""

import pytest
from project.longest_palindrome_substr import Solution
from time import time


@pytest.mark.parametrize("test_input, expected", [
    ("babad", "bab"),
    ("cbbd", "bb"),
    ("", ""),
    ("a", "a"),
    ("ab", "a"),
    ("abc", "a"),
    ("abcdd", "dd"),
    ("aaabaaaa", "aaabaaa"),
    ("salas", "salas"),
    ("psalas", "salas"),
    ("peter salas", "salas"),
    ("abcdefghijklmnopqrstuvwxyz", "a"),
    ("abcdefghijklmmnopqrstuvwxyz", "mm"),
    ("abcdefghijklmnopqrstuvwxyzz", "zz"),
    ("abcdefghijklmnopqrstuvwxyzzz", "zzz"),
    ("kztakrekvefgchersuoiuatzlmwynzjhdqqftjcqmntoyckqfawikkdrnfgbwtdpbkymvwoumurjdzygyzsbmwzpcxcdmmpwzmeibligwiiqbecxwyxigikoewwrczkanwwqukszsbjukzumzladrvjefpegyicsgctdvldetuegxwihdtitqrdmygdrsweahfrepdcudvyvrggbkthztxwicyzazjyeztytwiyybqdsczozvtegodacdokczfmwqfmyuixbeeqluqcqwxpyrkpfcdosttzooykpvdykfxulttvvwnzftndvhsvpgrgdzsvfxdtzztdiswgwxzvbpsjlizlfrlgvlnwbjwbujafjaedivvgnbgwcdbzbdbprqrflfhahsvlcekeyqueyxjfetkxpapbeejoxwxlgepmxzowldsmqllpzeymakcshfzkvyykwljeltutdmrhxcbzizihzinywggzjctzasvefcxmhnusdvlderconvaisaetcdldeveeemhugipfzbhrwidcjpfrumshbdofchpgcsbkvaexfmenpsuodatxjavoszcitjewflejjmsuvyuyrkumednsfkbgvbqxfphfqeqozcnabmtedffvzwbgbzbfydiyaevoqtfmzxaujdydtjftapkpdhnbmrylcibzuqqynvnsihmyxdcrfftkuoymzoxpnashaderlosnkxbhamkkxfhwjsyehkmblhppbyspmcwuoguptliashefdklokjpggfiixozsrlwmeksmzdcvipgkwxwynzsvxnqtchgwwadqybkguscfyrbyxudzrxacoplmcqcsmkraimfwbauvytkxdnglwfuvehpxd", "dtzztd"),
    ])

def test_add_two_numbers(test_input, expected):
    threshold = 700
    start = time()
    assert Solution().longestPalindrome(test_input) == expected
    duration = (time() - start) * 1000 # Duration in ms
    assert duration < threshold, "Expecting duration to be < %s ms" % threshold
