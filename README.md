# Datajud ETL Pipeline

![status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

> Pipeline de extração, tratamento e carga (ETL) de dados processuais públicos do Poder Judiciário brasileiro, usando a API pública do Datajud (CNJ).

---

## Sobre o projeto

Esse projeto extrai dados públicos de processos judiciais via API do Datajud (CNJ), trata os registros (JSON) e os organiza em um banco relacional para consulta. O objetivo é demonstrar uma projeto de integração e automação de dados usando uma fonte pública.

## Hipóteses de trabalho

- Como se distribui o volume de processos por classe e assunto em um tribunal?
- Existe sazonalidade no ajuizamento de processos ao longo do ano?
- Quanto tempo, em média, leva entre o ajuizamento e o último movimento registrado?

## Fontes de dados

| Fonte | Descrição | 
|---|---|
| API Pública do Datajud (CNJ) | Metadados processuais (classe, assunto, movimentos, datas) por tribunal | 

## Metodologia

Este projeto segue as etapas abaixo (adaptado de CRISP-DM):

1. Definição do Problema
2. Aquisição de Dados — consumo da API REST do Datajud (autenticação via chave pública)
3. Perfilamento de Dados — inspeção da estrutura JSON retornada por tribunal
4. Validação de Escopo — ajuste do recorte (tribunal, período, tipo de processo) conforme volume/qualidade dos dados
5. Preparação de Dados — normalização do JSON, padronização de campos
6. Análise Exploratória — indicadores de volume, distribuição por classe/assunto, séries temporais
7. Documentação e Achados
8. Implantação e Disseminação — carga em banco relacional e painel de visualização

## Tecnologias utilizadas

- Linguagem: Python
- Bibliotecas principais: requests, pandas
- Banco de dados: PostgreSQL
- Visualização: Power BI

## Estrutura do repositório

```
datajud-etl-pipeline/
├── data/
│   ├── raw/          #Dado não-processado
│   └── processed/    #Dado tratado
├── docs/             #Documentação adicional
├── notebooks/        #Jupyter Notebook
├── src/              #Código fonte módular
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
├── .gitignore
├── README.md
└── requirements.txt
```


## Como rodar

```bash
[quando o primeiro script estiver funcional]
```

## Roadmap

- [x] Definição do problema
- [ ] Coleta de dados (API Datajud)
- [ ] Validação de escopo
- [ ] Preparação e carga no PostgreSQL
- [ ] Análise exploratória
- [ ] Documentação dos achados
- [ ] Publicação (dashboard Power BI)

## Achados principais

_Preencher ao final da análise exploratória._

## Limitações conhecidas

- Cobertura limitada aos tribunais e período selecionados no recorte inicial.
- Dados dependem da qualidade de preenchimento de cada tribunal na base do CNJ.

## Fontes e referências

- Datajud (CNJ) — API Pública: https://datajud-wiki.cnj.jus.br/api-publica/

## Autor

pazoliveira
