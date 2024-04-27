from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from helper import get_object_by_id, is_url, return_exception, return_response

app = FastAPI()

urlObjects = []


class Url(BaseModel):
    id: int = None
    url: str = None


class UrlInput(BaseModel):
    url: str


# this provides path parameter validation request should be like /id/1
@app.get("/urls/id/{id}")
def get_and_redirect(id: int):
    # IMPLEMENT FIREBASE OBJECT FETCHING
    object = get_object_by_id(id, urlObjects)
    if object:
        return RedirectResponse(url=getattr(object, "url"))
    else:
        return_exception(404, f"Item with id {id} is not found")


# this provides query parameter validation request should be like /urls/?id=1
@app.get("/urls/")
def get_and_redirect(id: int = Query(..., title="ID of the URL")):
    # IMPLEMENT FIREBASE OBJECT FETCHING
    object = get_object_by_id(id, urlObjects)
    if object:
        return RedirectResponse(url=getattr(object, "url"))
    else:
        return_exception(404, f"Item with id {id} is not found")


@app.post("/url/create")
def create_url(url_body: UrlInput):
    url = url_body.url

    if not is_url(url):
        return_exception(400, "URL is not valid")

    # IMPLEMENT FIREBASE OBJECT CREATION
    new_url = Url(id=len(urlObjects) + 1, url=url)
    urlObjects.append(new_url)

    json_data = new_url.dict()
    return return_response(json_data)
