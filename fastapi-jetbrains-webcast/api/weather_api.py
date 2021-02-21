from typing import Optional
import fastapi

router = fastapi.APIRouter()


@router.get('/api/umbrella')
def do_i_need_an_umbrella(city: str, country: str = 'us', state: Optional[str] = None):
    return {"city": city}
