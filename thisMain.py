import json
import random

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass#Do I need to close the file?
    return i + 1

# def random_line(afile):
#     line = next(afile)
#     for num, aline in enumerate(afile, 2):
#         if random.randrange(num):
#             continue
#         line = aline
#     return line

nLines = file_len("text.txt")
deck = list(range(nLines))
random.shuffle(deck)

f= open("text.txt",'r')
for i in range(nLines):
    i = 0
    for num in f:
        if i == deck[0]:
            print(num)
        i += 1
# print(deck)

# for i in range(nLines):
#     # print("i:"+ str(i))
#     for j in range(nLines):
#         # print("j:" + str(j))
#         for num in f:
#             print(num)
#             if deck[i] == j:
#                 print(num)


#https://stackoverflow.com/questions/3540288/how-do-i-read-a-random-line-from-one-file
#https://stackoverflow.com/questions/845058/how-to-get-line-count-of-a-large-file-cheaply-in-python
