# -*- coding: utf-8 -*-
"""Mock2_4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mZQF7OLPVvHZPsZefAhmJko4FBHvq_yr

Sure, here is the function called `perform_hypothesis_test` that takes two lists of numbers as input, representing two samples. The function performs a two sample t-test and returns the p-value using the `scipy.stats` module in Python:
"""

import scipy.stats as stats


def perform_hypothesis_test(sample_1, sample_2):
  """
  Performs a two sample t-test and returns the p-value.

  Args:
    sample_1: The first sample.
    sample_2: The second sample.

  Returns:
    The p-value of the t-test.
  """

  t_statistic, p_value = stats.ttest_ind(sample_1, sample_2)
  return p_value


def main():
  sample_1 = [1, 2, 3, 4, 5]
  sample_2 = [6, 7, 8, 9, 10]
  p_value = perform_hypothesis_test(sample_1, sample_2)
  print(p_value)


if __name__ == "__main__":
  main()

"""This function first imports the `scipy.stats` module. Then, it performs a two sample t-test on the two samples passed as input. The t-statistic and p-value of the t-test are then returned.

To run the function, you can save it as a Python file and then run it from the command line. For example, if you save the function as `perform_hypothesis_test.py`, you can run it by typing the following command into the command line:

```
python perform_hypothesis_test.py
```

This will print the p-value of the t-test.
"""