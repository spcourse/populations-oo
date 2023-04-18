## Experiment: Population dynamics

### Goal

![](phase9.gif){: width="80%"}

The experiment above was configured with a birth rate of `0.15` for both rabbits and foxes. In the line-graph below the simulation the number of rabbits and foxes are tracked as the simulation progresses. As you can see, the population of rabbits is not stable. All of the rabbits are devoured by the foxes around iteration 100. We would like to run a set of experiments and find out what the effect of different combinations of birthrates is on the population of both rabbits and foxes.

Since our simulation is probabilistic and highly chaotic, we can not guarantee that the outcome of a single run is a good representation of the actual dynamics of the simulation. To get a good overview of the outcome of our experiments we will have to run each configuration of input parameters many times and analyze the results.

In this phase of our experimentation pipeline we will write the code that runs experiments with varying input parameters multiple times. More specifically, we will run the simulation with different combinations for the birthrate of rabbits and foxes. The generated results for each experiment are then written to several `csv`-files in a `data/` folder for future analysis. Each `csv`-file contains the outcome of a multitude of runs of experiments done with the same input parameters.

### Setup

First, we will write code that can run an experiment with a specific configuration multiple times and record the results to a `csv`-file. We have provided you with some code that should help you in this process which you can [download here](experiment.py).

The code provided imports the `Experiment` class from your final implementation (`phase9.py`) and provides you with a dictionary named `experiment_kwargs` defining the default set of parameters that we will use for our experiments. We've also defined two functions for you that will make it a bit easier to collect and store your data.

`generate_experiment_name()` is a function that can be used to generate filenames for your experiments. By using this function to name of the `csv`-file, the filename will be more descriptive, and manually finding data for experiments done with a specific configuration will be easier. The function accepts a single argument, which should be a dictionary formatted like `experiment_kwargs`.

`export_result_to_csv()` is the function you will use to store the results of your experiments. It accepts three arguments; the location where the data should be stored, the configuration of the experiments, and the results of those experiments.

### Specification

**First, repeat one experiment configuration `N` times**

Write code that runs `N` experiments with the given experiment configurations in `experiment_kwargs`. `results` should be filled with tuples, where every tuple indicates the number of rabbits and foxes at the end of an experiment. You can use `Experiment`'s `count_creatures()` method to get each tuple.

To test your code, try a lower value for `N` first, and look at the generated `csv`-file. Does it contain the values you expected?

**Then, repeat many experiment configurations `N` times**

Modify your code to run experiments with a range of configurations of `birthrate` for rabbits and foxes. Your code should run the experiment with each combination of birthrates for rabbits and foxes from 0.05 up to and including 0.5, incrementing with steps of 0.05. In essence, you are implementing a grid search.

To do this, you can use a loop to iterate through the different values of birthrate for rabbits and foxes. For each combination of birthrates, you should run `N` experiments and export the results of each individual configuration using `export_result_to_csv()`.

To test your code, try a lower value for `N` first again (something like `N=3`), and look at the `data` folder and the `csv`-files therein. If done properly, after some time, you should end up with 100 different `csv`-files containing `N` results each. Check the `csv`-files with low values for the birthrates: is the final number of rabbits and/or foxes in experiments sometimes 0? For experiments with high birthrates: is the final number of rabbits and/or foxes close to the value set for `max_creatures`?

Finally, run your code with `N=100`. You should end up with 100 `csv`-files containing 100 data rows and a header each. This could take around 20 to 30 minutes.
