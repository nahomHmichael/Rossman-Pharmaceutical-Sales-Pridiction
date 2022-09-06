import pandas as pd 
from log_helper import logger

class DataInfo:
    def __init__(self,df):
        self.df =df
    def colums_WithMissingValue(self):
        miss = []
        dff = self.df.isnull().any()
        summ = 0
        for col in dff:
            if col == True:
                miss.append(dff.index[summ])
            summ += 1
        
        return miss

    def get_column_based_missing_percentage(self):
        col_null = self.df.isnull().sum()
        total_entries = self.df.shape[0]
        missing_percentage = []
        for col_missing_entries in col_null:
            value = str(
                round(((col_missing_entries/total_entries) * 100), 2)) + " %"
            missing_percentage.append(value)

        missing_df = pd.DataFrame(col_null, columns=['total_missing_values'])
        missing_df['missing_percentage'] = missing_percentage
        return missing_df

        