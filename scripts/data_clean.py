import pandas as pd
import numpy as np
from log_help import App_Logger 
app_logger = App_Logger('../logs/data_clean.log').get_app_logger()

class DataClean:
    def __init__(self,df,deep=False) -> None:
        self.logger = App_Logger(
            '../logs/data_clean.log').get_app_logger()
        if(deep):
            self.df = df.copy(deep=True)
        else:
            self.df = df
            
    def remove_unwnated_columns(self,cols):
        self.df.drop(cols,axis=1,inplace=True)
        return self.df
    
    def remove_nulls(self) -> pd.DataFrame:
        return self.df.dropna()
    
    def remove_duplicates(self):
        rmv = self.df[self.df.duplicated()].index
        return self.df.drop(index=rmv, inplace=True)

    def fix_outlier(Self,cols):
        for col in cols:
            self.df[col] = np.where(self.df[col]>self.df[col].quantile(0.95),self.df[col].median(),self.df[col])
