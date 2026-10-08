from __future__ import annotations
from dataclasses import dataclass
from .tipos import CodigoDisciplina, TipoDisciplina

@dataclass()
class Disciplina:
    cod_disc: CodigoDisciplina
    nome: str
    creditos: int
    tipo: TipoDisciplina
    horas_obrig: int = 0
    limite_faltas: int = 18

    def creditos_horas(self) -> int:
        """Conversão simples: 1 crédito = 1h"""
        return  self.creditos * 1