import pandas as pd
import matplotlib.pyplot as plt

# Creating a sample DataFrame
data = {'Country': ['INDIA', 'SRI_LANKA', 'PAKISTAN', 'JAPAN', 'CHINA'],
        'Population': [3282000000, 3759000, 831400000, 12680000, 669900000],
        'GDP': [21427753, 1760623, 3980119, 5154471, 2928246]
        }
df = pd.DataFrame(data)

# Creating a bar chart of population
df.plot(x='Country', y='Population', kind='bar', legend=False)
plt.xlabel('Country')
plt.ylabel('Population (in millions)')
plt.title('Population by Country')
plt.show()

# Create a scatter plot of population vs. GDP
df.plot(x='Population', y='GDP', kind='scatter')
plt.xlabel('Population')
plt.ylabel('GDP')
plt.title('Population vs. GDP')
plt.show()
