import os
import pandas as pd
from dotenv import load_dotenv
from etl_faculdade.etl.database_connector import connect_to_db
from etl_faculdade.etl.data_loader import load_and_save
from etl_faculdade.analysis.query_analysis import (
    query_a,
    query_b,
    query_c,
    query_d,
    query_e,
    query_f,
    query_g,
    query_h,
    query_i,
    query_j,
    query_k,
    query_l,
    query_m,
)

load_dotenv()


def execute_and_save(query, connection, filename):
    df = pd.read_sql(query, connection)
    df.to_csv(f"etl_faculdade/data/{filename}.csv", index=False)
    return df


def main():
    connection = connect_to_db(
        os.getenv("DB_HOST"),
        os.getenv("DB_PORT"),
        os.getenv("DB_NAME"),
        os.getenv("DB_USER"),
        os.getenv("DB_PASSWORD"),
    )

    tables = ["historicos_escolares", "turmas", "professores", "alunos", "cursos"]
    for table in tables:
        load_and_save(table, connection)

    queries = [
        (query_a, "Professores que mais reprovam", "professores_mais_reprovam"),
        (
            query_b,
            "Quantidade de professores por curso, por ano/semestre",
            "professores_por_curso",
        ),
        (
            query_c,
            "Alunos que não passaram em uma disciplina na primeira tentativa",
            "alunos_reprovados_primeira_tentativa",
        ),
        (
            query_d,
            "Quantidade de alunos por curso num determinado intervalo de tempo:",
            "alunos_por_curso_intervalo",
        ),
        (query_e, "Maiores mpg por curso:", "maiores_mpg_por_curso"),
        (
            query_f,
            "Percentual de reprovação e aprovação de cada aluno:",
            "percentual_reprovacao_aprovacao",
        ),
        (
            query_g,
            "Percentual geral de aprovação de uma disciplina:",
            "percentual_aprovacao_disciplina",
        ),
        (query_h, "Maiores MGP no geral:", "maiores_mgp_geral"),
        (
            query_i,
            "Coordenadores que também são professores:",
            "coordenadores_professores",
        ),
        (
            query_j,
            "Turmas com mais alunos por disciplina/ano/semestre:",
            "turmas_mais_alunos",
        ),
        (
            query_k,
            "Alunos que fizeram disciplinas fora do seu curso:",
            "alunos_disciplinas_fora_curso",
        ),
        (
            query_l,
            "Nome do coordenador na dimensão Cursos:",
            "cursos_update",
        ),
        (
            query_m,
            "Situação corrigida na dimensão Histórico Escolares:",
            "historico_escolares_corrigido",
        ),
    ]

    for query, description, filename in queries:
        print(description + ":")
        print(execute_and_save(query, connection, filename))
    connection.close()


if __name__ == "__main__":
    main()
