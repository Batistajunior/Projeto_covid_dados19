# Projeto_covid_dados19  



Este projeto consiste em um dashboard interativo para visualização dos casos de COVID-19 em diferentes municípios. Os dados são obtidos através de uma API, processados utilizando o Pentaho Data Integration e, em seguida, visualizados usando Python, Flask e Plotly.

## Funcionalidades

- Visualização dos casos confirmados e óbitos por COVID-19 em diferentes municípios.
- Gráficos interativos de barra.
- Identificação dos 10 municípios com os maiores e menores índices de casos confirmados.

## Requisitos

- Python 3.x
- Flask
- Plotly
- Pandas
- Pentaho Data Integration (PDI)

## Configuração

1. Certifique-se de ter todas as dependências instaladas. Caso precise, você pode instalar as dependências do Python através do arquivo `requirements.txt`.


2. No Pentaho Data Integration, crie a transformação para extrair os dados da API, processá-los conforme necessário e armazená-los no banco de dados PostgreSQL. Utilize os passos Generate rows, REST client, JSON input, Select values e Microsoft values output.

3. No Python, execute o arquivo `app.py` para iniciar o servidor Flask e acessar o dashboard no navegador.

## Executando o Dashboard

Para executar o dashboard, execute o seguinte comando no terminal:

```bash
python app.py





