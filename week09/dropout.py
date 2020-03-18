# coding:utf-8
import numpy as np

def dropout(x,level):
    if level < 0 or level >= 1 :
        raise ValueError('Dropout level must be in interval [0, [1.')
    retain_prob = 1. - level

    random_tensor = np.random.binomial(n=1, p = retain_prob, size=x.shape)
    print(random_tensor)

    x *= random_tensor

    print(x)

    return x

x = np.asarray([1,2,3,4,5,6,7,8,9,10], dtype=np.float32)
dropout(x, 0.4)

#[ 0.  0.  3.  0.  5.  6.  7.  8.  0. 10.]
#[ 0.  0.  3.  4.  5.  6.  7.  0.  9. 10.]
#[0. 2. 3. 4. 0. 0. 0. 0. 9. 0.]