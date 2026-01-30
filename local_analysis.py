# scripts/local_analysis.py
"""Análise local simples (EDA) para o dataset fornecido.
Requer: pandas
Uso:
    python scripts/local_analysis.py
"""
import pandas as pd
from pathlib import Path

base = Path(__file__).resolve().parents[2]
data_path = base / "datasets" / "dataset-1000-com-preco-promocional-e-renovacao-estoque.csv"

def main():
    df = pd.read_csv(data_path, sep=',')
    print("Arquivo carregado:", data_path)
    print("Dimensões:", df.shape)
    print("Colunas:", df.columns.tolist())
    print("Tipos:", df.dtypes)
    print("--- Descritiva ---")
    print(df.describe(include='all').transpose().head(20))

if __name__ == '__main__':
    main()