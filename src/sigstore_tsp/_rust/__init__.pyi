class TimeStampRequest: ...

def create_timestamp_request(
    data: bytes,
) -> TimeStampRequest: ...


class TimeStampResponse: ...

def parse_timestamp_response(
    data: bytes,
) -> TimeStampResponse: ...
