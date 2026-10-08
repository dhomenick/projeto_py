from domain import (
    CodigoDisciplina, TipoDisciplina, Disciplina, Professor,
    Aluno, PeriodoLetivo, Turma
)

def run():
    disciplina = Disciplina(
        cod_disc=CodigoDisciplina("TMS0060"),
        nome="Desenvolvimento Rápido",
        creditos=2,
        tipo=TipoDisciplina.NORMAIS,
        limite_faltas=10,
    )
    prof = Professor(
        idt_prof=1, matricula=1234,
        nome="Elisrenan Barbosa"
    )
    aluno = Aluno(
        mat_alu=1, nome="Joao",
        cod_curso=4, data_nasc="01/04/2000"
    )
    periodo = PeriodoLetivo(
        semestre=2,
        ano=2025,
        data_ini="19/08/2025",
        data_fim="10/12/2025"
    )
    turma = Turma(disciplina=disciplina,
                  professor=prof,
                  periodo=periodo,
                  vagas=2)
    matricula = turma.matricular(aluno)
    print("Turma criada: ", turma.disciplina, str(turma.periodo))
    print("Matriculas: ", len(turma.matriculas))
    print("Aluno: ", matricula.aluno.nome, "| Situacao: ", matricula.situacao)
    print("Vagas restante", turma.vagas)

if __name__ == "__main__":
    run()