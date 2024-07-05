import numpy as np
import pandas as pd

sample_array = np.array([
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
])
print(sample_array)
df = pd.DataFrame(sample_array[1:], columns=sample_array[0])
df.to_csv('sample_array', index=False)
