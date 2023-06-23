import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the Seaborn style
sns.set_style("darkgrid")

# Read the dataset
washington_post_data = pd.read_csv("Datasets/fatal-police-shootings-data.csv")

# Reduce the dataset to top 10 values of each category
top_names = washington_post_data['name'].value_counts().nlargest(10)
top_kill_weapon = washington_post_data['armed'].value_counts().nlargest(10)
top_cities = washington_post_data['city'].value_counts().nlargest(10)
top_kill_numbers = washington_post_data['state'].value_counts().nlargest(10)

# Plot the count of most common names
plt.figure(figsize=(10, 6))
sns.barplot(x=top_names.index, y=top_names.values, palette="Set2")
plt.title('Most Common Names of Killed People')
plt.xlabel('Name')
plt.ylabel('Death Count')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("Images/Police_Visuals/Top_10_Most_Common_Names.png")
plt.close()

# Plot the count of most common kill weapons
plt.figure(figsize=(10, 6))
sns.barplot(x=top_kill_weapon.index, y=top_kill_weapon.values, palette="Set2")
plt.title('Most Common Kill Weapons')
plt.xlabel('Weapon')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("Images/Police_Visuals/Top_10_Most_Common_Kill_Weapons.png")
plt.close()

# Plot the count of most dangerous cities
plt.figure(figsize=(10, 6))
sns.barplot(x=top_cities.index, y=top_cities.values, palette="Set2")
plt.title('Most Dangerous Cities')
plt.xlabel('City')
plt.ylabel('Death Count')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("Images/Police_Visuals/Top_10_Most_Dangerous_Cities.png")
plt.close()

# Plot the count of kill numbers from different states
plt.figure(figsize=(10, 6))
sns.barplot(x=top_kill_numbers.index, y=top_kill_numbers.values, palette="Set2")
plt.title('Death Count from different States')
plt.xlabel('State')
plt.ylabel('Death Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Images/Police_Visuals/Kill_Numbers.png")
plt.close()

# Number of people killed by race
plt.figure(figsize=(10, 6))
sns.countplot(data=washington_post_data, x="race", palette="Set2")
plt.title('Number of People Killed by Race')
plt.xlabel('Race')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("Images/Police_Visuals/People_Killed_by_Race.png")
plt.close()

# Number of people killed by group of age
washington_post_data["group_of_age"] = pd.cut(washington_post_data["age"], bins=[0, 18, 25, 45, 65, 85, 95],labels=["0-18", "19-25", "26-44","45-64", "65-84", "85_95"])
washington_post_data["group_of_age"].value_counts()
plt.figure(figsize=(10, 6))
sns.countplot(data=washington_post_data, x="group_of_age", palette="Set2")
plt.title('Number of People Killed by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("Images/Police_Visuals/People_Killed_by_Age_Group.png")
plt.close()

# Distribution of signs of mental illness by race and gender
#Convert signs_of_mental_illness variable type to interger
washington_post_data["signs_of_mental_illness"]= washington_post_data["signs_of_mental_illness"].astype("int64")
washington_post_data["signs_of_mental_illness"].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x="race", y="signs_of_mental_illness", hue="gender", data=washington_post_data, palette="Set2")
plt.title('Distribution of Signs of Mental Illness by Race and Gender')
plt.xlabel('Race')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("Images/Police_Visuals/Signs_of_Mental_Illness.png")
plt.close()

# Distribution of flee types of people killed by the police
plt.figure(figsize=(10, 6))
washington_post_data["flee"].value_counts().plot(kind="pie", autopct='%1.2f%%')
plt.title('Distribution of Flee Types of People Killed by the Police')
plt.ylabel('')
plt.tight_layout()
plt.savefig("Images/Police_Visuals/Distribution_of_Flee_Types.png")
plt.close()
