import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # return customers.drop_duplicates('email')
    return customers.drop_duplicates(subset="email", keep="first")