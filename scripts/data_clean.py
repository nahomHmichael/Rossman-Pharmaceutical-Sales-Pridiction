import pandas as pd
import numpy as np
from log_helper import logger

class DataClean:
    def __init__(self,df,deep=False) -> None:
        if(deep):
            self.df = df.copy(deep=True)
        else:
            self.df = df
        logger.info("DataClean method added!")
            
    def remove_unwnated_columns(self,cols):
        self.df.drop(cols,axis=1,inplace=True)
        logger.info("removing unwanted columns successful!")
        return self.df
    
    def remove_nulls(self) -> pd.DataFrame:
        logger.info("removing nulls successful!")
        return self.df.dropna()
       
    def remove_duplicates(self):
        rmv = self.df[self.df.duplicated()].index
        logger.info("removing duplicates successful!")
        return self.df.drop(index=rmv, inplace=True)

    def fix_outlier(self,cols):
        for col in cols:
            self.df[col] = np.where(self.df[col]>self.df[col].quantile(0.95),self.df[col].median(),self.df[col])
        logger.info("removing outliers successful!")
        return 
    def change_column_to_date_type(self, col_name):
        try:
            self.df[col_name] = pd.to_datetime(self.df[col_name])
        except:
            print('failed to change column to Date Type')
        logger.info(
            f"Successfully changed column {col_name} to DateType!")

