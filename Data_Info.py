def description(dataframe):
    print(f'-----The datatframe shape is as follows:-----\n')
    print(f'{dataframe.shape} \n')

    print(f'-----The summary for the dataframe is as follows:-----\n')
    print(f'{dataframe.info()} \n')

    print(f'-----The descriptive statistics for the dataframe are as follows:-----\n')
    print(f'{dataframe.describe()} \n')

def cleaning(dataframe):
    print(f'----Missing Values----\n')
    print(f'{dataframe.isna().sum().sort_values(ascending=False)} \n')

    print(f'----Duplicate Values----\n')
    print(f'{dataframe.duplicated().value_counts()} \n')