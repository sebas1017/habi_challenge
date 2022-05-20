from fastapi import FastAPI
from core.config import settings
from app_propiedades  import routes
from starlette.responses import JSONResponse
import os
import uvicorn



app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
app.include_router(routes.router)

@app.exception_handler(404)
async def custom_404_handler(_, __):
	return JSONResponse({"message": "el recurso solicitado no existe"}, status_code=404)
	




if __name__=="__main__":
	PORT = int(os.environ.get('PORT', 8000))
	uvicorn.run("main:app",host='0.0.0.0',port=PORT ,reload=True)