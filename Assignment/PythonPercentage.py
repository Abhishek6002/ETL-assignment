import pandas as pd

def run(df):

    print("\n========== TASK 2 ==========")

    # Remove rows where language information is missing
    language_data = df.dropna(subset=["LanguageWorkedWith"])

    # Find developers who know Python
    python_developers = language_data[
        language_data["LanguageWorkedWith"].str.contains(
            "Python",
            na=False
        )
    ]

    print("Total developers who reported languages:",len(language_data))

    print("Developers who know Python:",len(python_developers))

    # Calculate Python percentage
    python_percentage = (
        len(python_developers) / len(language_data)
    ) * 100

    print("Overall Python percentage:",round(python_percentage, 2), "%")



    # Calculate Python percentage country-wise
    for country, group in language_data.groupby("Country"):

        total_developers = len(group)

        python_count = group["LanguageWorkedWith"].str.contains(
            "Python",
            na=False
        ).sum()

        percentage = (python_count / total_developers) * 100

        print(country, ":", round(percentage, 2), "%")

    
