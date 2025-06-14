from fastapi import APIRouter

from src.api.v1.healthcheck.schemas import HealthcheckResponse
from src.utils.i18n import _

router = APIRouter()


@router.get(
    "/",
    response_model=HealthcheckResponse,
    summary=_("Get healthcheck endpoint"),
    description=_("Returns the status of the application"),
)
def get_healthcheck():
    return HealthcheckResponse(status="ok")
