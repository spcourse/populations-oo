## Phase 5: Creatures

Before you continue, **make a copy of your previous file and call it `phase5.py`**. Make sure to **continue editing in this _new_ file**.

### Goal
Before we introduce additional complexity in the next phases, we should first improve the code to make it more elegant and organized. As you might have realized by now, in writing the code for the previous phase we generated a lot of duplicate code. Both the `Fox` and `Rabbit` classes share a lot of similarities. Not that surprising, given that a considerable portion of their code relates to their shared behavior of moving within our simulated environment.

So let's create a new abstraction: You're going to create a "superclass" called `Creature`. This class will contain the code for moving around that both `Fox` and `Rabbit` will inherit.

The UML will look like this:

![](oo-phase5.png){: width="100%"}

Notice that class inheritance is indicated by arrows (⇽). So `Fox` and `Rabbit` both inherit from `Creature`. You can also see that `Fox` and `Rabbit` are reduced a lot as most of their code will now reside in `Creature`.

### Specification

Create a new class called `Creature`. For this class:

* **add** method `__init__(pos_x, pos_y, angle)`.
  * **add** attributes `pos_x`, `pos_y`.
  * **add** attribute `angle`.
  * **add** attribute `speed`. Creatures get the default speed $$0.01$$.
  * **add** attribute `color`. Creatures get the default color `'black'`.
* **add** method `step()`. This method should only define the step based on the current angle, position and speed. It should not define the change of angle as that part is defined in the `step()` methods of the subclasses `Rabbit` and `Fox`

> Think about why it is wise to set the default color of creatures to something unique!

Modify the `Fox` class. You can remove a lot of code and inherit it from `Creature`.

* *modify* class `Fox`. The class definition should now be changed to inherit from `Creature`.
* *modify* method `__init__(pos_x, pos_y, angle)` to call the `__init__()` method from the superclass (using `super()`). After this, you should still specify `speed` and `color` in this class as those properties are particular to `Fox`.
* *modify* method `step()` to call the same method from the superclass. Only the modification of the angle should remain in this class (as the logic for changing angles is particular to the `Fox` class).

Modify class `Rabbit` in the same way as `Fox`.

> If you want, you can now also look into other ways to improve the design of your code!

### Test

This was only a design change. If you did it correctly, it shouldn't have changed any of the behavior of the experiment. Test this by using some of the test cases from the previous phases. Pay special attention if the movement behavior of the fox is still independent of that of the rabbit. Can you, for example, change the speed of the foxes without changing the speed of the rabbits?
