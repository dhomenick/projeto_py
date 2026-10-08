from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass()
class Historico:
    itens: List[object] = field(default_factory=list)