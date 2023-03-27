import pandas as pd
from glob_align import align_seq
def load_data():
    """Load data from datafile.csv into a pandas dataframe. without adding a index"""
    df = pd.read_csv('datafile.csv', usecols=[1])
    return df
    

def decipher(df):
    """Decipher the data."""
    for i in range(len(df)):
        # print(df.iloc[i, 0])
        seq1 = df.iloc[i, 0]
        seq2 = df.iloc[i, 1]
        align_seq(seq1, seq2)


def main():
    """Main function for deciphering a sequence of DNA."""
    df = load_data()
    decipher(df)

if (__name__ == '__main__'):
    main()