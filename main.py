from fastapi import FastAPI
from routes.user_route import router

app = FastAPI()

@app.get("/health-check")
def health_check():
    return "works"

app.include_router(router=router)




