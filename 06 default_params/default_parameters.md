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

### More advanced use cases

A common use for default parameter values is in functions that have a lot of parameters. With default parameter values, we can provide sensible default values for some of the parameters and allow the user to omit them if they are not needed.

For example, consider a function that calculates the area of a rectangle:

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

Using an `if` statement to handle a default value of `None` in this way can be useful for cases where the default value is more complex than a simple value or expression, or where we need to perform additional logic to determine the default value.
