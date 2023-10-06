# a. Quais professores mais reprovam?
query_a = """
SELECT p.nom_prof, COUNT(*) as reprovacoes
FROM professores p
JOIN historicos_escolares h ON p.cod_prof = h.cod_disc
WHERE h.situacao = 'RF'
GROUP BY p.nom_prof
ORDER BY reprovacoes DESC;
"""

# b. Quantidade de professores por curso, por ano/semestre.
query_b = """
SELECT c.nom_curso, t.ano, t.semestre, COUNT(DISTINCT p.cod_prof) as num_professores
FROM professores p
JOIN turmas t ON p.cod_prof = t.cod_prof
JOIN cursos c ON p.cod_curso = c.cod_curso
GROUP BY c.nom_curso, t.ano, t.semestre
ORDER BY c.nom_curso, t.ano, t.semestre;
"""

# c. Alunos que não passaram em uma disciplina na primeira tentativa;
query_c = """
WITH RankHistoricos AS (
    SELECT mat_alu, cod_disc,
    RANK() OVER (PARTITION BY mat_alu, cod_disc ORDER BY ano, semestre) as tentativa
    FROM historicos_escolares
    WHERE situacao = 'RF'
)
SELECT mat_alu, cod_disc FROM RankHistoricos WHERE tentativa = 1;
"""

# d. Quantidade de alunos por curso num determinado intervalo de tempo;
query_d = """
SELECT a.cod_curso, COUNT(DISTINCT h.mat_alu) as num_alunos
FROM historicos_escolares h
JOIN alunos a ON h.mat_alu = a.mat_alu
WHERE h.ano BETWEEN 1974 AND 2002
GROUP BY a.cod_curso;
"""

# e. Maiores mpg por curso.
query_e = """
SELECT cod_curso, MAX(mgp) as maior_mgp
FROM alunos
GROUP BY cod_curso;
"""

# f. Percentual de reprovação e aprovação de cada aluno;
query_f = """
WITH ReprovacaoAprovacao AS (
    SELECT 
        mat_alu,
        CASE WHEN situacao IN ('RF', 'RM') THEN 'Reprovado' ELSE 'Aprovado' END AS status,
        COUNT(*) AS total
    FROM historicos_escolares
    GROUP BY mat_alu, status
)
SELECT
    mat_alu,
    SUM(CASE WHEN status = 'Reprovado' THEN total ELSE 0 END) AS reprovacoes,
    SUM(CASE WHEN status = 'Aprovado' THEN total ELSE 0 END) AS aprovacoes,
    ROUND(100.0 * SUM(CASE WHEN status = 'Reprovado' THEN total ELSE 0 END) / COUNT(*), 2) AS perc_reprovacoes,
    ROUND(100.0 * SUM(CASE WHEN status = 'Aprovado' THEN total ELSE 0 END) / COUNT(*), 2) AS perc_aprovacoes
FROM ReprovacaoAprovacao
GROUP BY mat_alu;
"""

# g. Percentual geral de aprovação de uma disciplina;
query_g = """
SELECT cod_disc,
       ROUND(100.0 * SUM(CASE WHEN situacao = 'AP' THEN 1 ELSE 0 END) / COUNT(*), 2) AS perc_aprovacao
FROM historicos_escolares
GROUP BY cod_disc;
"""

# h. Maiores MGP no geral
query_h = """
SELECT MAX(mgp) as maior_mgp_geral
FROM alunos;
"""

# i. Coordenadores que também são professores;
query_i = """
SELECT cod_prof
FROM professores
WHERE cod_prof IN (SELECT cod_coord FROM cursos WHERE cod_coord IS NOT NULL);
"""

# j. Turmas com mais alunos por disciplina/ano/semestre
query_j = """
SELECT cod_disc, ano, semestre, COUNT(DISTINCT mat_alu) as num_alunos
FROM turmas_matriculadas
GROUP BY cod_disc, ano, semestre
ORDER BY num_alunos DESC;
"""

# k. Quais alunos fizeram disciplinas fora do seu curso?
query_k = """
SELECT DISTINCT h.mat_alu
FROM historicos_escolares h
JOIN alunos a ON h.mat_alu = a.mat_alu
WHERE h.cod_disc NOT IN (SELECT cod_disc FROM curriculos WHERE cod_curso = a.cod_curso);
"""

# iv. O nome do coordenador precisa estar também na dimensão Cursos;
query_l = """
SELECT
    c.cod_curso,
    c.tot_cred,
    c.nom_curso,
    c.cod_coord,
    p.nom_prof AS nome_coordenador
FROM
    cursos c
LEFT JOIN
    professores p ON c.cod_coord = p.cod_prof;
"""
# ii. Quando a situação for “Reprovado”, indique se a reprovação foi por FALTAS ou por MÉDIA.
# No caso teremos 3 tipos de situação na dimensão Histórico Escolares;
query_m = """
SELECT historicos_escolares.cod_disc, historicos_escolares.mat_alu,historicos_escolares.media,historicos_escolares.faltas,
    historicos_escolares.situacao,disciplinas.qtd_cred,
    (CASE
        WHEN disciplinas.qtd_cred = 4 THEN
             (CASE
                WHEN media < 6 AND faltas <= 21 THEN 'RM'
                 WHEN media < 6 AND faltas >= 21 THEN 'RM'
                 WHEN media >= 6 AND faltas >21 THEN 'RF'
              ELSE 'AP'
             END)
         WHEN disciplinas.qtd_cred = 2 THEN
             (CASE
                WHEN media < 6 AND faltas <= 11 THEN 'RM'
                 WHEN media < 6 AND faltas >= 11 THEN 'RM'
                 WHEN media >= 6 AND faltas >11 THEN 'RF'
              ELSE 'AP'
             END)
         WHEN disciplinas.qtd_cred = 16 THEN
             (CASE
                WHEN media < 6 AND faltas <= 84 THEN 'RM'
                 WHEN media < 6 AND faltas >= 84 THEN 'RM'
                 WHEN media >= 6 AND faltas >84 THEN 'RF'
              ELSE 'AP'
             END)
     ELSE 'AP'
    END) AS situacaos
FROM historicos_escolares,disciplinas-- where cod_disc = 200851 and mat_alu = 934091 
WHERE historicos_escolares.cod_disc = disciplinas.cod_disc
"""
