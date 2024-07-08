from .typings import Resp


def resp_cors() -> Resp:
    """
    Функция, которая включает поддержку CORS для Cloud Function.
    Пример:
    >>> async def handler(event: Event, context) -> Resp:
    ...     if event["httpMethod"] == "OPTIONS":
    ...         return resp_cors()
    """
    return {
        "statusCode": 200,
        "body": "ok",
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "*",
        },
    }
