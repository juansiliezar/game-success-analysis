# %%
import numpy as np
import pandas as pd
import plotly.express as px

# %%
man_in_contract = pd.read_csv('/Users/juansiliezar/data-sweeper/data/Manhattan In Contract - Nov 23 - report generated at 12_31pm on 2023-12-01 (1).csv')
man_sold = pd.read_csv('/Users/juansiliezar/data-sweeper/data/Manhattan Sold - Nov 23 - report generated at 12_18pm on 2023-12-01 (1).csv')
bk_nov = pd.read_csv('/Users/juansiliezar/data-sweeper/data/Brooklyn - Nov 23 - report generated at 12_22pm on 2023-12-01.csv')

# %%
class DataSweeper():
    
    def __init__(self, df):
        """
        Constructor for the DataCleaner class.

        Params:
            df: A Pandas DataFrame that needs to be cleaned.
        """
        # Ensuring the input is a DataFrame
        if not isinstance(df, pd.DataFrame):
            raise ValueError('Argument must be a Pandas DataFrame')
        
        # Storing the DataFrame in an instance variable otherwise
        self.df = df.copy() # creating copy to avoid modifying the original DF
        
    def clean_columns(self):
        """
        This method cleans the column names of the dataset

        Returns:
            DataFrame: A Pandas DataFrame with columns names that are
            stripped of whitespace, lowercase, and snake_case
        """
        # Accessing DF with "self.df" & formatting the column names
        clean_columns = self.df.columns \
            .str.strip() \
            .str.lower() \
            .str.replace(' ', '_') 
        
        # Checking that column names are formatted properly                         
        if list(self.df.columns) != list(clean_columns):
            self.df.columns = clean_columns
        else:
            pass
        
        return self.df

# %%
if __name__ == "__main__":
    DataSweeper()

# %%
