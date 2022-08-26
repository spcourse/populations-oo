## BONUS 1: Refactor

Make a copy of your previous file and call it `better.py`

### Goal
The design that you wound up with following our steps is far from perfect. When you're writing object-oriented code you can always add abstractions and make the design nicer, more reusable, simpler, more readable, etc.. Have a look at the design and see what could be improved.

To help you on your way have a look at the way new creatures are created. You probably have some duplicate code providing random locations. This could be made easier, by making the creatures themselves responsible for their random location. In that case, you don't have to provide a location when you create a new fox or rabbit. This way you can avoid some repeated code in the `__init__` of the `Experiment` class.

This is just an example, but there are many other ways to improve the design.

### Specification

* Improve the design of your code.

* Motivate the changes you made in a file called `better.txt` (`.md` or `.pdf` are also fine).

* If you made changes to the class structure, create a UML diagram `better-uml.png`. You can hand draw it and take a photo if you want.

## BONUS 2: Hungry bunnies

Make a copy of your previous file and call it `hungry-bunnies.py`.

### Goal

Having a hard cap on the number of rabbits is a very artificial solution. Now, the experiment is never 100% realistic (and that's often also not what you'd want), but it's not difficult to come up with a slightly more elegant solution. The reason foxes don't need a cap is that they have a limited food source. We can do the same for the rabbits.

### Specification

* Create a food source for the rabbits. (This can be anything: grass, carrots, Easter eggs, ...). The only requirement is that the source has to be limited, but renewable (e.g., grass that slowly grows back).

* Create a UML diagram for this experiment `experiment2-uml.png`. You can hand draw it and take a photo if you want.

* You would expect that the population stays stable for a much wider range of birth rates with this adaptation. Try to see if this is the case and document your findings in the comments.

* Feel free to change the class structure as much as you need. Try to generalize using inheritance as much as possible/makes sense.

## BONUS 3: Go nuts

Make a copy of your previous file and call it `nuts.py`.

### Specification

* Be creative: add an interesting new element to the simulation and see how it changes the dynamics.
0
