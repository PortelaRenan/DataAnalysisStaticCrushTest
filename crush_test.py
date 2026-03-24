# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools 
import statistics
from itertools import combinations
from scipy.stats import ttest_ind

# Functions
def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df[['Displacement_[mm]', 'Force_1_[N]', 'Force_2_[N]', 'Force_3_[N]']]
    df['Force_[N]'] = df[['Force_1_[N]', 'Force_2_[N]', 'Force_3_[N]']].sum(axis = 1).abs()
    df = df[df['Force_[N]'] > 200].reset_index()
    df['Displacement_[mm]'] = df['Displacement_[mm]'] - df['Displacement_[mm]'][0]
    return df[~((df['Displacement_[mm]'] > 10) & (df['Force_[N]'] < 3e3))].reset_index()

def interpolate_dataframe(*df: pd.DataFrame) -> pd.DataFrame:
    displacement = np.arange(0, 100.2, 0.2)
    interpolated_df = pd.DataFrame(displacement, columns=['Displacement [mm]'])
    for index, df_values in enumerate(df):
        interpolated_values = np.interp(displacement, df_values['Displacement_[mm]'],
                                        df_values['Force_[N]'])  
        interpolated_df[f'Sample_0{index+1}'] = interpolated_values/1e3
    return interpolated_df

def plot_crush(df: pd.DataFrame) -> None:
    samples = [f'Sample_0{index+1}' for index in range(len(df.columns) - 1)]
    ax = df.plot(x='Displacement [mm]', y=samples, figsize=(10, 6), kind="line",
                 color='red', fontsize = 30)
    df['Median'] = df[samples].median(axis = 1)
    df.plot(x='Displacement [mm]', y='Median', figsize=(10, 6), kind="line",
            color='black', ax=ax, fontsize = 30)
    plt.xlabel('Displacement [mm]', fontsize = 30)
    plt.ylabel('Force [kN]', fontsize = 30)
    plt.grid(True)
    plt.tight_layout()
    plt.xlim([0,100])
    plt.ylim([0,70])
    plt.show()
    
def comparable_plot(array_df: list[pd.DataFrame]) -> None:
    fig, ax = plt.subplots(1, 3, figsize=(20, 8), sharey = True, sharex = True)
    
    for index, df in enumerate(array_df):
        current_ax = ax[index]
        samples = [col for col in df.columns if col.startswith("Sample_")]

        # Plot all samples in grey with the same label (only first gets label)
        for i, sample in enumerate(samples):
            df.plot(x='Displacement [mm]', y=sample, ax=current_ax,
                    color='grey', linewidth=1,
                    label='Sample' if i == 0 else "", legend=False, fontsize = 30)
            
        # Plot the median in black
        df['Median'] = df[samples].median(axis=1)
        df.plot(x='Displacement [mm]', y='Median', ax=current_ax,
                color='black', linewidth=2, label='Median', legend = False, fontsize = 30)

        # Formatting
        current_ax.set_xlabel('Displacement [mm]', fontsize=30)
        titles = ['(a) UNB', '(b) AT', '(c) VAC 20 s']
        current_ax.set_title(titles[index], fontsize=25)

        if index == 0:
            current_ax.set_ylabel('Force [kN]', fontsize=30)
        current_ax.grid(True)
        plt.xlim([0,100])
        plt.ylim([0,70])
    
    # Create shared legend
    handles, labels = ax[0].get_legend_handles_labels()
    fig.legend(handles, labels,
               loc='upper left',
               bbox_to_anchor=(0.85, 1.05),  # Just outside the last plot
               frameon=True, fontsize=25)
    
    plt.tight_layout(rect=[0, 0, 1, 0.9])  # Leave space for the legend
    plt.show()

