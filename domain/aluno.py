from __future__ import annotations
from dataclasses import dataclass, field
from .historico import Historico


@dataclass()
class Aluno:
    mat_alu: int
    nome: str
    cod_curso: int
    data_nasc: str
    mgp: float = 0.0
    total_creditos: int = 0
    historico: Historico = field(default_factory=Historico)
