def int_to_roman(num):

    # Create value dict
    roman_list = [(1000,'M'), (900,'CM'), (500,'D'), (400,'CD'), (100,'C'), (90,'XC'), (50,'L'), (40,'XL')]
    roman_list2 = [(10,'X'), (9,'IX'), (5,'V'), (4,'IV'), (1,'I')]

    roman_list += roman_list2
    roman_numberal = ''

    if num < 0 or  num > 3999:
        raise ValueError("{} is not a roman numberal".format(num))
    # Return zero
    if num == 0 :
        return "N"
    #Return value:
    else:
        while num > 0:
            for i,r in roman_list:
                while num >= i:
                    roman_numberal += r
                    num-=i
    return roman_numberal


def roman_to_int(s):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            int_val += rom_val[s[i]]


    if s == int_to_roman(int_val):
        return int_val
    else:
        return TypeError("{} is not a roman_numberal".format(s))
