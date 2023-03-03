# from colorama import init, Fore, Back, Style

# # initialize colorama to work with Windows terminal
# init()

# # print a message in red
# print(Fore.RED + "This text is in red")

# # print a message with a green background
# print(Back.GREEN + "This text has a green background")


# # print a message with bold and yellow text
# print(Style.BRIGHT + Fore.YELLOW + "This text is bold and yellow")

# # reset colorama styles
# print(Style.RESET_ALL + "This text is back to normal")





# from colorama import init, Fore, Back, Style

# # initialize colorama to work with Windows terminal
# init()

# # define a list of all foreground colors
# fg_colors = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

# # define a list of all background colors
# bg_colors = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]

# # print a table of all foreground colors against all background colors
# for fg_color in fg_colors:
#     for bg_color in bg_colors:
#         print(fg_color + bg_color + "  Hello World  ", end="")
#     print(Style.RESET_ALL)





from colorama import init, Fore, Back, Style

# initialize colorama to work with Windows terminal
init()

# define a list of all foreground colors
fg_colors = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

# define a list of all background colors
bg_colors = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]

# define the "Hello World" message with styling
dim = Style.DIM + "Hel"
normal = Style.NORMAL + "lo W"
bright = Style.BRIGHT + "orld"

# print a table of all foreground colors against all background colors with the styled message
for fg_color in fg_colors:
    for bg_color in bg_colors:
        print(fg_color + bg_color + dim + fg_color + bg_color + normal + fg_color + bg_color + bright, end="")
    print(Style.RESET_ALL)




