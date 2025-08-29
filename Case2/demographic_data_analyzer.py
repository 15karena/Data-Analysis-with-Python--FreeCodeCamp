import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelor_count = (df['education'] == 'Bachelors').sum()
    total_count = len(df)
    percentage_bachelors = round((bachelor_count/total_count)*100,1)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0]
    salary = higher_education[higher_education['salary']=='>50K'].shape[0]
    higher_education_rich = round((salary/advanced_education)*100,1)
    
    education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0]
    salary = education[education['salary']=='>50K'].shape[0]
    lower_education_rich = round((salary/lower_education)*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = (df['hours-per-week']).min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df_sum = df[df['hours-per-week']== 1]
    df_sum_total = df[df['hours-per-week']== 1].shape[0]
    df_salary_sum = (df_sum['salary'] == '>50K').sum()
    rich_percentage = round((df_salary_sum/df_sum_total)*100)


    # What country has the highest percentage of people that earn >50K?
    total_salary_per_country_s = df[df['salary'] == '>50K'].groupby('native-country')['salary'].count()
    total_salary_per_country = df.groupby('native-country')['salary'].count()
    total_percentage_per_country = ((total_salary_per_country_s/total_salary_per_country)*100)
    highest_earning_country = total_percentage_per_country.idxmax()
    highest_earning_country_percentage = round(total_percentage_per_country.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

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
