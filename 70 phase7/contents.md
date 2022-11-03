## Phase 7: Feeding foxes

Before you continue, **make a copy of your previous file and call it `phase7.py`**. Make sure to **continue editing in this new file**. It is important to keep the previous file as is. For this module, you'll have to submit all the stages separately.

### Goal

Now that the foxes can get hungry they'll have to be able to feed. The idea is that when a fox gets close enough to a rabbit he can eat it. The rabbit will then be removed from the experiment and the fox will not be hungry anymore. In the example below you see that when a red dot comes close to a blue dot, the blue dot disappears. As a result, the red dots stay longer in the experiment.

![](phase7.gif){: width="60%"}

The UML below shows the elements that we need to add. We need to be able to compute the *distance* between creatures and we need to have them *interact* when the distance is small enough. This requires modifications to all the classes. We add the `distance()` method to the `Creature` class as we need to be able to compute the distance between any type of creature, not only between foxes or rabbits. We add an `interact()` method to `Creature` as potentially any creature can interact with any other creature. However, for now, this remains empty. As we only really implement the more specialized `interact()` method of the `Fox` class. Here we define what happens when a fox interacts with another creature. (If the other creature is a rabbit, the fox eats it.)

![](oo-phase7.png){: width="100%"}

This design follows a design pattern that you see more often in multi-agent systems: the creatures are responsible for their own interactions. That is to say that the `Experiment` code only decides whether or not two agents (i.e., `Creature`s) interact at all. The code for *how* they interact, so what an agent does when it encounters another is part of the agent's class, not of the experiment. So the `Experiment` class checks if two `Creatures` are close enough (with the method `handle_interaction()`). When that is the case, the `Creature` defines how to interact, so in this case, if the one creature is a fox and the other creature a rabbit, the first should eat the latter (which is implemented by the `interact()` method in `Fox`).

As a consequence of this design, every `Creature` should have this `interact()` method, even if it doesn't do anything.

### Specification

Modify the class `Creature`:

* **add** method `distance(other)`. This should return the distance between the creature and another one.
* **add** method `interact(other)`. This method specifies what a creature should do when it is close enough to another creature. For now, nothing, so you can leave the method empty with `pass`.

Modify the class `Fox`:

* **add** method `interact(other)`. This method specifies what a fox should do when it is close enough to another creature: If the other creature is a rabbit, the fox is not hungry anymore (so `hunger` is set back to `0`) and the rabbit is killed. (You can use the `alive` flag of the rabbit to `False`, to kill the rabbit.)

    Tip: you can use `if type(other) == Rabbit:` to test if the other creature is a rabbit.

Modify the class `Experiment`:

* **add** attribute `interaction_distance`. This sets at which minimal distance two creatures can interact. A good distance is `0.05`.
* **add** method `handle_interaction()`. This method tests the distance between **every pair** of creatures. If the distance is lower than `interaction_distance`, it calls the `interact` from one creature with the other creature as the argument.

    You can use the following code for that:

        def handle_interaction(self):
            for creature1 in self.creatures:
                for creature2 in self.creatures:
                    if not creature1 is creature2 and creature1.distance(creature2) < self.interaction_distance:
                        creature1.interact(creature2)

    Note that this code tests for every pair of creatures if they are close enough. If so, the method `interact()` is called on one creature with the other as an argument. The condition `not creature1 is creature2` in the if-statement prevents the interaction of a creature with itself.

    The time complexity of this code is $$O(n^2)$$. That makes it the bottleneck of the simulation. If you want to simulate many creatures you would have to use fancier collision detection algorithms that have a lower time complexity, like [quadtrees](https://en.wikipedia.org/wiki/Quadtree). But don't do this now.

    A consequence of this algorithm is that for every pair of creatures, the interact method is called twice. If creature A interacts with creature B then the reverse is also the case. So if `interact()` is called on A with B as an argument, then interact will also be called on B with A as an argument. This is something to keep in consideration for later phases.

* *modify* method `step()` to call `handle_interaction()`.


### Test

Do the rabbits seem to disappear when they encounter a fox?

Try some test cases:

* When you have 100 foxes and 100 rabbits, how quickly do the rabbits disappear?
* Make the `interaction_distance` 0. Do all the rabbits remain?
* Make the `interaction_distance` 1. Do all the rabbits disappear instantly?
* There are two possible outcomes: (1) The foxes eat all the rabbits and then slowly starve. Or (2) the foxes die out before all the rabbits are eaten and the rabbits survive. The outcome depends partly on the initial amount of rabbits. Experiment with this: For example, given 20 initial rabbits, how many initial foxes do you minimally need to always wind up in situation 1?
