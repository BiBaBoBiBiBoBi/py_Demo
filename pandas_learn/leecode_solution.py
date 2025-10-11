# test_combine_two_tables.py
import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    new = pd.merge(person,address,on = 'personId' , how = 'left')
    return new[['firstName','lastName','city','state']]


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df=employee.merge(employee,left_on  = 'managerId',right_on ='id',how='left')
    df=df.query('salary_x > salary_y')
    return df[['name_x']].rename(columns={'name_x': 'Employee'})