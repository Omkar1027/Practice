import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_path = "student_data.csv"
database = pd.read_csv(data_path)

print(database)

x_axis = "Age"
y_axis = "Name"

sns.scatterplot(
    x=x_axis,
    y=y_axis,
    data=database,
    hue="Surname",
    style="Surname",
    size="Age",
    palette="Set3"
)

plt.title("Student Age Distribution by Name")
plt.xlabel(x_axis)
plt.ylabel(y_axis)
plt.xticks(rotation=45)

plt.show()

x_data = database[x_axis]
y_data = database[y_axis]

plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, c="blue", alpha=0.7, edgecolors="black")

plt.title("Student Age Distribution by Name (Matplotlib)")
plt.xlabel(x_axis)
plt.ylabel(y_axis)
plt.xticks(rotation=45)
plt.grid(True)

plt.show()
