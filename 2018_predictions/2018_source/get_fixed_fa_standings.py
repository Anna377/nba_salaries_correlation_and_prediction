import pandas as pd
import re

def joinTables(FA_names, average_salary):

    name_col = (FA_names['first name'] + FA_names['last name']).str.lower()
    for i in range(len(name_col)):
        new_name = re.sub("[^a-zA-Z]+", "", name_col[i])
        if new_name.endswith('jr'):
            new_name = new_name[:-2]
        name_col[i] = new_name
    FA_names.insert(0, 'name', name_col)
    return FA_names.merge(average_salary, how = 'inner', on = ['last name', 'first name'])

def create_csv():
    for i in ['2018']:
        fa_csv_name = "/Users/annamartirosyan/PycharmProjects/NBA_salaries/2018_predictions/2018_source/2018_free_agents_list.csv"
        average_csv_name = '/Users/annamartirosyan/PycharmProjects/NBA_salaries/data/salary_data/fixed_fa_signings/2017.csv'
        faNames = pd.read_csv(fa_csv_name)
        averageSalary = pd.read_csv(average_csv_name)
        combined = joinTables(faNames, averageSalary)
        combined.to_csv("/Users/annamartirosyan/PycharmProjects/NBA_salaries/2018_predictions/2018_source/fixed_"+ i + '.csv')

create_csv()
