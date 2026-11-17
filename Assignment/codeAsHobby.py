
import pandas as pd
import country_converter as coco


def run(df):

    print("\n========== TASK 5 ==========")

    # Create country-to-continent converter
    cc = coco.CountryConverter()

    # Keep rows with country and hobby information
    hobby_data = df.dropna(
        subset=["Country", "Hobbyist"]
    ).copy()

    # Remove placeholder country responses
    hobby_data = hobby_data[
        ~hobby_data["Country"].str.contains(
            "Other Country",
            case=False,
            na=False
        )
    ].copy()

    # Convert countries into continents
    hobby_data["Continent"] = cc.convert(
        names=hobby_data["Country"],
        to="continent",
        not_found=None
    )

    # Remove countries that could not be mapped
    hobby_data = hobby_data.dropna(
        subset=["Continent"]
    )

    # Select developers who code as a hobby
    hobby_data = hobby_data[
        hobby_data["Hobbyist"] == "Yes"
    ]

    # Count hobby coders by continent
    hobby_report = hobby_data.groupby(
        "Continent"
    ).size().reset_index(name="Hobby_Coders")

    # Sort results in descending order
    hobby_report = hobby_report.sort_values(
        by="Hobby_Coders",
        ascending=False
    )

    # Display report
    print("\nHobby coders by continent:")
    print(hobby_report.to_string(index=False))

    print("\nTotal hobby coders:", len(hobby_data))
