from pydantic import BaseModel, Field

from src.utils.i18n import _


class HealthcheckResponse(BaseModel):
    status: str = Field(..., description=_("Status of the application"))
