import pandas as pd
import zipfile

zip_path = "C:/Users/msnit/Downloads/developer_survey_2019.zip"
with zipfile.ZipFile(zip_path, 'r') as z:
    z.extractall("unzippeddata")

df = pd.read_csv("unzippeddata/survey_results_public.csv")


print(df.head())
print(df.columns)
print(df.info())
na_percentage = df.isna().mean() * 100
print(na_percentage)

age = pd.to_numeric(df['Age1stCode'],errors="coerce")
average_age = age.mean()
print("Average age:", average_age)

#percentage of developers who know pythond
df["Knows_python"] = (
    df["LanguageWorkedWith"]
    .fillna("")
    .str.split(";")
    .apply(lambda languages: "Python" in languages)
)
total_developers=(df.groupby("Country").size())
python_developers = (df[df["Knows_python"]].groupby("Country").size())
python_percentage = (
    python_developers
    / total_developers
    * 100
)

# Step 5: Convert the result into a DataFrame

python_report = python_percentage.reset_index()

python_report.columns = [
    "Country",
    "Python_Percentage"
]


# Round the percentage to 2 decimal places

python_report["Python_Percentage"] = (
    python_report["Python_Percentage"]
    .round(2)
)


# Step 6: Display the result

print(python_report)
