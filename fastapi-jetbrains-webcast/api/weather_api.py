from typing import Optional
import fastapi
from models.location import Location


router = fastapi.APIRouter()


@router.get('/api/umbrella')
def do_i_need_an_umbrella(location: Location = fastapi.Depends()):
    return location
