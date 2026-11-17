
import pandas as pd

# Load the dataset
df = pd.read_csv(
    "../stack-overflow-developer-survey-2019/survey_results_public.csv",
    low_memory=False
)

print("Dataset loaded successfully!")
print("Shape:", df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nDataset information:")
df.info()

# Execute assignment tasks
import age1stcode as task1
task1.run(df)

#Execute the second task to calculate the percentage of developers who know Python per country
import PythonPercentage as task2
task2.run(df)


# Execute the third task to calculate the average salary by continent
import averageSalByContinent as task3
task3.run(df)


#Execute the fourth task to find the most desired programming language for 2020
import mostDesiredProgrammingLanguage as task4
task4.run(df)


#Execute the fifth task to find the number of developers who code as a hobby by continent
import codeAsHobby as task5
task5.run(df)

# Execute the sixth task to find the average job and career satisfaction by continent
import jobAndCarrerSatisfication as task6
task6.run(df)