from typing_extensions import Self
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from log_helper import Logger_Class
logger_obj = Logger_Class("../logs/data_exploration.log").get_logger()

class Plots:
    def __init__(self) -> None:
        self.logger = Logger_Class("../logs/data_exploration.log").get_logger()
    def plot_hist(self,df: pd.DataFrame, column: str, color: str) -> None:
        plt.figure(figsize=(9, 7))
        sns.displot(data=df, x=column, color=color, kde=True, height=7, aspect=2)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
      
        plt.show()
        self.logger.info('Hist plot plotted!!!')
        

    def plot_dist(self,df: pd.DataFrame, column: str):
        plt.figure(figsize=(9, 7))
        sns.distplot(df).set_title(f'Distribution of {column}')
        plt.show()
        self.logger.info('Disti plot plotted!!!')


    def plot_count(self,df: pd.DataFrame, column: str) -> None:
        plt.figure(figsize=(12, 7))
        sns.countplot(data=df, x=column)
        plt.title(f'Plot count of {column}', size=20, fontweight='bold')
        plt.show()
        self.logger.info('Count plot plotted!!!')


    def plot_bar(self, df: pd.DataFrame, x_col: str, y_col: str, title: str, xlabel: str, ylabel: str) -> None:
        plt.figure(figsize=(9, 7))
        sns.barplot(data=df, x=x_col, y=y_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks(fontsize=14)
        plt.xlabel(xlabel, fontsize=16)
        plt.ylabel(ylabel, fontsize=16)
        plt.show()
        self.logger.info('bar plot plotted!!!')


    def plot_heatmap(self, df: pd.DataFrame, title: str, cbar=False) -> None:
        plt.figure(figsize=(12, 7))
        sns.heatmap(df, annot=True, cmap='viridis', vmin=0,
                vmax=1, fmt='.2f', linewidths=.7, cbar=cbar)
        plt.title(title, size=18, fontweight='bold')
        plt.show()
        self.logger.info('heat map plotted!!!')


    def plot_box(self, df: pd.DataFrame, x_col: str, title: str) -> None:
        plt.figure(figsize=(12, 7))
        sns.boxplot(data=df, x=x_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.show()
        self.logger.info('Box plot plotted!!!')


    def plot_box_multi(self,df: pd.DataFrame, x_col: str, y_col: str, title: str) -> None:
        plt.figure(figsize=(12, 7))
        sns.boxplot(data=df, x=x_col, y=y_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()


    def plot_scatter(self,df: pd.DataFrame, x_col: str, y_col: str, title: str, hue: str, style: str) -> None:
        plt.figure(figsize=(10, 8))
        sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, style=style)
        plt.title(title, size=20)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()
        self.logger('Scatter plot plotted!!!')
        
    def plot_heatmap_from_correlation(self,correlation, title: str):
        plt.figure(figsize=(14, 9))
        sns.heatmap(correlation)
        plt.title(title, size=18, fontweight='bold')
        plt.show()    
        self.logger('Correlation heat map plotted!!!')    
    