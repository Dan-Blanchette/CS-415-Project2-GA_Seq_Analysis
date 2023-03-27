import pandas as pd

def load_data():
    """Load data from datafile.csv into a pandas dataframe. without adding a index"""
    df = pd.read_csv('datafile.csv', usecols=[1])
    print(df)
    

def decipher(df):
    """Decipher the data."""

def main():
    """Main function for deciphering a sequence of DNA."""
    load_data()

if (__name__ == '__main__'):
    main()