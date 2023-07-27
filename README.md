# Projeto_covid_dados19  

# Projeto COVID-19 Dashboard

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


Passo a passo no Pentaho Data Integration:
* 		Generate rows: Esse passo é usado para gerar um conjunto de linhas com valores específicos. No projeto, pode ser utilizado para criar um conjunto de linhas vazio para ser preenchido posteriormente com os dados da API.
* 		REST client: Nesse passo, é configurada uma chamada HTTP para uma API que contém os dados desejados. Ele permite fazer uma solicitação para uma URL e obter os dados no formato JSON ou XML. No projeto, o REST client é utilizado para acessar a API que contém os dados de casos de COVID-19 em diferentes municípios.
* 		JSON input: Esse passo é utilizado para ler os dados JSON obtidos do passo anterior. Ele transforma os dados no formato JSON em um formato tabular (linhas e colunas) que pode ser manipulado no Pentaho Data Integration. No projeto, o JSON input é usado para processar os dados obtidos do REST client.
* 		Select values: Nesse passo, é feita a seleção de colunas específicas e a filtragem dos dados. Ele permite selecionar apenas as colunas relevantes para o projeto e filtrar os dados com base em certos critérios. No projeto, o Select values pode ser utilizado para selecionar apenas as colunas "_id", "nome", "casosAcumulado" e "obitosAcumulado", que são as informações necessárias para o dashboard.
* 		Microsoft Excel Output: Esse passo é usado para escrever os dados processados em um arquivo Excel. No projeto, ele pode ser utilizado para armazenar temporariamente os dados processados antes de inseri-los no banco de dados PostgreSQL.
* 		PostgreSQL Output: Nesse passo, os dados processados são inseridos no banco de dados PostgreSQL. Ele faz a conexão com o banco de dados e insere os dados nas tabelas apropriadas. No projeto, o PostgreSQL Output é utilizado para inserir os dados na tabela que será utilizada para criar o dashboard.
Para que serve cada passo:
* Generate rows: Serve para criar um conjunto inicial de linhas vazio que será preenchido posteriormente com os dados da API.
* REST client: Serve para acessar uma API e obter os dados desejados, como os casos de COVID-19 em diferentes municípios.
* JSON input: Serve para transformar os dados JSON obtidos da API em um formato tabular que pode ser manipulado no Pentaho Data Integration.
* Select values: Serve para selecionar apenas as colunas relevantes e filtrar os dados com base em certos critérios.
* Microsoft Excel Output: Serve para armazenar temporariamente os dados processados antes de inseri-los no banco de dados PostgreSQL.


