#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean the data
df_clean = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    # Copy the cleaned data
    df_line = df_clean.copy()

    # Create a new column for Year-Month
    df_line['year'] = df_line.index.year
    df_line['month'] = df_line.index.month
    df_line['month'] = df_line['month'].replace({1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 
                                                 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 
                                                 11: 'Nov', 12: 'Dec'})

    # Group by date and calculate the mean
    df_line = df_line.groupby([df_line.index.year, df_line.index.month]).mean()
    df_line.index.rename(['year', 'month'], inplace=True)
    
    # Plotting
    fig, ax = plt.subplots(figsize=(14, 6))
    df_line['value'].plot(ax=ax, legend=False)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.grid(True)
    
    # Save plot to file
    plt.savefig('line_plot.png')
    
    # Return the plot
    return fig

def draw_bar_plot():
    # Copy the cleaned data
    df_bar = df_clean.copy()

    # Create a new column for Year-Month
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_bar['month'] = df_bar['month'].replace({1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 
                                               6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 
                                               11: 'Nov', 12: 'Dec'})
    
    # Group by year and month and calculate the mean
    df_bar = df_bar.groupby(['year', 'month']).mean()
    df_bar = df_bar.unstack()
    df_bar.columns = df_bar.columns.droplevel()
    
    # Plotting
    fig, ax = plt.subplots(figsize=(14, 10))
    df_bar.plot(kind='bar', ax=ax)
    ax.set_title('Average Page Views per Year by Month')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax.grid(True)
    
    # Save plot to file
    plt.savefig('bar_plot.png')
    
    # Return the plot
    return fig

def draw_box_plot():
    # Copy the cleaned data
    df_box = df_clean.copy()

    # Create a new column for Year-Month and reset index
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month
    df_box['month'] = df_box['month'].replace({1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 
                                               6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 
                                               11: 'Nov', 12: 'Dec'})
    df_box.reset_index(inplace=True)
    
    # Plotting
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))
    
    # Year-wise Box Plot (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Month-wise Box Plot (Seasonality)
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 
                                                                     'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 
                                                                     'Nov', 'Dec'])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    # Save plot to file
    plt.savefig('box_plot.png')
    
    # Return the plot
    return fig

if __name__ == '__main__':
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()

