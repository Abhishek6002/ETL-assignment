# Stack Overflow Developer Survey 2019 - ETL Assignment

## Project Overview

This project performs data extraction, transformation, and analysis using the Stack Overflow Developer Survey 2019 dataset.

The objective is to clean and process survey data using Python and Pandas, extract meaningful information, and generate reports based on developer responses.

## Technologies Used

- Python 3.11
- Pandas
- Country Converter
- CSV Dataset

## Project Structure

```text
stackoverflow-etl/
│
├── Assignment/
│   ├── main.py
│   ├── task1.py
│   ├── task2.py
│   ├── task3.py
│   ├── task4.py
│   ├── task5.py
│   └── task6.py
│
├── stack-overflow-developer-survey-2019/
│   ├── survey_results_public.csv
│   ├── survey_results_schema.csv
│   ├── README_2019.txt
│   └── so_survey_2019.pdf
│
├── requirements.txt
└── README.md
```

## Dataset

The project uses the Stack Overflow Developer Survey 2019 dataset.

The dataset contains information about developers, including:

- Country
- Age when first learning to code
- Programming languages used
- Programming languages developers want to learn
- Employment and salary information
- Hobbyist status
- Job satisfaction
- Career satisfaction

The dataset is loaded once in `main.py` and passed to individual task modules for analysis.

## Tasks Performed

### Task 1: Average Age When Developers First Started Coding

- Cleaned the `Age1stCode` column.
- Converted valid numeric responses into numbers.
- Handled missing and invalid values.
- Calculated the average age at which developers started coding.

### Task 2: Percentage of Developers Who Know Python by Country

- Processed the `LanguageWorkedWith` column.
- Identified developers who reported using Python.
- Calculated the percentage of Python developers in each country.
- Sorted the results by percentage.

### Task 3: Average Salary by Continent

- Processed country and salary information.
- Used the Country Converter library to map countries to continents.
- Calculated the average salary for each continent.
- Excluded invalid or unavailable country mappings.

### Task 4: Most Desired Programming Language for 2020

- Processed the `LanguageDesireNextYear` column.
- Split multiple programming languages reported by developers.
- Counted how many developers selected each language.
- Identified the most desired programming language.
- Displayed the top 10 most desired languages.

### Task 5: Number of Hobby Coders by Continent

- Processed the `Hobbyist` and `Country` columns.
- Identified developers who code as a hobby.
- Converted countries into continents.
- Calculated the number of hobby coders in each continent.

**Dataset Limitation:** The Stack Overflow Developer Survey 2019 public dataset used in this project does not contain a Gender column. The supplied schema file also does not provide gender information. Therefore, the requested gender-wise analysis (Man, Woman, Others) could not be performed. This task was completed using continent-wise analysis only. No gender information was assumed or fabricated.

### Task 6: Job and Career Satisfaction by Continent

- Processed the `JobSat` and `CareerSat` columns.
- Converted textual satisfaction responses into numerical scores:
  - Very dissatisfied: 1
  - Slightly dissatisfied: 2
  - Neither satisfied nor dissatisfied: 3
  - Slightly satisfied: 4
  - Very satisfied: 5
- Converted countries into continents.
- Calculated average job satisfaction and career satisfaction for each continent.

**Dataset Limitation:** Similar to Task 5, gender information is unavailable in the dataset. Therefore, the requested gender-wise satisfaction analysis could not be performed. The analysis was completed continent-wise instead.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Install Dependencies

```bash
py -3.11 -m pip install -r requirements.txt
```

### 3. Download the Dataset

Download the Stack Overflow Developer Survey 2019 dataset and extract it into the project root directory.

The expected dataset folder name is:

```text
stack-overflow-developer-survey-2019
```

Ensure that `survey_results_public.csv` is inside this folder.

### 4. Run the Project

Navigate to the Assignment directory:

```bash
cd Assignment
```

Run the main file:

```bash
py -3.11 main.py
```

The program executes all six tasks and displays their results in the terminal.

## Requirements

The project requires:

- pandas
- country_converter

Install them using the `requirements.txt` file.

## Key Concepts Covered

- Extract, Transform, Load (ETL)
- Reading and processing CSV files
- Data cleaning and handling missing values
- Data type conversion
- String operations
- Filtering and sorting
- Grouping and aggregation
- Calculating averages and percentages
- Splitting and expanding categorical data
- Country-to-continent mapping
- Working with multiple Python modules

## Conclusion

This project demonstrates how Python and Pandas can be used to process a large real-world survey dataset and extract useful insights about developers.

It provides practical experience with ETL operations, data cleaning, transformation, grouping, aggregation, and data analysis.