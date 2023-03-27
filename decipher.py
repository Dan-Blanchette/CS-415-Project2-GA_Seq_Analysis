import pandas as pd
from glob_align import align_seq
def load_data():
    """Load data from datafile.csv into a pandas dataframe. without adding a index"""
    df = pd.read_csv('datafile.csv', usecols=[1])
    return df
    

def decipher(df):
    """Decipher the data."""
    for i in range(len(df)):
        for j in range(i+1, len(df)):
            align_seq(df.iloc[i, 0], df.iloc[j, 0])
            


def main():
    """Main function for deciphering a sequence of DNA."""
    df = load_data()
    decipher(df)

if (__name__ == '__main__'):
    main()