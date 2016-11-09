import pandas as pd
import numpy as np
frame=pd.DataFrame(np.random.randn(1000,5),columns=['a','b','c','d','e'])

print (frame['a'].corr(frame['b']))

print (frame.corr())



s = pd.Series(np.random.randn(5), index=list('abcde'))
print (s.rank())

