# def strcount(s):
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)
#

def strcount(s):
    mydct = {}
    for sym in s:
        mydct[sym] = mydct.get(sym, 0) + 1

    for key in mydct:
        print(key, mydct.get(key))

strcount('adsavawd')

