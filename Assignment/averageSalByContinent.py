
import pandas as pd


def run(df):

    print("\n========== TASK 3 ==========")

    # Map countries to continents
    country_to_continent = {

        # Asia
        "Afghanistan": "Asia",
        "Armenia": "Asia",
        "Azerbaijan": "Asia",
        "Bahrain": "Asia",
        "Bangladesh": "Asia",
        "Bhutan": "Asia",
        "Brunei": "Asia",
        "Cambodia": "Asia",
        "China": "Asia",
        "Hong Kong": "Asia",
        "India": "Asia",
        "Indonesia": "Asia",
        "Iran": "Asia",
        "Iraq": "Asia",
        "Israel": "Asia",
        "Japan": "Asia",
        "Jordan": "Asia",
        "Kazakhstan": "Asia",
        "Kuwait": "Asia",
        "Kyrgyzstan": "Asia",
        "Laos": "Asia",
        "Lebanon": "Asia",
        "Malaysia": "Asia",
        "Maldives": "Asia",
        "Mongolia": "Asia",
        "Myanmar": "Asia",
        "Nepal": "Asia",
        "North Korea": "Asia",
        "Oman": "Asia",
        "Pakistan": "Asia",
        "Palestine": "Asia",
        "Philippines": "Asia",
        "Qatar": "Asia",
        "Saudi Arabia": "Asia",
        "Singapore": "Asia",
        "South Korea": "Asia",
        "Sri Lanka": "Asia",
        "Syria": "Asia",
        "Taiwan": "Asia",
        "Tajikistan": "Asia",
        "Thailand": "Asia",
        "Turkey": "Asia",
        "United Arab Emirates": "Asia",
        "Uzbekistan": "Asia",
        "Vietnam": "Asia",
        "Yemen": "Asia",

        # Europe
        "Albania": "Europe",
        "Andorra": "Europe",
        "Austria": "Europe",
        "Belarus": "Europe",
        "Belgium": "Europe",
        "Bosnia and Herzegovina": "Europe",
        "Bulgaria": "Europe",
        "Croatia": "Europe",
        "Cyprus": "Europe",
        "Czech Republic": "Europe",
        "Denmark": "Europe",
        "Estonia": "Europe",
        "Finland": "Europe",
        "France": "Europe",
        "Georgia": "Europe",
        "Germany": "Europe",
        "Greece": "Europe",
        "Hungary": "Europe",
        "Iceland": "Europe",
        "Ireland": "Europe",
        "Isle of Man": "Europe",
        "Italy": "Europe",
        "Kosovo": "Europe",
        "Latvia": "Europe",
        "Liechtenstein": "Europe",
        "Lithuania": "Europe",
        "Luxembourg": "Europe",
        "Malta": "Europe",
        "Moldova": "Europe",
        "Monaco": "Europe",
        "Montenegro": "Europe",
        "Netherlands": "Europe",
        "North Macedonia": "Europe",
        "Norway": "Europe",
        "Poland": "Europe",
        "Portugal": "Europe",
        "Romania": "Europe",
        "Russia": "Europe",
        "San Marino": "Europe",
        "Serbia": "Europe",
        "Slovakia": "Europe",
        "Slovenia": "Europe",
        "Spain": "Europe",
        "Sweden": "Europe",
        "Switzerland": "Europe",
        "Ukraine": "Europe",
        "United Kingdom": "Europe",

        # North America
        "Antigua and Barbuda": "North America",
        "Bahamas": "North America",
        "Barbados": "North America",
        "Belize": "North America",
        "Canada": "North America",
        "Costa Rica": "North America",
        "Cuba": "North America",
        "Dominican Republic": "North America",
        "El Salvador": "North America",
        "Guatemala": "North America",
        "Haiti": "North America",
        "Honduras": "North America",
        "Jamaica": "North America",
        "Mexico": "North America",
        "Nicaragua": "North America",
        "Panama": "North America",
        "Trinidad and Tobago": "North America",
        "United States": "North America",

        # South America
        "Argentina": "South America",
        "Bolivia": "South America",
        "Brazil": "South America",
        "Chile": "South America",
        "Colombia": "South America",
        "Ecuador": "South America",
        "Guyana": "South America",
        "Paraguay": "South America",
        "Peru": "South America",
        "Uruguay": "South America",
        "Venezuela": "South America",

        # Africa
        "Algeria": "Africa",
        "Angola": "Africa",
        "Benin": "Africa",
        "Botswana": "Africa",
        "Burkina Faso": "Africa",
        "Burundi": "Africa",
        "Cameroon": "Africa",
        "Cape Verde": "Africa",
        "Central African Republic": "Africa",
        "Chad": "Africa",
        "Democratic Republic of the Congo": "Africa",
        "Djibouti": "Africa",
        "Egypt": "Africa",
        "Eritrea": "Africa",
        "Ethiopia": "Africa",
        "Gabon": "Africa",
        "Gambia": "Africa",
        "Ghana": "Africa",
        "Guinea": "Africa",
        "Ivory Coast": "Africa",
        "Kenya": "Africa",
        "Lesotho": "Africa",
        "Liberia": "Africa",
        "Libya": "Africa",
        "Madagascar": "Africa",
        "Malawi": "Africa",
        "Mali": "Africa",
        "Mauritania": "Africa",
        "Mauritius": "Africa",
        "Morocco": "Africa",
        "Mozambique": "Africa",
        "Namibia": "Africa",
        "Niger": "Africa",
        "Nigeria": "Africa",
        "Republic of the Congo": "Africa",
        "Rwanda": "Africa",
        "Senegal": "Africa",
        "Sierra Leone": "Africa",
        "Somalia": "Africa",
        "South Africa": "Africa",
        "South Sudan": "Africa",
        "Sudan": "Africa",
        "Swaziland": "Africa",
        "Tanzania": "Africa",
        "Togo": "Africa",
        "Tunisia": "Africa",
        "Uganda": "Africa",
        "Zambia": "Africa",
        "Zimbabwe": "Africa",

        # Oceania
        "Australia": "Oceania",
        "Fiji": "Oceania",
        "New Zealand": "Oceania",
        "Papua New Guinea": "Oceania"
    }

    # Remove rows with missing country or salary
    salary_data = df.dropna(
        subset=["Country", "ConvertedComp"]
    ).copy()

    # Create a continent column
    salary_data["Continent"] = salary_data["Country"].map(
        country_to_continent
    )

    # Check countries that were not mapped
    unmapped = salary_data[
        salary_data["Continent"].isnull()
    ]["Country"].unique()

    print("Unmapped countries:", unmapped)

    # Remove countries without a continent mapping
    salary_data = salary_data.dropna(
        subset=["Continent"]
    )

    # Calculate average salary by continent
    average_salary = salary_data.groupby(
        "Continent"
    )["ConvertedComp"].mean()

    # Sort salary from highest to lowest
    average_salary = average_salary.sort_values(
        ascending=False
    )

    print("\nAverage salary by continent (USD):")
    print(average_salary.round(2))
