"""
Question: https://www.hackerrank.com/challenges/python-string-formatting/problem
pending
"""
def print_formatted(number):
    # your code goes here
    maxLen = len('{0:b}'.format(int(number)))
    space = " "*maxLen
    for i in range(1,number+1):
        decimal = str(i)
        octal = str(oct(i))[2:len(str(oct(i)))]
        hexDec = str(hex(i))[2:len(str(hex(i)))].upper()
        binary = '{0:b}'.format(int(i))
        binSpace = " "*(maxLen - len(binary))
        binSpace = " "*(maxLen - len(binary))
        formattedString = decimal.rjust(maxLen +1) + octal.rjust(maxLen +1)  + hexDec.rjust(maxLen +1) + binary.rjust(maxLen +1)
        print(formattedString)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)