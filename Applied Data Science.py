import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def extract_data(filename, countries, indicator):
    # Read the CSV file and skip the first 4 rows
    data_frame = pd.read_csv(filename, skiprows=(4), index_col=False)

    # Remove columns with '^Unnamed' in their name
    data_frame = data_frame.loc[:, ~
                                data_frame.columns.str.contains('^Unnamed')]

    # Filter data only for the countries specified in the 'countries' parameter
    data_frame = data_frame.loc[data_frame['Country Name'].isin(countries)]

    # Filter data only for the indicator specified in the 'indicator' parameter
    data_frame = data_frame.loc[data_frame['Indicator Code'].eq(indicator)]

    # Melt the data frame to pivot and store the resulting data frame in 'df2'
    df2 = data_frame.melt(id_vars=['Country Name', 'Country Code',
                                   'Indicator Name', 'Indicator Code'], var_name='Years')

    # Remove the 'Country Code' column
    del df2['Country Code']

    # Pivot the data frame and reset the index
    df2 = df2.pivot_table('value', [
                          'Years', 'Indicator Name', 'Indicator Code'], 'Country Name').reset_index()

    # Create two data frames from the filtered data: one for countries and one for years
    df_countries = data_frame
    df_years = df2

    # Remove any rows with missing values in both data frames
    df_countries.dropna()
    df_years.dropna()

    # Return the two data frames
    return df_countries, df_years


# Define the list of countries to be included in the analysis
countries = ['India', 'Australia',
             'Israel', 'China', 'United Kingdom']

# Call the 'extract_data' function to filter the data for the specified countries and indicator
df_c, df_y = extract_data(
    'data.csv', countries, 'AG.LND.FRST.ZS')

# Create an array of numbers from 0 to 4
num = np.arange(5)

# Set the width of each bar in the bar graph
width = 0.15

# Filter the data for the years 1990, 1995, 2000, 2005, and 2010
df_y = df_y.loc[df_y['Years'].isin(['1990', '1995', '2000', '2005', '2010'])]

# Create a list of years from the filtered data
years = df_y['Years'].tolist()

# Print the first 5 rows of the filtered data
print(df_y.head(5))

# Set the figure size and create a bar graph
plt.figure(dpi=144)
plt.title('Forest area (% of land area)')
plt.bar(num, df_y['India'], width, label='India', color='darkseagreen')
plt.bar(num+0.2, df_y['Australia'], width, label='Australia', color='teal')
plt.bar(num-0.2, df_y['Israel'], width,
        label='Israel', color='darkkhaki')
plt.bar(num-0.4, df_y['China'], width, label='China', color='khaki')
plt.xticks(num, years)
plt.xlabel('Years')
plt.ylabel('% of land area')
plt.legend(loc='best')
plt.show()


# Define the list of countries to be included in the analysis
countries = ['India', 'Australia',
             'Israel', 'China', 'United Kingdom']

# Call the 'extract_data' function to filter the data for the specified countries and indicator
df_c, df_y = extract_data(
    'data.csv', countries, 'AG.LND.AGRI.ZS')

# Create an array of numbers from 0 to 4
num = np.arange(5)

# Set the width of each bar in the bar graph
width = 0.15

# Filter the data for the years 1990, 1995, 2000, 2005, and 2010
df_y = df_y.loc[df_y['Years'].isin(['1990', '1995', '2000', '2005', '2010'])]

# Create a list of years from the filtered data
years = df_y['Years'].tolist()

# Print the first 5 rows of the filtered data
print(df_y.head(5))

# Set the figure size and create a bar graph
plt.figure(dpi=144)
plt.title('Agricultural land (% of land area)')
plt.bar(num, df_y['India'], width, label='India', color='darkseagreen')
plt.bar(num+0.2, df_y['Australia'], width, label='Australia', color='teal')
plt.bar(num-0.2, df_y['Israel'], width,
        label='Israel', color='darkkhaki')
plt.bar(num-0.4, df_y['China'], width, label='China', color='khaki')
plt.xticks(num, years)
plt.xlabel('Years')
plt.ylabel('% of land area')
plt.legend(loc='best')
plt.show()
