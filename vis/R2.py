# -*- coding: gbk -*-
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.ticker import FixedLocator

# ����ȫ������������С
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['xtick.labelsize'] = 18  # x��̶ȵ������С
plt.rcParams['ytick.labelsize'] = 20  # y��̶ȵ������С
plt.rcParams['legend.fontsize'] = 20  # ͼ���������С

# ׼������
df = pd.DataFrame({
    'Model': ['(EMD)-SVR', '(EMD)-LSTM', '(EMD)-GRU', '(EMD)-TCN', '(EMD)-TFR*',
              '(EEMD)-SVR', '(EEMD)-LSTM', '(EEMD)-GRU', '(EEMD)-TCN', '(EEMD)-TFR*',
              '(CEEMDAN)-SVR', '(CEEMDAN)-LSTM', '(CEEMDAN)-GRU', '(CEEMDAN)-TCN', 'TFR'],
    'Metric': ['R2']*15,
    'Value': [
        0.3000, 0.6072, 0.5915, 0.7607, 0.9207,
        0.2268, 0.6352, 0.6040, 0.7501, 0.9264,
        0.3375, 0.7597, 0.6744, 0.7807, 0.9507
    ]
})

# ��������ͼ
plt.figure(figsize=(14, 8))
barplot = sns.barplot(x="Model", y="Value", hue="Metric", data=df, palette=["#FF407D"], edgecolor="black", linewidth=1)

# ����������
# ��ģ������ת��Ϊ��ֵ�������Ա������ѧ����
x_numeric = np.arange(len(df['Model']))
slope, intercept = np.polyfit(x_numeric, df['Value'], 1)  # ���������ߵ�б�ʺͽؾ�
trend_line = slope * x_numeric + intercept  # ���������ߵ�ֵ

# ����������
plt.plot(df['Model'], trend_line, label='Trend Line', color='#1E1F22', linestyle='--')

# ȥ��ͼ������
plt.legend()

# ���ñ�������ǩ
plt.title('')
plt.xlabel('')
plt.ylabel('R2', fontdict={'family': 'Times New Roman', 'size': 22})

# ��תX���ǩ�Ա����Ǹ������Ķ�
x_ticks = barplot.get_xticks()
barplot.xaxis.set_major_locator(FixedLocator(x_ticks))
barplot.set_xticklabels(barplot.get_xticklabels(), rotation=45, horizontalalignment='right')

# ȥ��������
plt.grid(False)

# չʾͼ��
plt.tight_layout()
plt.savefig('R2.pdf', format='pdf', bbox_inches='tight', dpi=600)
plt.show()