def energy_comparison(array_df: list[pd.DataFrame]) -> None:
    
    ax = plt.subplot()
    labels = iter(['UNB', 'AT', 'VAC 20 s'])
    colors = iter(['red', 'green', 'blue'])
    markers = iter(['s', 'o', '^'])
    
    for df in array_df:
        samples = [f'Sample_0{index+1}' for index in range(len(df.columns) - 2)]
        df['Median'] = df[samples].mean(axis = 1)
        energy = [df['Median'][i:i+2].mean()*0.2/1e3 for i in range(len(df['Median']) - 1)]
        df['Total Energy [kJ]'] = [sum(energy[:i]) for i in range(len(df['Median']))]
        
        df.plot(x='Displacement [mm]', y='Total Energy [kJ]', figsize=(10, 6), kind="line",
                ax = ax, color = next(colors), label = next(labels), marker = next(markers),
                markevery = 50, fontsize = 30)
    
    
    
    plt.xlabel('Displacement [mm]', fontsize = 30)
    plt.ylabel('Energy [kJ]', fontsize = 30)
    plt.legend(fontsize = 25)
    plt.grid(True)
    plt.xlim([0,100])
    plt.ylim([0,5])
    plt.show()
    
def bar_crush_plots(*df: pd.DataFrame) -> None:  
    x_labels = ['UNB', 'AT', 'VAC 20 s', 'HP-RTM']
    means = []
    errors = []

    
    for df_aux in df:
        df_filtered = df_aux[df_aux['Displacement [mm]'] <= 10]
        max_vals = df_filtered[['Sample_01', 'Sample_02', 'Sample_03', 'Sample_04']].max().to_list()
        mean_val = statistics.mean(max_vals)
        std_dev = statistics.stdev(max_vals)
        print(f"mean = {mean_val:.2f}, std = {std_dev:.2f}")


        means.append(mean_val)
        errors.append(std_dev)
        
    fig, ax = plt.subplots(1, 4, figsize=(32, 8), sharex=True)
    ax[0].bar(x_labels, means, yerr=errors, capsize=15, color='skyblue')
    ax[0].set_title("(a) Peak Crush Force", fontsize = 30)
    ax[0].set_ylabel("Force [kN]", fontsize = 30)
    ax[0].tick_params(axis='both', labelsize=25)  
    ax[0].set_ylim([0,70])   
    ax[0].grid(True)
    
    
    mean_force = []
    
    for df_aux in df:
        energy = df_aux[['Total Energy [kJ]']].max().iloc[0]
        mean_force.append(energy/0.1)
   
    ax[1].bar(x_labels, mean_force, color='skyblue')
    ax[1].set_title("(b) Mean Crush Force", fontsize = 30)
    ax[1].set_ylabel("Force [kN]", fontsize = 30)
    ax[1].tick_params(axis='both', labelsize=25)  
    ax[1].set_ylim([0,70])      
    ax[1].grid(True)
    
    crush_efficiency = [i/j*100 for i, j in zip(mean_force, means)]
    
    ax[2].bar(x_labels, crush_efficiency, color='skyblue')
    ax[2].set_title("(c) Crush Force Efficiency", fontsize = 30)
    ax[2].set_ylabel("[%]", fontsize = 30)
    ax[2].tick_params(axis='both', labelsize=25)  
    ax[2].set_ylim([0,100])      
    ax[2].grid(True)
    
    mass = [0.083651, 0.084662, 0.084494, 0.08629989212513484]
    specific_energy = []
    i = 0
    
    for df_aux in df:
        energy = df_aux[['Total Energy [kJ]']].max().iloc[0]
        specific_energy.append(energy/mass[i])
        
        i += 1
    print(specific_energy)
    ax[3].bar(x_labels, specific_energy, color='skyblue')
    ax[3].set_title("(d) Specific Energy Absorption", fontsize = 30)
    ax[3].set_ylabel("Energy [kJ/kg]", fontsize = 30)
    ax[3].tick_params(axis='both', labelsize=25)  
    ax[3].set_ylim([0,70])      
    ax[3].grid(True)

    plt.tight_layout()
    plt.show()
    

