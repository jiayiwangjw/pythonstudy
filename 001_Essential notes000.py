#1.1-collections

"""
001 返回LIST里的最大最小值
"""
minmax([8, 7, 2, 5, 1]) == (1, 8)

def minmax(L):
    assert hasattr(L, "__iter__")
    #
    # YOUR CODE HERE
    #
    xmax, xmin = max(L), min(L)
    return xmin, xmax


"""
002 移除LIST里的某个值
"""
remove_all([1, 2, 3, 2, 4, 8, 2], 2) == [1, 3, 4, 8]

def remove_all(L, x):
    assert type(L) is list and x is not None
    #
    # YOUR CODE HERE
    L = [i for i in L if i != x]
    return L


"""
003 从LIST返回一个字典DICT KEY为非0数的INDEX， VALUE为非0数的值
"""
x = [0.0, 0.87, 0.0, 0.0, 0.0, 0.32, 0.46, 0.0, 0.0, 0.10, 0.0, 0.0]
d['inds'] = [1, 5, 6, 9]
d['vals'] = [0.87, 0.32, 0.46, 0.10]

def compress_vector(x):
    assert type(x) is list
    d = {'inds': [], 'vals': []}
    #
    # YOUR CODE HERE
    for i, j in enumerate(x):
        if j != 0:
            d['inds'].append(i)
            d['vals'].append(j)
    return d
    
    
"""
004 将字典转换成LIST
"""
d = {}
d['inds'] = [0,   3,   7,   3,   3,   5, 1]
d['vals'] = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
x_true = [1.0, 7.0, 0.0, 11.0, 0.0, 6.0, 0.0, 3.0]
    
def decompress_vector(d, n=None):
    # Checks the input
    assert type(d) is dict and 'inds' in d and 'vals' in d, "Not a dictionary or missing keys"
    assert type(d['inds']) is list and type(d['vals']) is list, "Not a list"
    assert len(d['inds']) == len(d['vals']), "Length mismatch"
    
    # Determine length of the full vector
    i_max = max(d['inds']) if d['inds'] else -1
    if n is None:
        n = i_max+1
    else:
        assert n > i_max, "Bad value for full vector length"
        
    #
    # YOUR CODE HERE
    x = [0.0] * n
    for i, v in zip(d['inds'], d['vals']):  #[(0, 1.0), (3, 2.0), (7, 3.0), (3, 4.0), (3, 5.0), (5, 6.0), (1, 7.0)]
        x[i] += v
    return x    
    
