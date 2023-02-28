## Keyword arguments

In Python, keyword arguments can be used to pass arguments to a function using their parameter names. This can make code more readable and help avoid errors when calling functions with many parameters, since it also allows you to change the order of the parameters.

Here's an example:

    def print_info(name, age, city):
        print(f"{name} is {age} years old and lives in {city}.")

In this function, we have three parameters: `name`, `age`, and `city`. If we call the function and pass arguments by position, we need to make sure that we pass them in the correct order:

    print_info("Alice", 30, "New York")

Which will output:

    Alice is 30 years old and lives in New York.

If we accidentally swap the order of the arguments, we might get unexpected results:

    print_info("New York", 30, "Alice")

This will output:

    New York is 30 years old and lives in Alice.

To avoid this kind of error, we can use keyword arguments. Instead of passing the arguments by position, we can pass them using their parameter names:

    print_info(name="Alice", age=30, city="New York")
    print_info(city="New York", age=30, name="Alice")

Which will, despite the order being different, both produce the same output as before:

    Alice is 30 years old and lives in New York.
    Alice is 30 years old and lives in New York.

By using keyword arguments, we can make our code more readable and avoid errors caused by passing arguments in the wrong order.

### `**kwargs` in functions

In addition to positional and keyword arguments, Python also allows us to use the `**kwargs` notation to pass a variable number of keyword arguments to a function.

Here's an example of a function that uses `**kwargs`:

    def print_kwargs(**kwargs):
        for key, value in kwargs.items():
            print(f"{key} = {value}")

As you can see, the arbitrary number of keyword arguments passed to the function will be collected in a dictionary named `kwargs`. In this dictionary, the keys are the names of the arguments provided, and the values of the dictionary are the values that were assigned to these arguments. We can use the example we have used previously:

    print_kwargs(name="Alice", age=30, city="New York")

Which will produce the following output:

    name = Alice
    age = 30
    city = New York

In this case, the `kwargs` dictionary inside the `print_kwargs` function will look like:

    {
        "name": "Alice",
        "age": 30,
        "city": "New York",
    }

As we've described before, the number of keyword arguments passed to the function is variable. This means we can even call this function without any arguments:

    print_kwargs()

This will produce no output, as there are no elements in the dictionary to loop over. The dictionary `kwargs` is empty.

## `**kwargs` when calling functions

The special `**kwargs` notation can also be used when passing arguments to a function. This is called _unpacking_. This is especially useful when a function has a lot of arguments, or when we want to pass arguments with values that are stored in a dictionary.

    info_kwargs = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
    }

The `print_info` function that we defined in an earlier example has three arguments: `name`, `age`, and `city`. The dictionary `info_kwargs` contains the names of these three arguments, and the values we would like to assign to them. We can call the `print_info` function and pass the `info_kwargs` dictionary using the `**` operator:

    print_info(**info_kwargs)

Which is equivalent to calling the function with three separate keyword arguments:

    print_info(name="Alice", age=30, city="New York")

The advantage of using `**kwargs` in this way is that we can pass a large number of keyword arguments to a function without having to type them all out. This can make our code more readable and reduce the risk of typos or other errors.

We can also use `**kwargs` to pass keyword arguments that are stored in a dictionary. For example, if we have a function that takes a large number of keyword arguments, we might store those arguments in a configuration file or database, and then load them into a dictionary and pass them to the function using `**kwargs`.
