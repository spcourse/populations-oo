## Phase 9: Controlling Growth

Before you continue, **make a copy of your previous file and call it `phase9.py`**. Make sure to **continue editing in this new file**. It is important to keep the previous file as is. For this module, you'll have to submit all the stages separately.

### Goal

Ultimately, we would like to be able to use our model to run a whole suite of experiments. In this phase we will work on making that a possibility, by addressing a couple of issues.

One of these issues is the model has potential for exponential population growth. In our model, reproduction is an exponential process. If more rabbits reproduce than the foxes  can eat, the number rabbits will quickly increase and your program will become unresponsive. The easiest way to deal with that, for now, is by putting a cap on the total number of creatures.

We would like to be able to use our model to run a whole suite of experiments. However, currently, changing the rate at which creatures reproduce involves going into the code, changing a parameter in the creatures' `__init__`, and then running the code again. We will resolve this by adding arguments to the `__init__` of the `Experiment`, `Rabbit`, and `Fox` classes that can be used to change the birthrate of rabbits and foxes.

Another issue is the visualization. If we would like to do multiple experiments in quick succession showing the visualization would slow down our process. This can be solved by adding a boolean attribute `visualize` to the `Experiment` class. When it is `True` we display our visualization, but by default we will set this value to `False`.

Our last addition to the `Experiment` class will be a function that can be used to determine the number of `Rabbit` and `Fox` instances that are currently present in the `Experiment`'s `creatures` list. We will use this to evaluate the results of our experiments.

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
  * *modify* the call to the method `setup_plot()` such that it is only done when `visualize` is set to `True`
* *modify* the methods `add_rabbits()` and `add_foxes()`. They should only add creatures as long as there are fewer creatures in the list `creatures` than `max_creatures`. Additionally, since we added `birthrate` to the `__init__` of our creatuers, adjust the code that creates `Rabbit` and `Fox` instances such that it uses `birthrate_rabbits` and `birthrate_foxes` respectively.
* *modify* the method `run()`. It should only call the method `draw()` when `visualize` is set to `True`
* **add** the method `count_creatures()`. The method should return two values as a tuple; the first being the number of `Rabbit` instances in `self.creatures`, the second the number of `Fox` instances.

### Test
