'''
Import necessary libraries to creates functions for churn model
'''

import pandas as pd
import dataframe_image as dfi
from matplotlib import pyplot as plt
import sys
from pylab import *
import seaborn as sns; sns.set()

def import_data(pth):
    '''
    returns dataframe for the csv found at pth

    input:
            pth: a path to the csv
    output:
            df: pandas dataframe
    '''
    return pd.read_csv(pth)


def perform_eda(df):
    '''
    perform eda on df and save figures to images folder
    input:
            df: pandas dataframe

    output:
            Missing counts by column: (.png) missing_counts_by_column.png
            Descriptive statistics per column: (.png) descriptive_stats_by_column.png
            x and y variables: (.png)
            cont. and count variable heatmap: (.png)
    '''

    ## missing counts save as image
    df_missing_counts = df.isnull().sum().reset_index()
    df_missing_counts.columns = ['column_name', 'missing_count']
    df_missing_counts['%'] = df_missing_counts.missing_count / len(df)
    dfi.export(df_missing_counts, r'./images/eda/missing_counts_by_column.png')

    ## descriptive stats by column saved as image
    dfi.export(df.describe(), r'./images/eda/descriptive_stats_by_column.png')

    ## barplot of y_variable = Churn
    df['Churn'] = df['Attrition_Flag'].apply(lambda val: 0 if val == "Existing Customer" else 1)
    df_churn = df.groupby('Churn').size().reset_index()
    df_churn['%'] = round(df_churn[0] * 100 / df_churn[0].sum(), 2)
    plt = df_churn.plot.bar(x='Churn',
                            y='%',
                            rot=0,
                            legend=False,
                            title='Churn Distribution (1 = yes, 2 = no)')
    plt.set_ylabel("Percent")
    plt.figure.savefig('./images/eda/y_churn_barplot.png')

    cat_columns = [
        'Gender',
        'Education_Level',
        'Marital_Status',
        'Income_Category',
        'Card_Category'
    ]
    count_columns = ['Dependent_count',
                     'Total_Relationship_Count',
                     'Months_Inactive_12_mon',
                     'Contacts_Count_12_mon'
                     ]
    ## Barplots of categorical variables
    for var in cat_columns:
        df_var = df.groupby(var).size().reset_index()
        df_var['%'] = round(df_var[0] * 100 / df_var[0].sum(), 2)
        plt = df_var.plot.bar(x=var, y='%', rot=45, legend=False, title=var + ' Distribution')
        plt.set_ylabel("Percent")
        plt.figure.savefig('./images/eda/X_{}_barplot.png'.format(var))

    cont_columns = ['Customer_Age',
                    'Months_on_book',
                    'Credit_Limit',
                    'Total_Revolving_Bal',
                    'Avg_Open_To_Buy',
                    'Total_Amt_Chng_Q4_Q1',
                    'Total_Trans_Amt',
                    'Total_Trans_Ct',
                    'Total_Ct_Chng_Q4_Q1',
                    'Avg_Utilization_Ratio'
    ]
    ## Distribution of continuous variables
    for var in cont_columns:
        img = sns.displot(df[var])
        img.savefig('./images/eda/X_{}_distribution.png'.format(var))

    ## get heatmap (correlation)
    sns.set(rc={'figure.figsize': (15, 8)})
    img = sns.heatmap(df[df.columns[1:]].corr(), annot=False, cmap='Dark2_r', linewidths = 2)
    fig = img.get_figure()
    fig.savefig('./images/eda/X_variable_heatmap.png')


def encoder_helper(df, category_lst, response):
    '''
    helper function to turn each categorical column into a new column with
    proportion of churn for each category - associated with cell 15 from the notebook

    input:
            df: pandas dataframe
            category_lst: list of columns that contain categorical features
            response: string of response name [optional argument that could be used for naming variables or index y column]

    output:
            df: pandas dataframe with new columns for
    '''
    pass


def perform_feature_engineering(df, response):
    '''
    input:
              df: pandas dataframe
              response: string of response name [optional argument that could be used for naming variables or index y column]

    output:
              X_train: X training data
              X_test: X testing data
              y_train: y training data
              y_test: y testing data
    '''

def classification_report_image(y_train,
                                y_test,
                                y_train_preds_lr,
                                y_train_preds_rf,
                                y_test_preds_lr,
                                y_test_preds_rf):
    '''
    produces classification report for training and testing results and stores report as image
    in images folder
    input:
            y_train: training response values
            y_test:  test response values
            y_train_preds_lr: training predictions from logistic regression
            y_train_preds_rf: training predictions from random forest
            y_test_preds_lr: test predictions from logistic regression
            y_test_preds_rf: test predictions from random forest

    output:
             None
    '''
    pass


def feature_importance_plot(model, X_data, output_pth):
    '''
    creates and stores the feature importances in pth
    input:
            model: model object containing feature_importances_
            X_data: pandas dataframe of X values
            output_pth: path to store the figure

    output:
             None
    '''
    pass

def train_models(X_train, X_test, y_train, y_test):
    '''
    train, store model results: images + scores, and store models
    input:
              X_train: X training data
              X_test: X testing data
              y_train: y training data
              y_test: y testing data
    output:
              None
    '''
    pass