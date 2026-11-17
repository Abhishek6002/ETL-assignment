
import pandas as pd
import country_converter as coco


def run(df):

    print("\n========== TASK 6 ==========")

    # Create country-to-continent converter
    cc = coco.CountryConverter()

    # Keep rows with required information
    satisfaction_data = df.dropna(
        subset=["Country", "JobSat", "CareerSat"]
    ).copy()

    # Remove placeholder country responses
    satisfaction_data = satisfaction_data[
        ~satisfaction_data["Country"].str.contains(
            "Other Country",
            case=False,
            na=False
        )
    ].copy()

    # Map countries to continents
    satisfaction_data["Continent"] = cc.convert(
        names=satisfaction_data["Country"],
        to="continent",
        not_found=None
    )

    # Remove unmapped countries
    satisfaction_data = satisfaction_data.dropna(
        subset=["Continent"]
    )

    # Convert satisfaction categories into numerical scores
    satisfaction_mapping = {
        "Very dissatisfied": 1,
        "Slightly dissatisfied": 2,
        "Neither satisfied nor dissatisfied": 3,
        "Slightly satisfied": 4,
        "Very satisfied": 5
    }

    satisfaction_data["JobSat_Score"] = (
        satisfaction_data["JobSat"].map(satisfaction_mapping)
    )

    satisfaction_data["CareerSat_Score"] = (
        satisfaction_data["CareerSat"].map(satisfaction_mapping)
    )

    # Calculate average satisfaction by continent
    satisfaction_report = satisfaction_data.groupby(
        "Continent"
    ).agg(
        Average_Job_Satisfaction=("JobSat_Score", "mean"),
        Average_Career_Satisfaction=("CareerSat_Score", "mean"),
        Total_Responses=("Country", "count")
    ).reset_index()

    # Round average values
    satisfaction_report[
        ["Average_Job_Satisfaction", "Average_Career_Satisfaction"]
    ] = satisfaction_report[
        ["Average_Job_Satisfaction", "Average_Career_Satisfaction"]
    ].round(2)

    # Display results
    print("\nJob and Career Satisfaction by Continent:")
    print(satisfaction_report.to_string(index=False))

