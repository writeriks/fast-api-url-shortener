from fastapi import HTTPException
from fastapi.responses import JSONResponse


def return_response(response):
    httpResponse = JSONResponse(content=response)
    httpResponse.set_cookie(key="emir", value="i am  the one")
    return httpResponse
    # return Response(content=json.dumps(response, indent=4), media_type="application/json")


def return_exception(status_code, detail):
    raise HTTPException(status_code=status_code, detail=detail)


def convert_array_to_dict(array):
    return [item.dict() for item in array]  # Convert each item to dictionary
