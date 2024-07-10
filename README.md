# analysispy
Análise das idades e distribuição por gênero das pessoas vacinadas em Recife, PE. Inclui scripts em Python para calcular estatísticas descritivas e gerar visualizações gráficas.

## Estrutura do Projeto

analysispy/
│
├── app.py
├── histograma.py
├── figures
├── table.csv
├── README.md
└── requirements.txt

## Requisitos

- Python 3.6 ou superior
- pandas
- matplotlib

## Instalação

1. Clone o repositório

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

### 1. Análise das Idades (`app.py`)

Este script calcula e exibe estatísticas descritivas das idades das pessoas vacinadas e gera histogramas para visualizar a distribuição das idades.

```bash
python app.py
```
##Exemplo de saída:
```
Geral: {'Media': 45.2, 'Mediana': 44.0, 'Moda': 45, 'Desvio Padrão': 15.1, 'Variância': 228.9, 'Quartil': 20, 'Assimetria': 0.67}
MASCULINO: {'Media': 44.8, 'Mediana': 44.0, 'Moda': 45, 'Desvio Padrão': 14.9, 'Variância': 222.0, 'Quartil': 19, 'Assimetria': 0.65}
FEMININO: {'Media': 45.5, 'Mediana': 45.0, 'Moda': 46, 'Desvio Padrão': 15.3, 'Variância': 234.1, 'Quartil': 21, 'Assimetria': 0.68}
OUTROS: {'Media': 46.0, 'Mediana': 46.0, 'Moda': 46, 'Desvio Padrão': 15.5, 'Variância': 240.3, 'Quartil': 22, 'Assimetria': 0.70}
```

### 2. Análise do histograma (`histograma.py`)
Este script exibe o histograma com os resultados da distribuição das idades e dos gêneros

```bash
python histograma.py
```
##Exemplo de Gráfico:
Resultados
Distribuição das Idades:
Distribuição dos Sexos:



Este projeto está licenciado sob a licença MIT.


