import my_utils.file_util
from my_utils import str_util

print(my_utils.str_util.str_reverse('hahahahaha'))
print(my_utils.str_util.substr('heheheeh', 4,5))

my_utils.file_util.print_file_info('./my_utils/bill.txt')
my_utils.file_util.append_to_file('./my_utils/python.txt', '\n123')
