import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.figure(figsize=(8, 6))
ts = pd.Series(np.random.randn(100), index=pd.date_range(
    '1/1/2020', periods=100))
ts = ts.cumsum()
ts.plot()
plt.show()
