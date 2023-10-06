## ETL Faculdade

### Visão Geral

Este projeto foi desenvolvido para extrair, transformar e carregar (ETL) dados de um banco de dados universitário. Também inclui um conjunto de análises predefinidas para ajudar na geração de insights a partir dos dados. Os dados são salvos em arquivos CSV após a extração e transformação, facilitando o compartilhamento e análise com outras ferramentas.

### Estrutura

- **etl_faculdade**: Pasta principal contendo os módulos ETL e análise.

  - **etl**: Contém scripts relacionados ao processo ETL.
    - **data_loader.py**: Funções para carregar dados do banco de dados e salvá-los como arquivos CSV.
    - **database_connector.py**: Função auxiliar para conectar ao banco de dados.
  - **analysis**: Contém scripts relacionados à análise de dados.
    - **query_analysis.py**: Consultas SQL predefinidas para análise de dados.

- **main.py**: O script principal que orquestra o processo ETL e executa a análise.

### Configuração

1. Clone o repositório.
2. Crie um arquivo `.env` no diretório raiz com as seguintes variáveis:

   ```
   DB_HOST=<Seu Host do Banco de Dados>
   DB_PORT=<Sua Porta do Banco de Dados>
   DB_NAME=<Nome do Seu Banco de Dados>
   DB_USER=<Seu Usuário do Banco de Dados>
   DB_PASSWORD=<Sua Senha do Banco de Dados>
   ```

3. Certifique-se de ter os pacotes Python necessários instalados:

   ```
   pip install -r requirements.txt
   ```

### Uso

Execute o script `main.py`:

```python
python main
```

Este script irá:

1. Conectar-se ao banco de dados.
2. Extrair dados de tabelas especificadas.
3. Transformar dados (se necessário, por exemplo, conversões de formato de data).
4. Salvar os dados transformados em arquivos CSV no diretório `etl_faculdade/data`.
5. Executar um conjunto de análises predefinidas.
6. Salvar os resultados das análises em arquivos CSV no diretório `etl_faculdade/data`.
7. Imprimir os resultados de cada análise no console.

### Análises

O projeto inclui várias análises predefinidas, incluindo:

1. Professores que mais reprovam alunos.
2. Número de professores por curso, por ano/semestre.
3. Alunos que não passaram em uma matéria na primeira tentativa.
4. Número de alunos por curso em um determinado período.
5. Maior média de notas por curso.
6. Porcentagem de aprovação e reprovação de cada aluno.
7. Porcentagem geral de aprovação de uma matéria.
8. Maior média geral de notas.
9. Coordenadores que também são professores.
10. Turmas com mais alunos por matéria/ano/semestre.
11. Alunos que cursaram matérias fora de seu curso.
12. Nome do coordenador na dimensão Cursos.
13. Situação corrigida na dimensão Histórico Escolar.

Para cada análise, os resultados são salvos em um arquivo CSV dedicado no diretório `etl_faculdade/data`.

### Conclusão

Este projeto oferece uma maneira direta de realizar operações ETL em dados universitários e obter insights por meio de análises predefinidas. Ao salvar os resultados em arquivos CSV, os dados podem ser facilmente compartilhados e analisados usando outras ferramentas.
