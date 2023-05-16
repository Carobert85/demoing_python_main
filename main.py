from example_from_a_different_file import example_from_a_different_file


def example_in_same_file():
    print('this example comes from this file')


def this_example_combines_both_previous_examples():
    example_in_same_file()
    example_from_a_different_file()


if __name__ == '__main__':
    # from the same file
    example_in_same_file()
    # from a different file
    example_from_a_different_file()
    # combined in a function
    print('this demos a function call that combines other functions')
    this_example_combines_both_previous_examples()
