class MovingAverage:
  """
  This class calculates the moving average of a list of numbers.

  Attributes:
      window_size: The number of elements to include in the moving average calculation.
      data: A list to store the data points.
  """

  def __init__(self, window_size):
    """
    Initializes the MovingAverage class with a specified window size.

    Args:
      window_size: The number of elements to include in the moving average calculation.
    """
    self.window_size = window_size
    self.data = []

  def update(self, value):
    """
    Updates the moving average with a new data point.

    Args:
      value: The new data point to be added to the moving average calculation.
    """
    self.data.append(value)
    if len(self.data) > self.window_size:
      self.data = self.data[-self.window_size:]
        

  def get_average(self):
    """
    Calculates and returns the current moving average.

    Returns:
      The current moving average, or None if there are not enough data points yet.
    """
    if len(self.data) < self.window_size:
      return None
    return sum(self.data) / len(self.data)

  def print_data(self):
    """
    Print the data array.

    Returns:
      None
    """
    print(self.data)

import random
def gen_temps(n, low, high):
    
    temp_range = range(low, high)
    amount = n
    temperatures = [0] * amount
    for i in range(0, amount):
        temperatures[i] = random.choice(temp_range)
    return temperatures

m = 10
temperatures = gen_temps(10, 0, m + 1)#high inclusive
print(temperatures)

# Example usage
ma = MovingAverage(window_size = 3)

for temp in temperatures:
  ma.update(temp)
  average = ma.get_average()
  if average is not None:
    print("Moving average after adding {0}: {1}".format(temp, average))
    ma.print_data()