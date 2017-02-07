from uuid import UUID


def uuid_validation(uuid: str, version: int = 4) -> bool:
    try:
        val = UUID(uuid, version=version)
    except ValueError:
        return False

    return True
