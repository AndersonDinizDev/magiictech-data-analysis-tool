import pandas as pd
import matplotlib.pyplot as plt

# 1. Coleta de Dados
def load_data(file_path):
    """
    Carrega dados de um arquivo CSV.
    Args:
    - file_path (str): Caminho para o arquivo CSV.
    
    Returns:
    - DataFrame: Dados carregados em um DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        print("Dados carregados com sucesso!")
        return data
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho do arquivo.")
        return None

# 2. Tratamento dos Dados
def clean_data(df):
    """
    Realiza limpeza básica dos dados.
    Args:
    - df (DataFrame): DataFrame com os dados carregados.
    
    Returns:
    - DataFrame: DataFrame com dados limpos.
    """
    # Remove linhas com valores nulos
    df_cleaned = df.dropna()
    # Converte colunas específicas para tipos apropriados (ajustar conforme os dados)
    if 'Date' in df_cleaned.columns:
        df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'])
    
    print("Dados limpos com sucesso!")
    return df_cleaned

# 3. Visualização dos Dados
def visualize_data(df):
    """
    Gera visualizações simples dos dados.
    Args:
    - df (DataFrame): DataFrame com os dados limpos.
    """
    # Exemplo: Gráfico de linhas para visualizar tendências de vendas ao longo do tempo
    if 'Date' in df.columns and 'Sales' in df.columns:
        plt.figure(figsize=(10, 5))
        plt.plot(df['Date'], df['Sales'], marker='o')
        plt.title('Tendências de Vendas ao Longo do Tempo')
        plt.xlabel('Data')
        plt.ylabel('Vendas')
        plt.grid()
        plt.show()
    else:
        print("Colunas necessárias ('Date', 'Sales') não encontradas no DataFrame.")

def main():
    # Caminho para o arquivo CSV (substituir com o caminho real)
    file_path = 'dados_empresa.csv'
    
    # Carregar dados
    df = load_data(file_path)
    
    if df is not None:
        # Limpar dados
        df_cleaned = clean_data(df)
        
        # Visualizar dados
        visualize_data(df_cleaned)

if __name__ == "__main__":
    main()
