from __future__ import annotations
from dataclasses import dataclass
from enum import StrEnum, auto


class Situacao(StrEnum):
    CURSANDO = auto()
    APROVADO = auto()
    REPROVADO = auto()
    REPROVADO_POR_FALTA = auto()

class TipoDisciplina(StrEnum):
    ESTAGIO = auto()
    NORMAIS = auto()

@dataclass(frozen=True)
class SemestreLetivo:
    ano: int
    semestre: int

    def __post_init__(self):
        if self.ano < 2000:
            raise ValueError("ano inválido (< 2000)")
        if self.semestre not in (1, 2):
            raise ValueError("semestre deve ser 1 ou 2")

    def __str__(self):
        return f"{self.ano}.{self.semestre}"

@dataclass(frozen=True)
class CodigoDisciplina:
    value: str

    def __post_init__(self):
        if not self.value or len(self.value) > 7:
            raise ValueError("código da disciplina inválido")

    def __str__(self):
        return self.value