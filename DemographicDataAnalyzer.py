#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from ucimlrepo import fetch_ucirepo

def calculate_demographic_data(print_data=True):
    # Fetch dataset
    adult = fetch_ucirepo(id=2)
    
    # Combine features and target into one dataframe
    df = pd.concat([adult.data.features, adult.data.targets], axis=1)
    
    # Print column names to identify the correct target column name
    print("Column names in the dataframe:\n", df.columns)

    # Assuming the target column might be named 'income'
    target_column = 'income'  

    # How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()
    if print_data:
        print("Number of each race:\n", race_count)

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    if print_data:
        print(f"Average age of men: {average_age_men}")

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(100 * df['education'].value_counts(normalize=True)['Bachelors'], 1)
    if print_data:
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")

    # What percentage of people with advanced education make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    higher_education_rich = round(100 * df[higher_education & (df[target_column] == '>50K')].shape[0] / df[higher_education].shape[0], 1)
    lower_education_rich = round(100 * df[lower_education & (df[target_column] == '>50K')].shape[0] / df[lower_education].shape[0], 1)
    if print_data:
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")

    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()
    if print_data:
        print(f"Min work time: {min_work_hours} hours/week")

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(100 * num_min_workers[num_min_workers[target_column] == '>50K'].shape[0] / num_min_workers.shape[0], 1)
    if print_data:
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")

    # What country has the highest percentage of people that earn >50K?
    country_stats = df.groupby('native-country')[target_column].apply(lambda x: (x == '>50K').mean()).sort_values(ascending=False)
    highest_earning_country = country_stats.index[0]
    highest_earning_country_percentage = round(100 * country_stats.iloc[0], 1)
    if print_data:
        print(f"Country with highest percentage of rich: {highest_earning_country}")
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df[target_column] == '>50K')]['occupation'].value_counts().index[0]
    if print_data:
        print(f"Top occupations in India: {top_IN_occupation}")

    # Return values
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Call the function to see the results
calculate_demographic_data()




