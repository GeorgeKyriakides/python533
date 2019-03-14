def my_print4(message):
    print('This is print 4: ', message)


my_msg = 'Hello 4'
my_print4(my_msg)

# =============================================================================
# GUARD THIS CODE AGAINST IMPORTS
# =============================================================================


def main():
    my_msg = 'Hello 4 from main'
    my_print4(my_msg)


if __name__ == '__main__':
    main()
