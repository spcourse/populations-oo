# Predator-prey model

One of the classic examples of complex systems is the predator-prey model. A famous mathematical description of the interactions in the predator-prey model are the [Lotka-Volterra equations](https://en.wikipedia.org/wiki/Lotka–Volterra_equations):

$$
\frac{dx}{dt} &= \alpha x - \beta x y, \\
\frac{dy}{dt} &= \delta x y - \gamma y
$$

Where $x$ is the number of prey, $y$ the number of predators, $t$ time, and the other variables describe the interactions between species. The population of a species is allowed to be a floating point number

The math used in these equations is very simple, but resulting models can have very unique complex properties and variants have been successfully used to describe various real-life populations. One of the problems with the model lies in using it to describe small scale dynamics; having a quarter of a rabbit interact with two thirds of a fox is unrealistic.

In this module, we'll create a very basic predator-prey model that simulates a field with rabbits and foxes. We will visualize the system, such that we have direct visual feedback about the functioning of our code, and such that we can see the consequences of the behavioral rules that we add. This simulation will be programmed using the OOP paradigm, which will enable us to provide a very generic structure of an animal, onto which we can add properties that define the behavior of our predators and our prey.

## Field and Walker classes

Download [field.py](/for_students/field.py). We'll be setting up the field in which the rabbits and the foxes will move around. The `Field` class has a couple of properties and functions which we will first explain:

- `width`: This is the width of the field.
- `height`: This is the height of the field.
- `creatures`: This list will keep track of all creatures that are currently alive in the simulation
- `fig`, `ax1`, `ax2`: These variables will be needed to keep track of the plots we will make later.
- `add_creatures()`: Through this function we will add more creatures to the simulation.
- `draw()`: This function will draw our field, and all creatures on it. We will also add some fancy statistics to this function later.
- `step()`: This function can be used to take a single timestep in the simulation.
- `simulate()`: This function will take an argument through which we can take several timesteps in the simulation.

You will see that all functions are defined, but that most only have `pass` in them. This is simply a trick to make Python do nothing (while preventing errors), and it merely serves as a placeholder for the code we will implement later. We would create an empty field of equal width and height (100) as follows:

    meadow = Field(100, 100)

Now download [walker.py](/for_students/walker.py). In this file, we will be implementing our first walking creatures. `Walker` is a class that we will use as the basis for all our walking creatures, and all creatures have at least the following properties: a position (defined by an x and a y coordinate), a speed, and an angle. We expect to create a creature at x = 15 and y = 10, speed = 1, and angle = 0 as follows:

    creature = Walker(15, 10, 1, 0)

Create a third file `main.py`. This file will serve as the main point from which we will start our program. For now, you can keep this one empty.

## Implementing both `draw()` functions

To get our first good look at what our creatures look like, we will start with implementing the `draw()` function of both the `Field` and `Walker` classes.

We'll start off with `Field.draw()`. This function should draw the whole field with all its contents. A structure has been provided in which a plot window is created where two graphs can be drawn next to eachother horizontally. The left graph can be accessed (and drawn on) trough `ax1`, while the right plot can be acessed through `ax2`. For now, we will only need `ax1`.

To test our future code we will, for now, hardcode two creatures into the list of creatures of a field. Copy and paste the following code into `main.py`:

    from field import Field
    from walker import Walker

    simulation_field = Field(100, 100)

    creature1 = Walker(15, 10, 0, 1)
    creature2 = Walker(95, 10, 0, 1)

    simulation_field.creatures.append(creature1)
    simulation_field.creatures.append(creature2)

    simulation_field.draw()

> The imports in the code above are so-called relative imports. Python will search for files named 'field.py' and `walker.py` locally, and by using the `from` keyword we only import the classes `Field` and `Walker`.

Running this code using `python main.py` will very briefly open a plot-window. To keep it open for longer, you can lengthen the `plt.pause()` in `field.py` to something like 5 seconds.

As you can see, the code already draws one blue dot exactly in the middle of the field. It is your job to change this code to draw dots for every creature in the list of creatures for this specific `Field`.

Navigate to the `draw()` function in `walker.py` and replace `pass` with `ax.plot()` in such a way that it would plot a dot on the location of the walker (use `self.x` and `self.y`) using the color from `self.color`.

If done correctly, we can now replace the line that plots a blue dot in `field.py` with `self.creatures[0].draw(self.ax1)` to make the first walker in the list draw itself to the left graph.

Create a for-loop that calls the `draw()` function of all objects in the list `self.creatures`.

You should end up with two _black_ walkers positioned on (15, 10) and (95, 10).

## Simulating steps

Currently, we are visualizing the initial state of the simulation. To actually make the simulation progress we will have to implement the methods `Field.step()` and `Field.simulate()`. First, implement `Field.simulate()`. This method gets an argument named `iterations`, which indicates how many "steps" should be made in the simulation. Use a `for`-loop to iteratively call the functions `step()` and `draw()`, such that for every step made in the simulation, the visualisation is redrawn. _Don't forget to shorten `plt.pause()` back to 0.01 seconds!_

You can test your code by replacing `simulation_field.draw()` in your `main.py` with `simulation_field.simulate(100)` and by adding a `print` with the iteration  number to `Field.simulate()`. If done correctly, you should see the exact same as before; a graph that shows two _black_ walkers positioned on (15, 10) and (95, 10), which opens for about a second while the numbers 0 to 100 are printed in your terminal.

## Moving around

Of course two dots just sitting there on the screen isn't that exciting. We will quickly "move on" to making the dots move. To do this, we'll be changing the method `Walker.move()`. Each `Walker` already has some properties that can help us calculate the new position after one timestep. We can use it's `angle` and `speed` to calculate the change in `x` and `y` with the following formulae:

$$ \delta x = cos(angle) * speed $$

$$ \delta y = sin(angle) * speed $$

Change `Walker.move()` such that it changes `pos_x` and `pos_y` using the formulae above.

Now, implement `Field.step()`. This function should loop over all creatures in the field, and call their `move()` function.

If done correctly, your code in `main.py` should now show your walkers slowly moving off the screen to the right!

## Edge cases

Unfortunately, this is behavior is not entirely desired. Ideally, we would want to keep our rabbits and foxes within the field.

TODO FIND PROPER SOLUTION FOR CURRENT HARDCODE WITHOUT ADDING TOO MANY PROPERTIES

If done correctly, your walkers should no longer leave the screen, but bounce around within the boundaries of our `Field`.

## Streamlining adding creatures

At the moment, creatures are added manually through manipulating the list of `creatures` saved in the `Field` instance. As we start adding more and more creatures, the need for a general function that can do this arrises. As you might have noticed, `Field.add_creatures()` was already defined. This function should accept three arguments: `Creature_type`, `number`, and `speed`. `Creature_type` is the class of which we want to create creatures, which in our case is a `Walker`. `number` is the amount of creatures that we want to create. `speed` is the speed that should be given to the creatures that are created. Other attributed of the created creatures should be randomized.

> Angles in our simulation are defined as radians, $angle=0$ points to the right, $angle=\frac{1}{2}\pi$ points up, $angle=\pi$ points to the left, and $angle=1\frac{1}{2}\pi$ points down. Your random angle should be generated between $0$ and $2\pi$.

Create a loop that creates `number` creatures of type `Creature_type` with a random starting position within the field, a random angle, and a given `speed`. Each of these creatures should be appended to the list of `creatures`. **Hint**: creating a single creature of type `Creature_type` in the middle of the field with an angle of 0 and speed of 1 can be done as follows:

    creature = Creature_type(50, 50, 0, 1)

After you have done this, you can replace the two manually created creatures in  `main.py` with the following code, and test:

    simulation_field.add_creatures(Walker, 2, 1)

If you now run your code, you should see that 2 creatures get randomly placed in our `Field` and start walking in a random direction.
