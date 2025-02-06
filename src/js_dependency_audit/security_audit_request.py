from typing import TYPE_CHECKING

from .audit import Audit

if TYPE_CHECKING:
    from .lock_file_content import LockFileContent


def request_security_audit(lock_file_content: "LockFileContent") -> Audit:
    import requests

    try:
        response = requests.post(
            url="https://registry.npmjs.org/-/npm/v1/security/audits",
            headers={
                "Content-Type": "application/json; charset=utf-8"
            },
            data=lock_file_content.as_json()
        )

        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))

        return Audit.model_validate_json(response.content.decode('utf-8'))

    except requests.exceptions.RequestException:
        print('HTTP Request failed')

