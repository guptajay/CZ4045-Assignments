import json
import pandas as pd


if __name__=="__main__":
    path = "./Data/reviewSelected100.json"

    records = []

    with open(path, 'r') as f:
        data = f.readlines()
        for i in data:
            records.append(json.loads(i))
    
    df = pd.DataFrame.from_records(records)
    df.to_csv('./Data/review.csv', index=False)



