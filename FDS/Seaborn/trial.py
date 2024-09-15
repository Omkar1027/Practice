import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# roll_no=[1,2,3,4,5,6,7,8,9]
# marks=[10,1,33,83,2,99,33,88,0]
# sample=pd.DataFrame({"RollNo":roll_no, "Marks":marks})
# sample.head()
# print(sample)

# sns.lineplot(x='RollNo', y='Marks', data=sample)
# plt.title('StudentsMarks')
# plt.show()

planetdf=pd.read_csv('FDS/Seaborn/planets.csv')
print(planetdf)

sns.lineplot(x='year', y='mass', data=planetdf)
plt.show()