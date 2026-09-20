import pandas as pd

def calculate_demographic_data(print_data=True):
    # قراءة البيانات
    df = pd.read_csv("adult.data.csv")

    # 1. عدد الأشخاص حسب العِرق
    race_count = df['race'].value_counts()

    # 2. متوسط عمر الرجال
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. نسبة الحاصلين على بكالوريوس
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. نسبة أصحاب التعليم المتقدم (>50K)
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)

    # 5. نسبة أصحاب التعليم غير المتقدم (>50K)
    lower_education = ~higher_education
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    # 6. أقل عدد ساعات عمل بالأسبوع
    min_work_hours = df['hours-per-week'].min()

    # 7. نسبة من يعملون أقل ساعات ولديهم >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # 8. الدولة ذات أعلى نسبة >50K
    country_rich = (df[df['salary'] == '>50K']['native-country'].value_counts() /
                    df['native-country'].value_counts()) * 100
    highest_earning_country = country_rich.idxmax()
    highest_earning_country_percentage = round(country_rich.max(), 1)

    # 9. أكثر وظيفة شائعة في الهند لمن يكسبون >50K
    india_top_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print("Min work time:", min_work_hours, "hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage:", highest_earning_country_percentage)
        print("Top occupation in India:", india_top_occupation)

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
        'india_top_occupation': india_top_occupation
    }
