# Projetos-SENAI
# Mini-Projeto Avaliativo - Base Varejo

INTRODUÇÃO
Este projeto tem como objetivo aplicar técnicas de ETL e análise de qualidade de dados
em uma base de varejo, seguindo sprints organizados para importação, limpeza,
transformação e análise estatística.

## ETL - Extract, Transform, Load
- **[Extract](ca://s?q=ETL_Extract)**: processo de extração dos dados da fonte original (CSV da base de varejo).
- **[Transform](ca://s?q=ETL_Transform)**: aplicação de regras de limpeza, conversão de tipos, tratamento de nulos e duplicatas.
- **[Load](ca://s?q=ETL_Load)**: carregamento da versão limpa em um novo arquivo (df_limpo.csv) ou em um banco de dados.

O ETL garante que os dados estejam prontos para análise, reduzindo inconsistências e aumentando a confiabilidade dos resultados.

## Qualidade de Dados
A qualidade dos dados é essencial para análises corretas. Os principais critérios são:

- **[Completude](ca://s?q=Qualidade_de_dados_Completude)**: ausência de valores nulos ou tratamento adequado.
- **[Consistência](ca://s?q=Qualidade_de_dados_Consistencia)**: padronização de formatos (datas, categorias).
- **[Validade](ca://s?q=Qualidade_de_dados_Validade)**: dados coerentes com regras de negócio (ex.: número de filhos não negativo).
- **[Unicidade](ca://s?q=Qualidade_de_dados_Unicidade)**: remoção de duplicatas.
- **[Acurácia](ca://s?q=Qualidade_de_dados_Acuracia)**: proximidade dos dados com a realidade observada.

Refletir sobre qualidade de dados significa reconhecer que análises só são confiáveis
quando a base foi devidamente tratada.

## Sprints

- Sprint 1: Importação dos dados
- Sprint 2: Transformação de tipos (string, int, float, datetime)
- Sprint 3: Limpeza de nulos e duplicatas
- Sprint 4: Estatística descritiva da coluna CL_FHL (número de filhos)
- Sprint 5: Relatório e documentação (este README.md)
- Sprint 6: Versionamento no GitHub

## Resumo dos Insights
Itens essenciais dominam: Alimentos (52,38%), Higiene (18,74%) e Limpeza (17,56%) concentram 88,68% do volume total, mostrando que o público usa o estabelecimento principalmente para suprimentos básicos.

Baixa penetração em categorias secundárias: Bebidas (5,22%), Pet (3,90%) e Acessórios (1,75%) têm pouca participação, indicando espaço para estratégias de cross‑selling.

Predomínio de clientes sem filhos: 52,70% da base não possui dependentes, sugerindo campanhas segmentadas — embalagens individuais para lares unipessoais e kits família para os 47,30% restantes.

Concentração no Segmento B: 64,50% dos clientes pertencem ao Segmento B, seguido por C (27,10%) e A (8,40%).

Alta recorrência no Segmento C: Apesar de menor valor por compra, clientes do Segmento C têm a maior média de transações (~856 compras), revelando fidelidade elevada.

Oportunidade de venda cruzada: Reposicionamento de layout e promoções podem aumentar faturamento em categorias de maior margem (Bebidas, Pet, Acessórios).

