
import pandas as pd


def run(df):

    print("\n========== TASK 4 ==========")

    # Remove rows with missing language responses
    language_data = df["LanguageDesireNextYear"].dropna()

    # Split multiple languages into separate rows
    desired_languages = language_data.str.split(";").explode()

    # Remove unnecessary spaces
    desired_languages = desired_languages.str.strip()

    # Remove empty values
    desired_languages = desired_languages[desired_languages != ""]

    # Count how many developers want each language
    language_counts = desired_languages.value_counts()

    # Find the most desired language
    most_desired_language = language_counts.idxmax()
    highest_count = language_counts.max()

    print("Most desired programming language for 2020:",
          most_desired_language)

    print("Number of developers who desired it:",
          highest_count)

    # Display top 10 desired languages
    print("\nTop 10 most desired programming languages:")
    print(language_counts.head(10))
