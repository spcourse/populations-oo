## Phase 9: Controlling Growth

Before you continue, **make a copy of your previous file and call it `phase9.py`**. Make sure to **continue editing in this new file**. It is important to keep the previous file as is. For this module, you'll have to submit all the stages separately.

### Goal

Finally, we would like to be able to use our model to run a whole suite of experiments using several experiment parameters. In this phase we will work on making that possible, by addressing a couple of issues.

One of these issues is the model has potential for exponential population growth. In our model, reproduction is an exponential process. If more rabbits reproduce than the foxes  can eat, the number rabbits will quickly increase and your program will become unresponsive. The easiest way to deal with that, for now, is by putting a cap on the total number of creatures.

Currently, changing the rate at which creatures reproduce involves going into the code, changing a parameter in the creatures' `__init__`, and then running the code again. This effectively makes it impossible to run a large amount of automated experiments. We will resolve this by adding arguments to the `__init__` of the `Experiment`, `Rabbit`, and `Fox` classes that can be used to change the birthrate of rabbits and foxes.

> There are more parameters in our implementation that are not easily changeable, like `speed`, `color`, the amount of `hunger` a fox can have before it dies, and some others. Even though it would probably be better code design (increasing abstraction), we have chosen not to include these parameters in the initialization of the `Experiment` class. Similarly, you might have noticed the code duplication in the methods `add_rabbits()` and `add_foxes()`. Alternative ways of implementing the experiment parameters or the aforementioned methods would make the code more complex, and therefore more difficult to implement. We have opted for the easier implementation. _If you are up to the challenge, you are allowed improve the implementation of these features, as long as the code functions in the same way._

After running an experiment, we are interested in the number of rabbits and foxes remaining. We need to write a function that can be used to determine the number of `Rabbit` and `Fox` instances that are currently present in the `Experiment`'s `creatures` list. We will use this to evaluate the end results of our experiments.

When we are doing a lot of experiments with different parameters, it is probably not necessary to view the visualization every single time. Visualizing the simulation is relatively slow, and ultimately we are only interested in the result of the simulation. For this reason, our last addition to the `Experiment` class is a boolean attribute `visualize`. When it is set to `True` we display our visualization, but by default we will set this value to `False`.

The UML below shows the required modifications:

![](oo-phase9.png){: width="100%"}

### Specification

Modify the class `Fox`:

* *modify* `__init__` to accept the new parameter `birthrate` and use it to set the value for the attribute `birthrate`.

Modify the class `Rabbit`:

* *modify* `__init__` to accept the new parameter `birthrate` and use it to set the value for the attribute `birthrate`.

Modify the class `Experiment`:

* *modify* `__init__` to accept four new parameters: `birthrate_rabbits`, `birthrate_foxes`, `max_creatures`, and `visualize`
  * All four parameters should be stored as attributes.
  * `max_creatures` should get a default value of `50` in the function header
  * `visualize` should get a default value of `False` in the function header
* *modify* `__init__` such that the call to the method `setup_plot()` such that it is only done when `visualize` is set to `True`
* *modify* the methods `add_rabbits()` and `add_foxes()`. They should only add creatures as long as there are fewer creatures in the list `creatures` than `max_creatures`. Additionally, since we added `birthrate` to the `__init__` of our creatuers, adjust the code that creates `Rabbit` and `Fox` instances such that it uses `birthrate_rabbits` and `birthrate_foxes` respectively.
* *modify* the method `run()`. It should only call the method `draw()` when `visualize` is set to `True`
* **add** the method `count_creatures()`. The method should return two values as a tuple; the first being the number of `Rabbit` instances in `self.creatures`, the second the number of `Fox` instances.

### Test

Run some tests to determine whether the newly added features function as intended.

* Is the visualization disabled by default?
* Can you enable the visualization by giving the experiment the argument `visualize=True`?
* After running an experiment, can you use the `count_creatures()` method to determine the number of rabbits and foxes remaining? Do these numbers seem correct?
* Test different values for `birthrate_rabbits` and `birthrate_foxes`.
* When you set a high birthrate for rabbits or foxes, do their numbers not grow beyond the value you set for `max_creatures`?
