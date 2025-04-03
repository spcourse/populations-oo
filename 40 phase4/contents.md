## Phase 4: Foxes

Before you continue, **make a copy of your previous file and call it `phase4.py`**. Make sure to **continue editing in this _new_ file**.

### Goal

We are now going to introduce foxes into our experiment. For now, they will simply roam around without disturbing any rabbits. Just like rabbits, foxes have a position, angle, speed, and movement. However, their movements have distinct characteristics; they move faster and make more gradual turns. We'll distinguish foxes by giving them a red color. The new simulation will look like this:

![](phase4.gif){: width="60%"}

This will require a whole new class `Fox` as you can see in the UML:

![](oo-phase4.png){: width="70%"}

You see that the class `Experiment` can contain any number of instances of `Fox` (as indicated by the `*`).

### Specification

For the class `Fox`:

* **add** class `Fox`. For now, it has the same properties as the `Rabbit`, only the speed and color have different values.
* **add** method `__init__(pos_x, pos_y, angle)`.
  * **add** attributes `pos_x`, `pos_y`.
  * **add** attribute `angle`.
  * **add** attribute `speed`. The speed of the fox should be $$0.03$$ (faster than the rabbit).
  * **add** attribute `color`. Foxes get the color `'red'`.
* **add** method `step()`. The steps are the same as for `Rabbit` only the change of angle is less abrupt: the angle has a $$20\%$$ probability of changing by a random value between $$-\pi/4$$ and $$\pi/4$$ (i.e., between -45 and 45 degrees).

For the class `Experiment`:

* *change* attribute `rabbits` to `creatures`. This list will now contain both foxes and rabbits.
* *modify* `add_rabbits(number_of_rabbits)` to add the Rabbit instances to the list `creatures` instead of to `rabbits`.
* *modify* `step()` to use the list `creatures` in stead of `rabbits`.
* *modify* `draw()` to use the list `creatures` in stead of `rabbits`.
* **add** `add_foxes(number_of_foxes)` this should add foxes to the list of creatures.
* *modify* `__init__(iterations, number_of_rabbits, number_of_foxes)`. The method should now get an additional parameter for the number of foxes. And it should call the method `add_foxes()`.

The experiment should spawn 10 rabbits and 3 foxes when called like this:

    my_experiment = Experiment(100, 10, 3)
    my_experiment.run()

> Your code for `add_foxes()` will probably look very similar to the code in `add_rabbits()`. Can you think of a way to reduce duplicate code here? Don't make your change yet, but comment what you could do to improve your code! You can improve your design in phase 5.

### Test

Do the foxes seem to move faster than the rabbits?

Think about how you can test if everything works as expected. Test at least a few different configurations.

For example, an experiment without foxes:

    my_experiment = Experiment(100, 10, 0)
    my_experiment.run()

an experiment without rabbits:

    my_experiment = Experiment(100, 0,3)
    my_experiment.run()

an experiment without any creature:

    my_experiment = Experiment(100, 0, 0)
    my_experiment.run(100)

Change the parameters of the fox and see if you have the expected behavior. What happens when you make the angle of change of the foxes 0? What happens when you set their speed to 0? Is this what you would expect?


### Checkpy

Checkpy checks the class-structure. It doesn't check if it actually runs the experiment correctly.

    checkpy phase4
