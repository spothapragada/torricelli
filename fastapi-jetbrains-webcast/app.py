import fastapi
import uvicorn
from views import home
from api import weather_api
import logging

logging.basicConfig(filename='log_file', level=logging.DEBUG, format="'%(asctime)s %(message)s'")
api = fastapi.FastAPI()


def configure():
    api.include_router(home.router)
    api.include_router(weather_api.router)


# @api.get('/')
# def index():
#     return {
#         "message": "Hello World!",
#         "status": "OK"
#     }

# @api.get('/api/calculate')
# def calculate():
#     return 2 + 2
configure()
if __name__ == '__main__':
    # uvicorn.run(api, host='127.0.0.1', port=8000)
    uvicorn.run(api)
