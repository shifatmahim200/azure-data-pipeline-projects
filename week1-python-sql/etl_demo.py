import pandas as pd

# Sample ETL script
def extract():
    print("Extracting sample data...")
    data = {'student': ['Anna', 'Ben', 'Clara'], 'score': [85, 90, 95]}
    df = pd.DataFrame(data)
    return df

def transform(df):
    print("Transforming data...")
    df['grade'] = ['A' if s >= 90 else 'B' for s in df['score']]
    return df

def load(df):
    print("Loading data...")
    df.to_csv('data/output.csv', index=False)
    print("Data saved to data/output.csv")

if __name__ == "__main__":
    df = extract()
    df = transform(df)
    load(df)

