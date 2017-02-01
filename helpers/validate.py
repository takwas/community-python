from uuid import UUID


def uuid_validation(uuid: str, version: int = 1) -> bool:
    try:
        val = UUID(uuid, version=version)
    except ValueError:
        return False

    return True