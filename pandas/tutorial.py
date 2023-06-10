import pandas as pd

# load from CSV
df = pd.read_csv('sample_data/california_housing_train.csv')

# print size
df.shape

type(df)

# print
df.head(3)
df['longitude'].head(3)

# save to CSV
df.to_csv('sample.csv')

#-----------------------
# statistics
#-----------------------
# 平均
df.mean()
# 分散
df.var()
# 各列の None, NaN, NaT のいずれでもない値の数
df.count()
# データの概要
df.describe()

#-----------------------
# show
#-----------------------
df.iloc[0,0]
df.iloc[1,1]

# すべての行の、最後の列を選択
t = df.iloc[:, -1]
  # check type
  type(t)
  #> <class 'pandas.core.series.Series'>

# すべての行の、先頭の列から末尾の列のひとつ手前までを選択
x = df.iloc[:, :-1]

# median_house_value 列を選択し、全要素に対し 70000 より大きいかどうかを計算
mask = df['median_house_value'] > 70000
mask.head()
#> 0    False
#> 1     True
#> 2     True
#> 3     True
#> 4    False


