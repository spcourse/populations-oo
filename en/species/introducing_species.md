# Species and interaction

## Rabbits

Now that we've created the basis for our simulation, we can start adding details and interactions. We'll start with implementing our rabbits. Start by downloading [`rabbit.py`](/for_students/rabbit.py). There are a couple of elements in `rabbit.py` that are new, but we'll explain them after a little experiment. Add a line to the top of your `main.py`: `from rabbit import Rabbit`. Now, instead of adding `Walker`s, add a couple of `Rabbit`s and run your code.

You will see that not a lot has changed; the dots on your screen act in the exact same manner they did before, except that their color is now blue. Now, take a look at the contents of `rabbit.py`. The class `Rabbit` is created in the following fashion:

    class Rabbit(Walker):

This is called _inheritance_. The newly-made class `Rabbit` "inherits" all methods and attributes that have been defined for the class `Walker`. Simply put, this means that even though we didn't explicitly define the `move()` and `draw()` methods for `Rabbit`, the versions of these functions we wrote for the `Walker` class are used.

In OOP, the class that is inherited from is called either the _parent class_, the _super class_, or the _base class_. In our case this parent/super class is `Walker`. The class that inherits is called the child class, or the derived class. Inheritance in Python follows the following simple rules:

- The child class inherits all methods and attributes from the parent class
- The child class can _overwrite_ all methods and attributes it got from the parent by redefining them (under the same name)

In our `Rabbit` class, this second rule is examplified as well; the `__init__()` method for `Rabbit` _overwrites_ the `__init__()` method in `Walker`, such that it can change the way the attribute `color` is set.

The `__init__()` of our `Rabbit` class also shows a line of code with an unfamiliar command: `super()`. This command enables you to get the parent/super class of the class it was called in. In our case, this is the `Walker` class. Thus, on this line, the `__init__()` of the `Walker` class is called, which saves us from having to repeat the code where the position, angle, and speed are set.

Rabbits move erratically, and to replicate this movement in our simulation, we will randomly change the angle of the rabbit. Define a method named `move()` for your `Rabbit` class. This method should overwrite the method `move()` that was defined in `Walker`. With a probability of 0.05, your code should change the angle to a new random value between zero and $$2\pi$$. If the rabbit does not change it's angle, it should call `super().move()`, such that it moves as if it is a walker. If the rabbit does change it's angle, it should not move that step.

If done correctly, you can now see your `Rabbit`s randomly change their angle every so often.

## Foxes

We will now do the same for foxes. Create a file named fox.py, import the `Walker` class and create a class named `Fox` inheriting from `Walker`. Overwrite the `__init__()` and set the color for foxes to `'red'`.

Check your class by importing it in `main.py` and adding some foxes to your simulation. You should now see some red dots moving around, acting as normal walkers.

Foxes move very smoothly through the landscape, and to simulate that we will slightly alter their `move()` method. Overwrite the `move()` method, call `super().move()` and change the angle of the fox using [`np.random.normal`](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.normal.html) to slightly change the `angle` of the fox with a standard deviation of 0.2. Foxes _can_ move and change their angle in the same step.

If done correctly, you will now see your `Fox`es move around the simulation while making smooth turns.

## Interaction

Our simulation is of course not complete without interaction between different instances. The Lotka-Volterra equations describe the change in the number of prey and the number of predators using based on a very basic set of rules:

1. The prey always have ample food
2. The predator population is entirely dependant on the prey population
3. The rate of change in populations is proportional to its size
4. The environment does not change and species do not adapt
5. Predators have limitless appetite.

Using these rules, we will define interactions between species.
