# Instruções detalhadas para o Amazon SageMaker Canvas

1. Acesse a AWS Console e selecione a região: **América do Sul (São Paulo) — sa-east-1**
2. Procure por **SageMaker** e abra **Canvas**
3. Se for o primeiro uso, clique em **Configurar para um único usuário**
4. No Canvas:
   - **Create dataset** → `Upload file` → escolha `datasets/dataset-1000-com-preco-promocional-e-renovacao-estoque.csv`
   - Verifique tipos de coluna (date, numeric, categorical)
   - Se a base tiver coluna de data:
     - Marque essa coluna como **tempo** (timestamp)
     - Selecione o problema como **Forecast** (previsão)
   - Se não houver coluna de data, selecione **Prediction (tabular)**
5. Defina a **variável alvo** (target):
   - Exemplos: `vendas`, `quantidade_vendida`, `demanda`
   - Se seu arquivo tiver `preco_promocional`, avalie o impacto das promoções como feature
6. Treine o modelo (Canvas seleciona automaticamente algoritmos e validação)
7. Avalie métricas (MAE, RMSE, R2, etc) e a importância das features
8. Exporte previsões para CSV
9. Faça prints das telas principais e salve em `docs/prints` (opcional)
10. Para reduzir custos: finalize/pare a aplicação Canvas quando terminar.

Dica: Ao documentar, inclua uma seção "Como reproduzir" com prints das etapas.