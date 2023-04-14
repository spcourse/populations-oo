## Keyword arguments

In Python, keyword arguments can be used to pass arguments to a function using their parameter names. This can make functions with many input paramaters a lot easier to use when only few of these parameters are changed. It also makes your code more readable, and helps avoid errors, since it also allows you to change the order of the parameters.

Here's an example:

    def print_info(name, age, city):
        print(f'{name} is {age} years old and lives in {city}.')

In this function, we have three parameters: `name`, `age`, and `city`. If we call the function and pass arguments by position, we need to make sure that we pass them in the correct order:

    print_info('Alice', 30, 'New York')

Which will output:

    Alice is 30 years old and lives in New York.

If we swap the order of the arguments, we might get unexpected results:

    print_info('New York', 30, 'Alice')

This will output:

    New York is 30 years old and lives in Alice.

Instead of passing the arguments by position, we can pass them using their parameter names:

    print_info(name='Alice', age=30, city='New York')
    print_info(city='New York', age=30, name='Alice')

Which will, despite the order being different, both produce the same output as before:

    Alice is 30 years old and lives in New York.
    Alice is 30 years old and lives in New York.

This also works when you have a function that has *default arguments*, and comes in especially handy when you want to change only one specific argument to some value that is not its default. The following function has 3 default arguments and calculates the volume of a beam:

    def calculate_volume(height=1, width=1, depth=1):
        return height * width * depth

By default, the function calculates the volume of a beam with a `height`, `width`, and `depth` of length 1 (a cube). If we would like to change just the `depth` of the beam to the value `3` *without* using *keyword arguments*, we would need to do the following:

    print(calculate_volume(1, 1, 3))

However, if we use keyword arguments, the following is also possible:

    print(calculate_volume(depth=3))

By not providing values for the `height` and `width` arguments, they assume their default values of `1`, while the value for `depth` is specifically set to `3`.

## Passing a dictionary of keyword arguments with `**`

In addition to positional and keyword arguments, Python also allows us to use the so-called `**kwargs` notation to pass a number of keyword arguments to a function as a dictionary.

    info_kwargs = {
        'name': 'Alice',
        'age': 30,
        'city': 'New York',
    }

The `print_info` function that we defined in an earlier example has three arguments: `name`, `age`, and `city`. The dictionary `info_kwargs` we defined above contains the names of these three arguments, and the values we would like to assign to them. We can call the `print_info` function and pass the `info_kwargs` dictionary using the `**` operator:

    print_info(**info_kwargs)

This is called _unpacking_ and is equivalent to calling the function with three separate keyword arguments:

    print_info(name='Alice', age=30, city='New York')

This is especially useful when a function has a lot of arguments, we want to call the function many times with a set of different arguments, or when we want to pass arguments with values that are stored in a dictionary.

The advantage of using `**kwargs` in this way is that we can pass a large number of keyword arguments to a function without having to type them all out separately. This can make our code more readable, but also makes it very easy to change just one value at the time.

    for alice_age in range(30, 50):
        info_kwargs['age'] = alice_age
        print_info(**info_kwargs)

> If we have a function that takes a large number of keyword arguments, we might store those arguments in a configuration file or database, and then load them into a dictionary and pass them to the function using `**kwargs`.

### Unpacking arguments

Another useful feature in Python is positional argument unpacking. This allows you to expand an iterable (such as a list or tuple) into separate arguments when calling a function. This is done by placing an asterisk (`*`) before the iterable argument in the function call.

    def fun(arg1, arg2, arg3):
        print(arg1)
        print(arg2)
        print(arg3)

    lst = [1, 2, 3]
    fun(*lst)

In the example above, the `lst` variable is a list of three elements. When `fun()` is called with `*lst`, our list is unpacked and its elements are passed as separate positional arguments to the function. This is equivalent to calling `fun(1, 2, 3)`.

You can also use positional argument unpacking with a mix of regular arguments and iterable arguments:

    lst = [2, 3]
    my_function(1, *lst)

`fun()` still takes three arguments, but we only pass one argument directly, and then use `*lst` to unpack the remaining arguments from our list.

> Note that the total number of values passed to the function must still be the same as the number of positional arguments in the function definition!
