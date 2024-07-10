import pandas as pd
import statistics as stats
import matplotlib.pyplot as plt

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        data['idade'] = pd.to_numeric(data['idade'], errors='coerce')
        data.dropna(subset=["idade"], inplace=True)
        data = data[data["idade"] <= 100]
        return data
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return None

def calculate_statistics(data):
    statistics = {}
    
    # Funções auxiliares
    def calculaMedia(arraydeidade):
        return round(stats.mean(arraydeidade), 1)
    
    def calculaQuartis(arraydeidades):
        arraySorted = sorted(arraydeidades)
        n = len(arraySorted)
        indexQ1 = int(0.25 * n)
        indexQ3 = int(0.75 * n)
        Q1 = arraySorted[indexQ1]
        Q3 = arraySorted[indexQ3]
        return Q3 - Q1

    def skewness(arraydeidade):
        n = len(arraydeidade)
        mu = stats.mean(arraydeidade)
        sigma = stats.stdev(arraydeidade)
        return (n * sum(((x - mu) / sigma) ** 3 for x in arraydeidade)) / ((n - 1) * (n - 2))
    
    # Cálculos gerais
    statistics['Geral'] = {
        'Media': calculaMedia(data['idade']),
        'Mediana': stats.median(data['idade']),
        'Moda': stats.mode(data['idade']),
        'Desvio Padrão': stats.stdev(data['idade']),
        'Variância': stats.variance(data['idade']),
        'Quartil': calculaQuartis(data['idade']),
        'Assimetria': skewness(data['idade'])
    }
    
    # Cálculos por gênero
    for gender in ['MASCULINO', 'FEMININO', 'OUTROS']:
        gender_data = data[data['sexo'] == gender]['idade'].astype(int)
        statistics[gender] = {
            'Media': calculaMedia(gender_data),
            'Mediana': stats.median(gender_data),
            'Moda': stats.mode(gender_data),
            'Desvio Padrão': stats.stdev(gender_data),
            'Variância': stats.variance(gender_data),
            'Quartil': calculaQuartis(gender_data),
            'Assimetria': skewness(gender_data)
        }
    
    return statistics

def plot_histogram(data, title):
    plt.hist(data, bins=20, edgecolor='black')
    plt.title(title)
    plt.xlabel('Idade')
    plt.ylabel('Frequência')
    plt.show()

if __name__ == "__main__":
    data = load_data("table.csv")
    if data is not None:
        stats = calculate_statistics(data)
        for key, value in stats.items():
            print(f"{key}: {value}")
        
        #Retire os comentários "#" para exibir o histograma
        #plot_histogram(data['idade'], 'Distribuição de Idades Geral')
        #plot_histogram(data[data['sexo'] == 'MASCULINO']['idade'], 'Distribuição de Idades - Masculino')
        #plot_histogram(data[data['sexo'] == 'FEMININO']['idade'], 'Distribuição de Idades - Feminino')
        #plot_histogram(data[data['sexo'] == 'OUTROS']['idade'], 'Distribuição de Idades - Outros')
