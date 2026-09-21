import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. قراءة البيانات
    df = pd.read_csv("epa-sea-level.csv")

    # 2. رسم scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label="Data", color="blue")

    # 3. خط الانحدار الأول (1880–2014)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = range(1880, 2051)
    y_pred = res.intercept + res.slope * pd.Series(x_pred)
    plt.plot(x_pred, y_pred, 'r', label="Best fit line (1880–2014)")

    # 4. خط الانحدار الثاني (2000–2014)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = range(2000, 2051)
    y_recent = res_recent.intercept + res_recent.slope * pd.Series(x_recent)
    plt.plot(x_recent, y_recent, 'green', label="Best fit line (2000–2014)")

    # 5. إعدادات الرسم
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()

    # حفظ الصورة
    plt.savefig('sea_level_plot.png')
    return plt.gca()
