from __future__ import annotations
from dataclasses import dataclass


@dataclass()
class Professor:
    idt_prof: int
    matricula: int
    nome: str
