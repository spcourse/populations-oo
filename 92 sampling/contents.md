# Sampling

When you are conducting experiments with a computational model, it is important to understand how different input parameters can affect the output of your model. Often, changing the values of input parameters can cause unpredictable changes in the output.

## OFAT

A method that can be used to test how different input parameter values affect the output of your model is called "one factor at the time" (OFAT) testing. As the name suggests, OFAT involves changing one input parameter at a time and observing how the output changes in response. This output can help you identify which input parameters are important in your model, which affect the output most, and, by repeating each run with a specific configuration multiple times, how these parameters contribute to the variability in the output of your model.

However, OFAT testing has limitations. By changing only one factor at the time you do not take in to account potential interactions between different input parameters. Changing one input parameter might have a different effect depending on the value of another input parameter.

## Grid Sampling

A very similar approach is grid sampling, which involves testing all possible combinations of a large set of values, often uniformly spaced, for each individual input parameter. This approach can help you identify more complex relationships between input parameters and the output of your model, as well as identify potential interactions between different input parameters.

A big downside to this approach is that it can be very time consuming. Depending on the desired granularity of input values and the number of input parameters you might require a lot of samples. Increasing either of these factors changes the number of samples that need to be taken exponentially.

Overall, it is important to recognize that different input parameters can interact and affect the outcome of a model in unpredictable ways. It is best to test a large set of input parameter values to get a better understanding of how they affect the output of your model.
