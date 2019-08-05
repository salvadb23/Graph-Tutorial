def knapsack(C, items, n):
    ''' A  method to determine the maximum value of the items included in the knapsack 
  without exceeding the capacity  C

      Parameters: 
      C= 50
      items = (("boot", 10, 60),
           ("tent", 20, 100),
           ("water", 30, 120),
           ("first aid", 15, 70))
      Returns: max value
  '''


def print_knapsack_solution(items, capacity, result):
    print("For this input: {}, \n Capacity of knapsack: {}\n The value of the optimal solution to the knapsack problem is V={}".format(
        items, capacity, result))


items = (("boot", 10, 60),
         ("tent", 20, 100),
         ("water", 30, 120),
         ("first aid", 15, 70))
result = knapsack(50, items, len(items))
print('')
