from typing import Optional, List

from pydantic import BaseModel


class Resolve(BaseModel):
    id: int
    path: str
    dev: bool
    optional: bool
    bundled: bool


class Action(BaseModel):
    isMajor: Optional[bool] = None
    action: str
    resolves: List[Resolve]
    module: str
    target: Optional[str] = None
    depth: Optional[int] = None
