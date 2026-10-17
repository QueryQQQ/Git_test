import my_utils.str_util
print(my_utils.str_util.str_reverse("黑马程序员"))
print(my_utils.str_util.substr("ithema", 0, 4))

from my_utils import file_util
file_util.print_file_info("D:/test_append.txt")
file_util.append_to_file("D:/test_append.txt", "今天也要努力学习喵")