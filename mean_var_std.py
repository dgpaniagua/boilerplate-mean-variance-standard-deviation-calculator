import numpy as np

def calculate(mlist):
    
    if len(mlist) < 9:
      raise ValueError("List must contain nine numbers.")
    
    matrix = np.array([[mlist[0],mlist[1],mlist[2]],[mlist[3],mlist[4],mlist[5]],[mlist[6],mlist[7],mlist[8]]])

    mean_ax1 = matrix.mean(axis = 0).tolist()
    mean_ax2 = matrix.mean(axis = 1).tolist()
    mean_elem = matrix.mean()

    var_ax1 = matrix.var(axis = 0).tolist()
    var_ax2 = matrix.var(axis = 1).tolist()
    var_elem = matrix.var()

    std_ax1 = matrix.std(axis = 0).tolist()
    std_ax2 = matrix.std(axis = 1).tolist()
    std_elem = matrix.std()

    max_ax1 = matrix.max(axis = 0).tolist()
    max_ax2 = matrix.max(axis = 1).tolist()
    max_elem = matrix.max()
    
    min_ax1 = matrix.min(axis = 0).tolist()
    min_ax2 = matrix.min(axis = 1).tolist()
    min_elem = matrix.min()

    sum_ax1 = matrix.sum(axis = 0).tolist()
    sum_ax2 = matrix.sum(axis = 1).tolist()
    sum_elem = matrix.sum()

    calculations = {
      "mean": [mean_ax1, mean_ax2, mean_elem],
      "variance": [var_ax1, var_ax2, var_elem],
      "standard deviation": [std_ax1, std_ax2, std_elem],
      "max": [max_ax1, max_ax2, max_elem],
      "min": [min_ax1, min_ax2, min_elem],
      "sum": [sum_ax1, sum_ax2, sum_elem]
    }

    return calculations