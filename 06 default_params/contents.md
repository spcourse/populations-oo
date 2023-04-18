## Default parameters

In Python, it is possible to set a default value for function parameters. If the function is called without defining a value for that specific parameter, the parameter will get its default value.

Here is an example function that uses default parameter values:

    def greet(name, greeting="Hello"):
        print(greeting, name)

In this function, the parameter `name` is required, while the parameter `greeting` has a default value of `"Hello"`. If the function is called with only one argument:

    greet("John")

the function will use the default value for the greeting parameter and print:

    Hello John

If the function is called with two arguments:

    greet("Jane", "Hi")

the function will use the second argument as the value for the `greeting` parameter and print:

    Hi Jane

### Optional parameters

A common use for default parameter values is in functions that have a lot of parameters. With default parameter values, we can provide sensible default values for some of the parameters and allow the user to omit them if they are not needed.

Suppose we have a function that takes a list of inputs and returns a long string made by joining the inputs together. By default, we would like to join the string with underscores (`'_'`) and to convert all inputs to lowercase. However, we would still like the option to change to use a different separator and to not convert everything to lowercase.

    def create_long_string(lst, separator='_', lowercase=True):
        if lowercase:
            lst = [str(element).lower() for element in list]
        else:
            lst = [str(element) for element in lst]

        return separator.join(lst)

You can set the optional arguments `separator` and `lowercase` to desired values. Here are some examples of using this function:

    print(create_long_string(['a', 'B', 'c']))
    print(create_long_string(['a', 'B', 'c'], '-')
    print(create_long_string(['a', 'B', 'c'], '-', False))

which would give the following output:

    'a_b_c'
    'a-b-c'
    'a-B-c'

In the first example, the list `['a', 'B', 'c']` is passed to the function, and the default values for separator (`'_'`) and lowercase (`True`) are used. The function returns `'a_b_c'`.

In the second example, two arguments are passed to the function. The same list is passed to the function, the value for `separator` is set to `'-'`, and the default value is used for `lowercase` (`True`). The function returns `'a-b-c'`.

In the third example, three arguments are passed to the function. The same list is passed to the function again, and the values for `separator` and `lowercase` are explicitly specified. The function returns `'a-B-c'`.

Note that if we want to set a value for `lowercase`, we also have to set a value for `separator` because the function expects the value for `lowercase` to be in the third position. If we would want to use the default `separator` `'_'`, we would need to pass that explicitly:

    print(create_long_string(['a', 'B', 'c'], '_', False))

When setting up a function with multiple default parameters, it is therefore especially important to order the parameters by importance; variables you are expecting to change more often should come first.

### More advanced use cases

Consider a function that calculates the area of a rectangle:

    def calculate_area(length, width):
        return length * width

If we want to allow the user to omit the `width` parameter and use a default value equal to `length` (resulting in the area of a square), we can modify the function like this:

    def calculate_area(length, width=None):
        if width is None:
            width = length
        return length * width

Inside the function, we check if the `width` parameter is `None`. If it is, we set `width` equal to `length`. This allows the caller to omit the `width` parameter and use the same value for both `length` and `width`.

For example, if we call the function with both `length` and `width`:

    calculate_area(5, 3)

the function will return the area of a rectangle with `length` `5` and `width` `3`.

If we call the function with only `length`:

    calculate_area(5)

the function will use the default value of `None` for `width`, and set `width` equal to `length`. This will return the area of a square with sides of `length` `5`.

> Note that we chose a value of `None` here as the default value, and not `0` (zero), as the number `0` does have meaning in the context of this function. If we would use the function with `calculate_area(5, 0)`, calculating the area of a rectangle where one side has length `0`, we would expect the function to return `0`.

Using an `if` statement to handle a default value of `None` in this way can be useful for cases where the default value is more complex than a simple value or expression, or where we need to perform additional logic to determine the default value.
