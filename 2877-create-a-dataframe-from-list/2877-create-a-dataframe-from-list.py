import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    
    details = {
        "student_id": [data[0] for data in student_data],
        "age": [data[1] for data in student_data]
    }
    return pd.DataFrame(details)