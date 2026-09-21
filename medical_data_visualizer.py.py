import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. استيراد البيانات
df = pd.read_csv("medical_examination.csv")

# 2. إضافة عمود overweight
BMI = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (BMI > 25).astype(int)

# 3. تطبيع البيانات (0 جيد، 1 سيء)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. رسم Cat Plot
def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    fig = sns.catplot(x="variable", y="total", hue="value", col="cardio", data=df_cat, kind="bar").fig
    return fig

# 5. رسم Heat Map
def draw_heat_map():
    # تنظيف البيانات
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # مصفوفة الارتباط
    corr = df_heat.corr()

    # قناع للمثلث العلوي
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # الشكل
    fig, ax = plt.subplots(figsize=(12, 12))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", center=0, cmap="coolwarm")
    return fig
