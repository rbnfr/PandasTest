
#%%
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import pprint as pp
import seaborn as sns

#%%
def main():
#%%
    excel_input = pd.read_excel('./excels/export2021716.xlsx', header=6, usecols=[1,2,3])
    excel_input.columns = excel_input.iloc[0]
    excel_dict = excel_input.to_dict()
    printer = pp.PrettyPrinter
    concepto = str()
    total_cost = dict()
    subjects = {
        'Netflix'  : ['Netflix'],
        'Rent'     : 'Alquiler',
        'Amazon'   : ['Amzn', 'Amazon'],
        'Internet' : 'Cableworld',
        'Water'    : 'Emuasa',
        'Card'     : 'Contactless',
        'JustEat'  : 'just-eat',
        'Online'   : 'Compra Internet',
        'Light'    : 'Iberdrola',
        'Gym'      : 'Befitlive',
        # 'Bizum'    : 'Bizum',
        'Jiu-Jitsu': 'Judo'
    }
    # pp.pprint(excel_dict)
    for index in excel_dict.keys():
        for row in excel_dict[index].keys():
            if index == 'CONCEPTO':
                concepto = str(excel_dict[index][row])
                cost = excel_dict['IMPORTE EUR'][row]
                for subject in subjects.keys():
                    if isinstance(subjects[subject], list):
                        for needle in subjects[subject]:
                            if concepto.find(needle) != -1:
                                total_cost[subject] = total_cost.get(subject, 0) - cost
                        else:
                            if isinstance(cost, int):
                                total_cost['Others'] = total_cost.get('Others', 0) - 0
                    else:
                        if concepto.find(subjects[subject]) != -1:
                            total_cost[subject] = total_cost.get(subject, 0) - cost
                        else:
                            if isinstance(cost, int):
                                total_cost['Others'] = total_cost.get('Others', 0) - 0 
    
    money_np_array = pd.DataFrame(list(total_cost.items()))
    money_np_array = money_np_array.sort_values([1]).reset_index(drop=True)
    money_np_array_T = money_np_array.T
    money_np_array_T.columns = money_np_array_T.iloc[0]
    money_np_array_T.drop(
        labels = 0,
        axis = 0,
        inplace = True        
        )

    # plt.hist(x = subjects.keys() ,data=money_np_array_T.values)
    # plt.show()

    barplot = sns.barplot(
        data=money_np_array_T
        )
    barplot.set(xlabel = 'Categories', ylabel='€')
    
    for i in range(len(money_np_array_T.columns)):
        column_name = money_np_array_T.columns[i]
        column_data_value = money_np_array_T[column_name].values[0]
        barplot.text(
            x = i,
            y = column_data_value+150, 
            s = str(round(column_data_value,2))+'€', 
            color = 'black', 
            ha = "center"
            )
    
#%%
if __name__ == '__main__':
    main()
