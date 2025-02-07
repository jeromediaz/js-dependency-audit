# JS-DEPENDENCY-AUDIT

[![PyPI - License](https://img.shields.io/pypi/l/js-dependency-audit)](https://pypi.org/project/js-dependency-audit/)
[![PyPI - Python Version](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fjeromediaz%2Fjs-dependency-audit%2Frefs%2Fheads%2Fmain%2Fpyproject.toml)](https://pypi.org/project/js_dependency_audit/)
[![PyPI - Version](https://img.shields.io/pypi/v/js-dependency-audit)](https://pypi.org/project/js-dependency-audit/)

A library to help perform a security audit check using a yarn (v1) lock file.

Not intended to be used as a standalone tool, but as part of a system
periodically checking for vulnerabilities.

## Usage

```python
from js_dependency_audit.lock_file_content import LockFileContent
from js_dependency_audit.security_audit_request import request_security_audit

lock_file_content = LockFileContent.from_yarn_file("files/yarn.lock")
audit_data = request_security_audit(lock_file_content)
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/jeromediaz/js-dependency-audit/blob/main/LICENSE) file for details.
