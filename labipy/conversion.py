import numpy as np

def conversion(labi):
    
    arr_labi = np.array(labi)
    arr_converted = np.zeros((2*arr_labi.shape[0]+1)*(arr_labi.shape[1]+1)).reshape((2*arr_labi.shape[0]+1), (arr_labi.shape[1]+1))
    for i in range(arr_labi.shape[0]):
        for j in range(arr_labi.shape[1]):
            if arr_labi[i][j] == 1:
                arr_converted[2*i][j] = 1
                arr_converted[2*i + 1][j] = 1
                arr_converted[2*i + 1][j + 1] = 1
                arr_converted[2*i + 2][j] = 1
    return arr_converted