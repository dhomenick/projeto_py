from __future__ import annotations
from dataclasses import dataclass
from .tipos import SemestreLetivo


@dataclass()
class PeriodoLetivo:
    ano: SemestreLetivo.ano
    semestre: SemestreLetivo.semestre
    data_ini: str
    data_fim: str
