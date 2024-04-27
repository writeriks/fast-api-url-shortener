from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse

from helper import return_exception

app = FastAPI()


# this provides path parameter validation request should be like /id/1
@app.get("/id/{id}")
def get_and_redirect(id: int):
    if id == 1:
        return RedirectResponse(url="https://www.emiroztrk.com/")
    else:
        return_exception(404, f"Item with id {id} is not found")


# this provides query parameter validation request should be like /urls/?id=1
@app.get("/urls/")
def get_and_redirect(id: int = Query(..., title="ID of the URL")):
    if id == 1:
        return RedirectResponse(url="https://www.emiroztrk.com/")
    else:
        return_exception(404, f"Item with id {id} is not found")
