import datetime
from typing import List, Optional

from pydantic import BaseModel


class Finding(BaseModel):
    version: str
    paths: List[str]


class Cvss(BaseModel):
    score: float
    vectorString: Optional[str]

class Advisory(BaseModel):
    findings: List[Finding]
    found_by: Optional[str]
    deleted: Optional[datetime.datetime]
    references: str
    created: datetime.datetime
    id: int
    npm_advisory_id: None
    overview: str
    reported_by: None
    title: str
    metadata: None
    cves: List[str]
    access: str
    severity: str
    module_name: str
    vulnerable_versions: str
    github_advisory_id: str
    recommendation: str
    patched_versions: str
    updated: str
    cvss: Cvss
    cwe: List[str]
    url: str