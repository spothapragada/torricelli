from typing import Optional
import fastapi
from models.location import Location


router = fastapi.APIRouter()


@router.get('/api/umbrella', response_model=Location)
def do_i_need_an_umbrella(location: Location = fastapi.Depends()):
    return location
