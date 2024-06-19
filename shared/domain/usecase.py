from typing import Protocol, Any, Optional


class UseCase(Protocol):
    """Use Case that defines the base of a business level use case.

    Args:
        Protocol (_type_): _description_
    """
    
    async def execute(self, request: Any) -> Optional[Any]:
        pass
