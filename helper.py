import re
from typing import Union

from fastapi import HTTPException
from fastapi.responses import JSONResponse


def return_response(response) -> JSONResponse:
    return JSONResponse(content=response)


def return_exception(status_code, detail) -> HTTPException:
    raise HTTPException(status_code=status_code, detail=detail)


def convert_array_to_dict(array) -> list:
    return [item.dict() for item in array]  # Convert each item to dictionary


def is_url(input_str) -> bool:
    # Regular expression pattern to match URLs
    url_pattern = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https:// or ftp://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,63}|"  # domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or IPv4
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    return bool(re.match(url_pattern, input_str))


def get_object_by_id(id, array) -> Union[object, bool]:
    for obj in array:
        if getattr(obj, "id") == id:
            return obj
    return False
