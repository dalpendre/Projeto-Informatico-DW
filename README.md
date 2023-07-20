-- Processo de instalação de projeto (Seeder e ETL)

As pastas ETL e Seeder são ambas projetos Python. Deverão ser abertos dentro do IDE pretendido (File -> Open -> Selecionar a pasta desejada).
Recomenda-se a utilização da versão 3.11 do Python para ambos os projetos

Seeder:

- Instalar virtual environment e instalar os pacotes necessários dentro desse mesmo virtual environment

ETL:

- Instalar virtual environment e instalar os pacotes necessários dentro desse mesmo virtual environment. 

Criar dentro de ambos os projetos um ficheiro chamado constants.py (tem de ser estritamente este nome).

No projeto Seeder a estrutura é a seguinte:

username = "username"
password = "password"
host = "host"
port = "5432"
db_name = "projeto_informatico_source_db"
google_maps_api_key = "google_maps_api_key"

No projeto ETL a estrutura é a seguinte:

source_db_name = "projeto_informatico_source_db"
dsa_db_name = "projeto_informatico_dsa_db"
dw_db_name = "projeto_informatico_dw_db"
username = "username"
password = "password"
port = "5432"
host = "host"

Devem ser alterados os campos username, password e host para os valores desejados (o campo host corresponde ao IP do servidor de bases de dados, que poderá ser externo, como cloud, ou localhost) e o username e password da instância, e chave da API do google maps.

------------------------------------------------------------------------------------------------------------------------------------------------

-- Processo de instalação das bases de dados PostgreSQL do sistema fonte, processo ETL, data warehouse e tabelas respetivas

Dentro do software de gestão de bases de dados, dentro da instância de BDs desejada, criar 3 bases de dados e dentro de cada base de dados criar as tabelas correspondentes:

Base de dados projeto_informatico_source_db -> executar o código sql no ficheiro source.sql dentro pasta DBs_scripts/create tables
Base de dados projeto_informatico_dsa_db -> executar o código sql no ficheiro dsa.sql dentro pasta DBs_scripts/create tables
Base de dados projeto_informatico_dw_db -> executar o código sql no ficheiro dw.sql dentro pasta DBs_scripts/create tables