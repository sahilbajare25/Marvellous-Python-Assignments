import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def main():

    data = {'marks':[85,np.nan, 90,np.nan,95]}

    df = pd.DataFrame(data)

    new_df = df.interpolate()

    print(new_df)
    
if __name__ == "__main__":
    main()