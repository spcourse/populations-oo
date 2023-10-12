## Phase 2: Rabbits

Before you continue, **make a copy of your previous file and call it `phase2.py`**. Make sure to **continue editing this _new_ file**.

### Goal

A single rabbit moving around is a bit boring, let's add some more. Like so:

![](phase2.gif){: width="60%"}

One of the key advantages of using classes is the ability to create multiple instances of a particular class. This means that we can introduce multiple rabbits into our system without the need to make substantial changes to the `Rabbit` class, and with only minor adjustments to the `Experiment` class.

After your changes the UML should look like this:

![](oo-phase2.png){: width="70%"}

The fact that `Experiment` can now contain any number of rabbits is indicated by the `*` near the `Rabbit` class on the aggregation line. Everything that is **bold** in the UML is new (and is up to you to implement). So here you'll have to add the method `add_rabbits(number_of_rabbits)`. Everything in _italic_ is not new, but you will have to modify it to make things work.

### Specification

For this phase you have to *modify* the class `Experiment` as follows:

* **add** method `add_rabbits(number_of_rabbits)` that creates a list of rabbits with random locations and angles and adds them to the attribute `rabbits`.
* *modify* `__init__(iterations, number_of_rabbits)` to accept the new parameter `number_of_rabbits`.
* *modify* attribute `rabbit` (one single instance of `Rabbit`) to `rabbits` (a `List`) and use `add_rabbits()` to create the correct number of `Rabbit` instances.

    **From here on the `Rabbit` objects will be created *inside* the `Experiment` object.** We don't have to do this in the main code anymore as we did in Phase 1.

* *modify* method `step()` to loop over all instances in `rabbits` and call their `step()` method.
* *modify* method `draw()` to draw *all* rabbits using a similar loop.

> Don't forget the `self` parameter when you define new methods!

The experiment should spawn 10 rabbits when called like this:

    my_experiment = Experiment(100, 10)
    my_experiment.run()

> Calling `self.ax1.scatter(...)` many times will make your code very slow with larger amounts of rabbits. Try to collect all the coordinates that need to be plotted first and call `self.ax1.scatter(...)` _only once_ to plot all the rabbits in one go.

### Test

Make sure your experiment works with 1 rabbit:

    my_experiment = Experiment(100, 1)
    my_experiment.run()

Make sure your experiment works with 100 rabbits:

    my_experiment = Experiment(100, 100)
    my_experiment.run()

And, with 0 rabbits:

    my_experiment = Experiment(100, 0)
    my_experiment.run()
