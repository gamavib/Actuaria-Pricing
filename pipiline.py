import pandas as pd
###print(pd.__version__)
import numpy as np
#print(np.__version__)

raa_df = pd.read_csv(
    "https://raw.githubusercontent.com/casact/chainladder-python/master/chainladder/utils/data/raa.csv"
)
raa_df.head(20)