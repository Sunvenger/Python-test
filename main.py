from limited_type import Limited_var
from checker import do_test
from colorama import init

init(autoreset=True)
print "Main called !"

a=Limited_var(-5,57,1)
print a
do_test(a)

a=Limited_var(-5,5000,1)
do_test(a)

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

