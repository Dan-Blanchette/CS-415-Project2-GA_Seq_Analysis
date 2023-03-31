import pandas as pd
from glob_align import align_seq
import os

def load_data():
    """Load data from datafile.csv into a pandas dataframe. without adding a index"""
    df = pd.read_csv('datafile.csv', usecols=[1])
    return df
    

def decipher(df):
    """Decipher the data."""
    
    #delete file if it exists
    if os.path.exists('aligned.csv'):
        os.remove('aligned.csv')

    for i in range(len(df)):
        for j in range(i+1, len(df)):
            val = align_seq(df.iloc[i, 0], df.iloc[i, 0])
            #write aligned 1 and aligned2 to csv file 
            with open('aligned.csv', 'a') as f:
                f.write("Seq1:" + df.iloc[i, 0] + "\n" + "Seq2:" + df.iloc[i, 0] + "\n" + "Score:" + str(val) + "\n\n")
            


def main():
    """Main function for deciphering a sequence of DNA."""
    df = load_data()
    decipher(df)

if (__name__ == '__main__'):
    main()