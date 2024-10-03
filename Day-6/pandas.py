import pandas as pd 

def pandas_operations()->dict:
    data ={
        "Name":["Alice","Bob","Charlie"],
        "Age":[25,30,35]
    }

    df =pd.DataFrame(data)

    filtered_df=df[df['Age']>28]

    sum_of_ages=df['Age'].sum()

    result ={
        "filtered_dataframe":filtered_df,
        "sum_of_ages":sum_of_ages
    }

    return result