def pairwise_t_tests(*df: pd.DataFrame, x_labels=None) -> pd.DataFrame:
    """
    Conducts pairwise t-tests on maximum values (Sample_01 to Sample_04)
    for each dataframe, filtered where Displacement <= 10 mm.

    Parameters:
    ----------
    *df : pd.DataFrame
        Variable number of dataframes containing sample columns and 'Displacement [mm]'.
    x_labels : list of str, optional
        Names corresponding to each dataframe (for labeling results).

    Returns:
    -------
    pd.DataFrame
        A summary dataframe with t-statistics and p-values for each pairwise comparison.
    """
    if x_labels is None:
        x_labels = [f"Group_{i+1}" for i in range(len(df))]

    max_values_list = []

    # Extract maximum values per dataset
    for df_aux in df:
        df_filtered = df_aux[df_aux['Displacement [mm]'] <= 10]
        max_vals = df_filtered[['Sample_01', 'Sample_02', 'Sample_03', 'Sample_04']].max().to_list()
        max_values_list.append(max_vals)

    # Run pairwise t-tests
    results = []
    for (i, j) in combinations(range(len(max_values_list)), 2):
        t_stat, p_val = ttest_ind(max_values_list[i], max_values_list[j], equal_var=False)
        results.append({
            'Group 1': x_labels[i],
            'Group 2': x_labels[j],
            'p-value': round(p_val, 4)
        })

    results_df = pd.DataFrame(results)
    print("\nPairwise t-tests (based on maximum values up to 10 mm displacement):")
    print(results_df)
    return results_df


# UNB
unb_01 = pd.read_csv(r'[2] UNB/UNB-01-01.csv')
unb_01 = filter_dataframe(unb_01)

unb_02 = pd.read_csv(r'[2] UNB/UNB-04-01.csv')
unb_02 = filter_dataframe(unb_02)

unb_03 = pd.read_csv(r'[2] UNB/UNB-05-01.csv')
unb_03 = filter_dataframe(unb_03)

unb_04 = pd.read_csv(r'[2] UNB/UNB-04-02.csv')
unb_04 = filter_dataframe(unb_04)

df_unb = interpolate_dataframe(unb_01, unb_02, unb_03, unb_04)


# AT
at_01 = pd.read_csv(r'[1] AT/AT-01-01.csv')
at_01 = filter_dataframe(at_01)

at_02 = pd.read_csv(r'[1] AT/AT-01-02.csv')
at_02 = filter_dataframe(at_02)

at_03 = pd.read_csv(r'[1] AT/AT-02-01.csv')
at_03 = filter_dataframe(at_03)

at_04 = pd.read_csv(r'[1] AT/AT-02-02.csv')
at_04 = filter_dataframe(at_04)

df_at = interpolate_dataframe(at_01, at_02, at_03, at_04)

# VAC 20 s
vac_01 = pd.read_csv(r'[3] VAC 20s/VAC 20-01-01.csv')
vac_01 = filter_dataframe(vac_01)

vac_02 = pd.read_csv(r'[3] VAC 20s/VAC 20-01-02.csv')
vac_02 = filter_dataframe(vac_02)

vac_03 = pd.read_csv(r'[3] VAC 20s/VAC 20-02-01.csv')
vac_03 = filter_dataframe(vac_03)

vac_04 = pd.read_csv(r'[3] VAC 20s/VAC 20-02-02.csv')
vac_04 = filter_dataframe(vac_04)

df_vac = interpolate_dataframe(vac_01, vac_02, vac_03, vac_04)

d = {'Displacement [mm]': [0], 'Sample_01': [65.41], 'Sample_02': [65.41], 
     'Sample_03': [65.41], 'Sample_04': [65.41], 'Total Energy [kJ]': [5.6],
     'Specific Energy Absorption [kJ/kg]': [64.89]}
df_hp_rtm = pd.DataFrame(data = d)

comparable_plot([df_unb, df_at, df_vac])
energy_comparison([df_unb, df_at, df_vac])
bar_crush_plots(df_unb, df_at, df_vac, df_hp_rtm)

pairwise_t_tests(df_unb, df_at, df_vac)