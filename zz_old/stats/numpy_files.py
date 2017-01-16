import numpy as np
import pandas
t = np.linspace(-6, 6, 20) # linear space from -6 to +6 (radians) with 20 steps.
sin_t = np.sin(t)
cos_t = np.cos(t)
print(sin_t)
my_df = pandas.DataFrame({'t': t, 'sin': sin_t, 'cos': cos_t})
print(my_df)
# note order is different
