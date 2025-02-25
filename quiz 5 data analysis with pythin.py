import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Get data
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.scatter(x, y)

    # Create first line of best fit
    slope, intercept, _, _, _  = linregress(x, y)

    # Create new x values for the extended range (1880 to 2050)
    x_extended = range(1880, 2051)  # This will create values from 1880 to 2050

    # Calculate the corresponding y values for the extended x values
    y_extended = [slope * year + intercept for year in x_extended]

    # Plot the extended best-fit line
    plt.plot(x_extended, y_extended, color='cyan', label='Best-fit line (2050)')

    # Create second line of best fit
    x_latest = df[df['Year'] >= 2000]['Year']
    y_latest = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
    slope_latest, intercept_latest, _, _, _  = linregress(x_latest, y_latest)

    # Create new x values for 2000 to 2050
    x_latest_extended = range(2000, 2051)

    # Calculate correspondng y values for 2000 to 2050
    y_latest_extended = [slope_latest * year + intercept_latest for year in x_latest_extended]
    
    # Plot the latest best-fit line
    plt.plot(x_latest_extended, y_latest_extended, color='magenta', label='Best-fit line (2000 - 2050)')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()