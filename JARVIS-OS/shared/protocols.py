from typing import Final, List


HTTP_Route: Final[str] = "/v1/jarvis"
HTTP_Method: Final[str] = "POST"
REQUEST_TIMEOUT_SECONDS: Final[int] = 30
STREAMING_CHUNK_SIZE: Final[int] = 1024
MAX_CONTENT_LENGTH: Final[int] = 100_000
VALID_INPUT_TYPES: Final[List[str]] = ["text", "voice"]
VALID_DEVICE_STATES: Final[List[str]] = ["idle", "active", "speaking"]
CONTENT_TYPE_JSON: Final[str] = "application/json"
