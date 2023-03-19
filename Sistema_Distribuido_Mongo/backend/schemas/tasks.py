from typing import Any, Optional

from pydantic import BaseModel, NonNegativeInt


class TasksOptionalParameters(BaseModel):
    countdown_in_seconds: Optional[NonNegativeInt] = None
    payload: Optional[dict[str, Any]] = None
