import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt


DATA_SOURCE = r'C:\git\python\projects\Machine-Learning\bank_affluent_classif\data\bank_customer_data.csv'

df = pd.read_csv(DATA_SOURCE)

print(df.describe)

#def plot_age


#Box Plot for Age vs C Seg
# sns.violinplot(data=df, x="C_seg", y="C_AGE", hue="C_seg")
# sns.violinplot(data=df, x="C_seg", y="C_AGE", hue="C_seg", split=True,gap=0, inner="quart")

#Box Plot for Age vs C Seg per Occupaton
#sns.violinplot(data=df, x="gn_occ", y="C_AGE", hue="C_seg", split=True,gap=0, inner="quart")

#Box Plot for Age vs C Seg per MthCasa
plt.figure(figsize=(10, 6))  # Adjust the figure size to your needs
ax = sns.violinplot(data=df, x="C_seg", y="AVG_TRN_AMT", hue="C_seg")
# ax.set_yscale('log')                    # Set the y-axis to log scale
# Set labels and title if necessary
plt.xlabel('Customer Segment')
plt.ylabel('MTHCASA')
plt.title('Violin Plot of MTHCASA by Customer Segment with Log Scale')

# sns.violinplot(data=df, x="C_seg", y="MTHCASA", hue="C_seg", split=True,gap=0, inner="quart")


plt.show()
# sns.violinplot(data=df, x="class", y="age", hue="alive")
# sns.violinplot(data=df, x="class", y="age", hue="alive", fill=False)
#Split Violin
# sns.violinplot(data=df, x="class", y="age", hue="alive", split=True, inner="quart")
# sns.violinplot(data=df, x="class", y="age", hue="alive", split=True, gap=.1, inner="quart")


print(df['C_AGE'])