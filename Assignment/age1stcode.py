import pandas as pd
def run(df):

    print("\n========== TASK 1 ==========")

    # Convert Age1stCode into numeric values
    df["Age1stCode_clean"] = pd.to_numeric(
        df["Age1stCode"],
        errors="coerce"
    )

    # Calculate average age
    average_age = df["Age1stCode_clean"].mean()

    # Count valid responses
    valid_responses = df["Age1stCode_clean"].count()

    # Display results
    print("Average age when developers first coded:", average_age)
    print("Valid age responses:", valid_responses)
