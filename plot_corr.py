from scipy.stats import linregress
import numpy as np
import matplotlib.pyplot as plt

def regression_line(slope: float, intercept: float):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')

def plot_corr(x: list, y: list, plot_title = None, x_variable_name = 'X Variable', y_variable_name = 'Y Variable'):
    """Plot correlation between two variables of equal length"""

    # Use scipy.stats.linregress to calc correlation
    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    # Plotting variables
    ax = plt.subplot(111)
    ax.scatter(x,y)
    
    # Plotting regression line
    regression_line(slope,intercept)

    # Plot labelling
    r_value_round = round(r_value**2,3)
    p_value_round = round(p_value,3)
    subtitle_string = f'R-sq = {r_value_round}, p = {p_value_round}'
    if plot_title:
        full_title = (plot_title + '\n' + subtitle_string)
        plt.title(full_title)
    else:
        plt.title(subtitle_string)
    plt.xlabel(x_variable_name, fontsize=14)
    plt.ylabel(y_variable_name, fontsize=14)

    # Various plot beautification
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.setp(ax.get_xticklabels(), fontsize=14)
    plt.setp(ax.get_yticklabels(), fontsize=14)

    plt.show()