import mne
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
from src.params import PERF_PATH, BEHAV_PATH

def all_perf_data(perf_path) :

    '''TODO'''

    df_data = pd.DataFrame()
    for subj_perf in os.listdir(perf_path) :
        if '.csv' in subj_perf : 
            df_subj = pd.read_csv(perf_path + subj_perf)
            df_data = pd.concat([df_data, df_subj])
    df_data['nb_resp'] = 1   

    # Export table into csv
    df_data.to_csv(BEHAV_PATH + 'discrimination_performance.csv')
    return df_data

def plot_perf(df) : 

    '''TODO'''

    # TODO : Change variables to plot 
    # Plot differences between hit and false
    grouped_hit_false = df.groupby(['subID', 'response', 'active_laughType']).count()
    grouped_hit_false.boxplot(column = 'nb_resp', by = ['response'])
    plt.ylabel('Number of answer')
    plt.title('Overall performance')
    plt.savefig(BEHAV_PATH + 'discrimination_performance-hit-false.png')
    plt.show()

    # Plot differences between laughter type performance
    grouped_real_posed = df.groupby(['subID', 'response', 'active_laughType']).count()
    grouped_real_posed.boxplot(column = 'nb_resp', by = ['response', 'active_laughType'])
    plt.ylabel('Number of answer')
    plt.title('Performance for each type of laughter')
    plt.savefig(BEHAV_PATH + 'discrimination_performance-real-posed.png')
    plt.show()

    return grouped_hit_false, grouped_real_posed

if __name__ == '__main__' :

    # check if the path exists, if not, create it
    if not os.path.isdir(BEHAV_PATH):
        os.mkdir(BEHAV_PATH)
        print('BEHAV folder created at : {}'.format(BEHAV_PATH))
    else:
        print('{} already exists.'.format(BEHAV_PATH))

    df_data = all_perf_data(PERF_PATH)

    grouped_hit_false, grouped_real_posed = plot_perf(df_data)

