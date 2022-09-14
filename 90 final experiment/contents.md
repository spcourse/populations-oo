## Experiment 1: Stable population

Make a copy of your previous file and call it `experiment1.py`. Make sure to continue editing in this new file. It is important to keep the previous file as is. For this module, you'll have to submit all the stages separately.

### Goal

Let's do a first real experiment. You're going to track the size of both the populations over time (iterations), like in the example below:

![](phase9.gif){: width="80%"}

As you can see here, the population of rabbits is not stable. The rabbits die out at around iteration 100. Your goal is to set the birth rate of foxes to 0.05 and find a birth rate of rabbits that makes the population relatively stable. I.e., the rabbits don't die out, but they also don't overpopulate the system.

Since there is chance involved and this is a highly chaotic system, you can never guarantee an outcome a 100%, so let's define stable as follows: For at least half the experiments, there are between 10 and 50 rabbits in the system after 200 iterations. 

### Setup

You will still need to modify the classes to be able to run this experiment, but we're not going to spell out how to do it. It's up to your design now.

One of the things to account for is the potential for exponential population growth. Since reproduction is an exponential process, if there are too many rabbits for the foxes to keep up with, they will overrun the system and their numbers will explode. The easiest way to deal with that, for now, is by putting a cap on the total number of rabbits. So we don't ever allow more than 100 rabbits to exist at the same time. (Putting a cap on the foxes is less important as they will only be able to grow in numbers when there are enough rabbits to eat. So capping rabbits automatically caps the number of foxes.)

We also want to have a timeline plot that monitors the number of rabbits and foxes in the system. Like in the example above.

### Specification

So to run the experiment you have to change the following:

* Add a way to set a maximum amount of rabbits. Make sure that, once that number is reached, the reproduction of rabbits is temporarily blocked.
* Create a second subplot that shows a timeline of the rabbits and foxes. You can create a second subplot like so:

        self.fig, (self.ax1, self.ax2) = plt.subplots(2)

    You can then plot using the `ax2` like this:

        self.ax2.plot(iterations_list, fox_history, color='red')

    Where for `iterations_list` and `fox_history` you have to fill in your own data.

    Don't forget to clear the plot in the same way you clear the plot of `ax1`:

        self.ax2.cla()

    These two changes might require some refactoring of your code and/or additional methods and attributes. It's up to you to decide how to implement this. But you might, at least, want to have an additional method that allows you to count creatures of a specific type in the experiment.
* Draw a new UML diagram of your update and save this as `experiment1-uml.png`. You can hand draw it and take a photo if you want.
    * Make sure the UML diagram contains *all* attributes and methods of each class.
    * Clearly highlight your modifications concerning the UML of the previous phase.
* Run the experiment (a decent number of times). What seems to be a good growth rate for the rabbits?
