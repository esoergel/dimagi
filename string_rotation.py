import string
import re


word_chars = string.letters + "0123456789_"


def rot13ish(s):
    """
    returns a rot13 version of a string with every other word reversed
    It uses non word characters as word boundaries
    """
    words = re.split(r'(\w*)', s)
    output = []
    even = False
    for word in words:
        if word:
            if word[0] in word_chars:
                # it's a word, not punctuation
                even = not even
                if even:
                    word = word[::-1]
                # why reinvent the wheel?
                word = word.encode("rot13")
            output.append(word)
    return "".join(output)


def test(s):
    """
    checks integrity of the rot13ish function
    """
    if s == rot13ish(rot13ish(s)):
        print "'%s' passed" % s
    else:
        print "'%s' failed" % s
    print rot13ish(s)


# test("Hello, world!")
print rot13ish("Hello, world!")
