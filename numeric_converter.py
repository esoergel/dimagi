ones_digit = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

annoying = {
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

tens_digit = {
    1: "ten",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}

def translate(n):
    """
    outputs the spoken-language format of n
    Accepts any number less than 1 billion
    """
    if n >= 10**9:
        return "this function only accepts numbers below 1 billion"

    output = []
    if n%100 in annoying:
        output = [ annoying[n%100] ]
    else:
        if n%10:
            output = [ ones_digit[n%10] ]
        if n%100/10:
            output.insert(0, tens_digit[n%100/10])
    if n%1000/100:
        hundreds = "%s hundred" % ones_digit[n%1000/100]
        output.insert(0, hundreds)
    if n%10**6/1000:
        thousands = "%s thousand" % translate(n%10**6/1000)
        output.insert(0, thousands)
    if n/10**6:
        millions = "%s million" % translate(n/10**6)
        output.insert(0, millions)
    return " ".join(output)

for i in [6, 12, 73, 231, 334, 9852, 10015, 201708, 301600892]:
    print translate(i)