from pydantic import BaseModel


class Vulnerabilities(BaseModel):
    info: int
    low: int
    moderate: int
    high: int
    critical: int

class Metadata(BaseModel):
    vulnerabilities: Vulnerabilities
    dependencies: int
    devDependencies: int
    optionalDependencies: int
    totalDependencies: int