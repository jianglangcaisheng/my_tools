
# tool_basic.print_red("%s, %s" % (__file__, sys._getframe().f_lineno), e)
def print_red(my_str, default_color_str=""):
    if default_color_str == "":
        print("\033[0;30;41m\t%s\033[0m" % my_str)
    else:
        print("\033[0;30;41m\t%s:\033[0m" % my_str, end=" ")
        print(default_color_str)


# i = 1
# print("Finish: %d/%d" % (i, 1))
# i += 1

