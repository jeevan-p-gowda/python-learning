# First class function
# A programming language is said to have first class functions if it treats functions as first-class citizens.

# First-Class Citizen (Programming)
# "First-class citizen (sometimes called first-class objects) in a programming language is an
# entity which supports all the operation generally available to other entities. These operations typically include
# being passed as an argument, returned from a function, and assigned to a variable."

def square(x):
    return x * x


f = square
print(f(5))


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


l = my_map(square, [1, 2, 3, 4, 5])
print(l)


# use case: if there is a commanility we can use this type of approach
# In below example, tag is common
def html_tag(tag):
    def html_msg(msg):
        print('<{0}>{1}<{0}>'.format(tag, msg))

    return html_msg


print_h1 = html_tag('h1')
print_h1('Hello')
print_h1('World')
