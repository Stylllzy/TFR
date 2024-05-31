# -*- coding: gbk -*-
# ���������
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# ����������
data = {
    "Model": ["SVR", "LSTM", "GRU", "TCN", "TFR(AE+TCN)"],
    # "MSE": [9.3571, 2.3259, 2.1919, 2.1238, 0.7408],
    "MAE": [2.5391, 1.1829, 1.1153, 1.1655, 0.5828],
    "RMSE": [3.0589, 1.5251, 1.4805, 1.4573, 0.8607],
    "MAPE": [0.0607, 0.03, 0.0278, 0.0288, 0.0144]
}

# ������ת��Ϊ����ʽ���ʺ�����Seaborn�Ļ�ͼ����
df_long = pd.melt(pd.DataFrame(data), id_vars='Model', var_name='Metric', value_name='Error')

# ����ȫ������������С
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['xtick.labelsize'] = 20  # x��̶ȵ������С
plt.rcParams['ytick.labelsize'] = 20  # y��̶ȵ������С
plt.rcParams['legend.fontsize'] = 20  # ͼ���������С

# ������״ͼ
plt.figure(figsize=(14, 6))
barplot = sns.barplot(x='Model', y='Error', hue='Metric', data=df_long,
                      palette=["#4793AF", "#FFC470", "#DD5746", "#8B322C"], edgecolor="black", linewidth=1)

# ����ͼ��
plt.legend()

# ����ͼ�α��⼰�������ǩ
plt.title('')
plt.xlabel('')
plt.ylabel('Error', fontdict={'family': 'Times New Roman', 'size': 22})
plt.tick_params(axis='both', direction='in')

plt.savefig('single_model.pdf', format='pdf', bbox_inches='tight', dpi=600)
# ��ʾͼ��
plt.show()

