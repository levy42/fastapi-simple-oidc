import uvicorn
from fastapi import FastAPI, Depends

from fastapi_simple_oidc import OIDC, get_logged_user

app = FastAPI()
sso = OIDC(app, '12345')

app.include_router(sso.router)


@app.get('/protected')
def protected(user=Depends(get_logged_user)):
    return user


if __name__ == '__main__':
    uvicorn.run(app)
