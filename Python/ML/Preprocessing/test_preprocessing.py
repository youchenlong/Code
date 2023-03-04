import pandas as pd
from numpy import NaN
# 读取数据
# df = pd.read_excel('./dataset.xlsx', index_col=0, dtype={'sex':str, 'height':float, 'weight':float})
df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'name': ['Alice', 'Bob', 'Catherine', 'Bob', 'David', 'Eric', 'Frank', 'Gina', 'Helen'],
    'sex': ['female', 'male', 'female', 'male', 'male', 'male', 'male', 'female', 'female'],
    'height': [165.0, 175.0, 168.0, 175.0, 180.0, 172.0, 178.0, 162.0, 166.0],
    'weight': [100.0, 140.0, NaN, 140.0, 150.0, 130.0, 135.0, 92.0, 96.0],
    'age': [18, 22, NaN, 22, 122, 21, 23, 19, 20],
    'grade': ['freshman', 'senior', 'sophomore', 'senior', 'junior', 'sophomore', 'senior', 'sophomore', 'junior']
}).set_index('id')
df = df.drop(columns='name')
print(df)

# 一、数据清洗
# 1.重复值
df.drop_duplicates(inplace=True)
# 1.缺失值
# df.fillna(method='ffill', inplace=True)
# df.fillna(value=df.mean(), inplace=True)
df.dropna(axis=0, inplace=True)
# 3.异常值
df.mask(df.sub(df.mean()).div(df.std()).abs().gt(2), inplace=True)
df.fillna(df.median(), inplace=True)

# 二、数据转换
# 1.类型转换
df['height'] = df['height'].astype("float32").round(2)
df['weight'] = df['weight'].astype("float32").round(2)
df['age'] = df['age'].astype("int32")
df = pd.get_dummies(df, columns=['sex'])
df['grade'] = df['grade'].replace(['freshman', 'sophomore', 'junior', 'senior'], [1, 2, 3, 4]).astype("int32")
# 1.归一化和正则化
# Min-Max Scaling
min_max = lambda x: (x - x.min()) / (x.max() - x.min())
# Z-score Normalization
# z_score = lambda x: (x-x.mean()) / x.std()
df[['height', 'weight', 'age']] = df[['height', 'weight', 'age']].apply(min_max)

# 三、数据描述
# 1.统计量
df.describe()
# 1.可视化
# df.plot()

print(df)
df.to_csv("preprocessing.csv")
