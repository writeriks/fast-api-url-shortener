from fastapi import FastAPI, Query, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from firebase import create_firebase_document, read_firebase_document
from helper import is_url, return_exception, return_response

app = FastAPI()


class UrlModel(BaseModel):
    url: str = None


# this provides path parameter validation request should be like /id/1
@app.get("/urls/{id}")
def get_and_redirect(id: str):
    object: UrlModel = read_firebase_document("urls", id)
    if object:
        return RedirectResponse(url=object["url"])

    return_exception(404, f"Item with id {id} is not found")


@app.post("/urls/create")
def create_url(url_body: UrlModel, request: Request):
    url = url_body.url

    if not is_url(url):
        return_exception(400, "URL is not valid")

    document_data = {"url": url}
    doc_id = create_firebase_document("urls", document_data)

    shortened_url = f"{request.base_url}urls/{doc_id}"
    return return_response(shortened_url)
