from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from .disciplina import Disciplina
from .professor import Professor
from .periodo import PeriodoLetivo
from .matricula import Matricula
from .aluno import Aluno


@dataclass()
class Turma:
    disciplina: Disciplina
    professor: Professor
    periodo: PeriodoLetivo
    vagas: int = 20
    matriculas: List[Matricula] = field(default_factory=list)

    def tem_vaga(self):
        return len(self.matriculas) <= self.vagas

    def matricular(self, aluno: Aluno) -> Matricula:
        if not self.tem_vaga():
            raise ValueError("turma sem vagas disponiveis")
        matricula = Matricula(aluno=aluno, disciplina=self.disciplina, periodo_letivo=self.periodo)
        self.vagas = self.vagas - 1
        self.matriculas.append(matricula)
        return matricula
