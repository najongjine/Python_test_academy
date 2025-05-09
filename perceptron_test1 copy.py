import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 데이터 로드
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data'
columns = [f'feature_{i}' for i in range(57)] + ['label']
print(columns)
#data = pd.read_csv(url, header=None, names=columns)