import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data_path = "student_data.csv"
database = pd.read_csv(data_path)

# ---- Bar Plot using Seaborn ----
plt.figure(figsize=(8, 6))
sns.barplot(x="Name", y="Age", data=database, palette="Set2")

plt.title("Age of Students by Name")
plt.xlabel("Name")
plt.ylabel("Age")
plt.xticks(rotation=45)
plt.show()

# ---- Histogram using Seaborn ----
plt.figure(figsize=(8, 6))
sns.histplot(database["Age"], bins=5, kde=False, color="green")

plt.title("Distribution of Ages")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# ---- Density Plot using Seaborn ----
plt.figure(figsize=(8, 6))
sns.kdeplot(database["Age"], shade=True, color="purple")

plt.title("Density Plot of Ages")
plt.xlabel("Age")
plt.ylabel("Density")
plt.grid(True)
plt.show()

# ---- Bar Plot using Matplotlib ----
plt.figure(figsize=(8, 6))
plt.bar(database["Name"], database["Age"], color="lightblue")

plt.title("Age of Students by Name (Matplotlib)")
plt.xlabel("Name")
plt.ylabel("Age")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# ---- Histogram using Matplotlib ----
plt.figure(figsize=(8, 6))
plt.hist(database["Age"], bins=5, color="orange", edgecolor="black")

plt.title("Distribution of Ages (Matplotlib)")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# ---- Density Plot using Matplotlib ----
plt.figure(figsize=(8, 6))
database["Age"].plot(kind='density', color='red')

plt.title("Density Plot of Ages (Matplotlib)")
plt.xlabel("Age")
plt.ylabel("Density")
plt.grid(True)
plt.show()
