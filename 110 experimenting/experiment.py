from phase9 import Experiment

import csv
import os

def generate_experiment_name(exp_kwargs):
    """
    Generates a filename for an experiment in the following format:
        result_<first-keyword-value>_<second-keyword-value>...

    The argument `exp_kwargs` should be a dictionary containing keywords for the
    experiment parameters and their values.
    """
    return 'result_' + '_'.join(f'{round(value, 2)}' for value in exp_kwargs.values()) + '.csv'

def export_result_to_csv(experiment_path, exp_kwargs, results):
    """
    Exports the `results` of an experiment that was performed using `exp_kwargs`
    as experiment parameters to a file in the location described by `experiment_path`.

    The generated csv has a header and each row thereafter describes the
    experiment parameters as well as the number number of rabbits and foxes at
    the end of an experiment.
    """
    exp_params = tuple(exp_kwargs.keys())
    exp_param_values = tuple(exp_kwargs.values())

    with open(experiment_path, 'w') as output_file:
        csv_writer = csv.writer(output_file)

        # write header
        csv_writer.writerow(exp_params + ('Rabbits', 'Foxes'))

        # repeat experiment parameters and add the outcome for each experiment
        for (rabbits, foxes) in results:
            csv_writer.writerow(exp_param_values + (rabbits, foxes))


if __name__ == '__main__':
    # create the folder data if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    N = 100

    experiment_kwargs = {
        'iterations': 200,
        'number_of_rabbits': 10,
        'number_of_foxes': 3,
        'birthrate_rabbits': 0.15,
        'birthrate_foxes': 0.15,
        'max_creatures': 50
    }

    results = []

    ### YOUR SOLUTION HERE

    experiment_name = generate_experiment_name(experiment_kwargs)
    export_result_to_csv(f'data/{experiment_name}', experiment_kwargs, results)
