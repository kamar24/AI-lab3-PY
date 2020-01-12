def print_two(a, b):
    print("Argumenty: 0,1".format(a, b))

try:
    print_two(4, 1, b=1)
except TypeError:
    print("1. Wrong type") #prediction: error
try:
    print_two(1, a=1)
except TypeError:
    print("2.Wrong type") #predictions: good
try:
    print_two(b=1, a=4)
except TypeError:
    print("3.Wrong type") #predictions: good
try:
    print_two(a=4, b=1)
except TypeError:
    print("4.Wrong type") #predictions: good
try:
    print_two(eval('b=4, 1'))
except SyntaxError:
    print("5.Wrong syntax")#predictions: good
try:
    print_two(4, a=1)
except TypeError:
    print("6.Wrong type")#predictions: good
try:
    print_two(4, 1, 1)
except TypeError:
    print("7.Wrong type")#predictions: error
try:
    print_two(4, a=1)
except TypeError:
    print("8.Wrong type")#predictions: good
try:
    eval('print_two(a=4, 1)')
except SyntaxError:
    print("9.Wrong syntax")#predictions: error
try:
    print_two(41)
except TypeError:
    print("10.Wrong type")#predictions: error
try:
    print_two(4,1)
except TypeError:
    print("11.Wrong type")#predictions: good
try:
    print_two()
except TypeError:
    print("12.Wrong type")#predictions: good
