
# tool_basic.print_red("%s, %s" % (__file__, sys._getframe().f_lineno), e)
def print_red(my_str, default_color_str=""):
    if default_color_str == "":
        print("\033[0;30;41m\t%s\033[0m" % my_str)
    else:
        print("\033[0;30;41m\t%s:\033[0m" % my_str, end=" ")
        print(default_color_str)


def fun1(x):
    return x + 1

def save_float(x, num_float):
    return round(x, num_float)

def int_round(x, num_0):
    num_level = pow(10, num_0)
    return x // num_level * num_level

if __name__ == "__main__":
    if 0:
        fun2 = fun1
        print(fun2(1))
    if 0:
        x = 0.123456789
        print(x)
        print(save_float(x, 6))
    if 1:
        print(int_round(123, 2))

# i = 1
# print("Finish: %d/%d" % (i, 1))
# i += 1

