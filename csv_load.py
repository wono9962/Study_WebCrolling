import pandas as pd
import warnings
import sys

warnings.filterwarnings('ignore')

geojeisland = pd.read_csv('../pythonProject1/location/food.csv', encoding='cp949')

pd.set_option('display.max_rows', None)
address = geojeisland[['업소주소']]
print("|" + address)

sys.stdout = open('food.txt', 'w')

for i in range(1):
    print("|" +address)

sys.stdout.close()


