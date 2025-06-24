def set_all_seeds(generate=False):
    import random
    import numpy as np
    import tensorflow as tf
    if generate:
        seed = random.randint(0, 2**32 - 1)
    else: 
        seed = 42
    np.random.seed(seed)
    random.seed(seed)
    tf.random.set_seed(seed)
    return seed
