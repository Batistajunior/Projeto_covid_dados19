CREATE TABLE covid_dados (
    _id TEXT,
    nome TEXT,
    cod TEXT,
    casosAcumulado INTEGER,
    obitosAcumulado INTEGER
);



COPY covid_dados FROM '/Users/batistajunior/Downloads/Projeto_covid_dados/covid_dados.csv' DELIMITER ';' CSV HEADER;

select _id,  casosAcumulado 
from covid_dados 
order by casosAcumulado desc 
Limit 10;

SELECT _id, casosAcumulado
FROM covid_dados
ORDER BY casosAcumulado ASC
LIMIT 5;










