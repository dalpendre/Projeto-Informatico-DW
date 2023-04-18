-- Database: projeto_informatico

-- DROP DATABASE IF EXISTS projeto_informatico;

CREATE DATABASE projeto_informatico
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

COMMENT ON DATABASE projeto_informatico
    IS 'Data Warehouse de Projeto Informático de apresentação de veículos em mapas';