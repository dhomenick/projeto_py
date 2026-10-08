from __future__ import annotations
from dataclasses import dataclass
from .aluno import Aluno
from .disciplina import Disciplina
from .periodo import PeriodoLetivo
from .tipos import Situacao


@dataclass()
class Matricula:
    aluno: Aluno
    disciplina: Disciplina
    periodo_letivo: PeriodoLetivo
    situacao: Situacao = Situacao.CURSANDO
