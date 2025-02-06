import json
from os import PathLike
from typing import NamedTuple, Dict, Self


class _DependencyVersion(NamedTuple):
    version: str
    integrity: str

class LockFileContent:

    def __init__(self) -> None:
        super().__init__()
        self._requires_map: Dict[str, str] = {}
        self._dependencies_map: Dict[str, _DependencyVersion] = {}

    @classmethod
    def from_yarn_file(cls, path: int | str | bytes | PathLike[str] | PathLike[bytes]) -> Self:
        from pyarn import lockfile
        yarn_lock_file = lockfile.Lockfile.from_file(path)

        instance = cls()

        for dep_key, data in yarn_lock_file.data.items():
            dep_name, version_marker = dep_key.rsplit("@", 1)

            version = data['version']
            integrity = data['integrity']

            instance.add_dependency(dep_name, version_marker, version, integrity)

        return instance


    def add_dependency(self, name: str, marked: str, version: str, integrity: str):
        self._requires_map[name] = marked
        self._dependencies_map[name] = _DependencyVersion(version, integrity)


    def as_json(self) -> str:
        payload = {
            "name": "npm_audit_test",
            "version": "1.0.0",
            "requires": self._requires_map,
            "dependencies": {name:{"version": data[0], "integrity": data[1]} for name, data in self._dependencies_map.items()}
        }

        return json.dumps(payload)