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

    