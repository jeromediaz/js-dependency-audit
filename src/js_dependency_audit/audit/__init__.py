from typing import List, Dict

from pydantic import BaseModel

from .action import Action
from .metadata import Metadata
from .advisory import Advisory


class Audit(BaseModel):
    actions: List[Action]
    advisories: Dict[str, Advisory]
    muted: List
    metadata: Metadata
