import utils
import read_csv
import charts
import pandas as pd

def run():
  # Manual
  '''
  data = read_csv.read_csv('./data.csv')

  country = input('Type country: ')
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values, country['Country/Territory'])

  data = list(filter(lambda item : item['Continent'] == 'South America', data))

  countries = list(map(lambda x : x['Country/Territory'], data))
  percentages = list(map(lambda x : x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  '''

  # Pandas
  df = pd.read_csv('./data.csv') # df = dataframe, lectura del CSV
  df = df[df['Continent'] == 'Africa'] # Filtrado de paises en Sur America

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values

  charts.generate_pie_chart(countries, percentages)

    
if __name__ == '__main__':
  run()