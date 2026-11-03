import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # What percentage of people with advanced education make more than 50K?
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round(
        (df.loc[higher_education, 'salary'] == '>50K').mean() * 100, 1
    )

    # What percentage of people without advanced education make more than 50K?
    lower_education_rich = round(
        (df.loc[~higher_education, 'salary'] == '>50K').mean() * 100, 1
    )

    # What is the minimum number of hours a person works per week?
    min_work_hours = int(df['hours-per-week'].min())

    # What percentage of people working the minimum hours earn more than 50K?
    min_workers = df['hours-per-week'] == min_work_hours
    rich_percentage = round(
        (df.loc[min_workers, 'salary'] == '>50K').mean() * 100, 1
    )

    # Which country has the highest percentage of people earning more than 50K?
    country_rich_percentages = (
        df['salary'].eq('>50K').groupby(df['native-country']).mean() * 100
    )
    highest_earning_country = country_rich_percentages.idxmax()
    highest_earning_country_percentage = round(
        country_rich_percentages.max(), 1
    )

    # Most popular occupation among people in India earning more than 50K
    india_rich = df.loc[
        (df['native-country'] == 'India') & (df['salary'] == '>50K'),
        'occupation',
    ]
    top_IN_occupation = india_rich.value_counts().idxmax()

    if print_data:
        print('Number of each race:\n', race_count)
        print('Average age of men:', average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f'Min work time: {min_work_hours} hours/week')
        print(f'Percentage of rich among those who work fewest hours: {rich_percentage}%')
        print('Country with highest percentage of rich:', highest_earning_country)
        print(f'Highest percentage of rich people in country: {highest_earning_country_percentage}%')
        print('Top occupations in India:', top_IN_occupation)

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
        'top_IN_occupation': top_IN_occupation,
    }
