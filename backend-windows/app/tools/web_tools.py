import httpx
from typing import Optional, Dict
from app.logging.logger import logger


class WebTools:
    def __init__(self):
        self._client = None

    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(timeout=30.0, follow_redirects=True)
        return self._client

    async def search(self, query: str, num_results: int = 5) -> dict:
        try:
            client = await self._get_client()
            response = await client.get(
                "https://api.duckduckgo.com/",
                params={"q": query, "format": "json", "no_html": 1, "skip_disambig": 1}
            )

            if response.status_code == 200:
                data = response.json()
                return {
                    "success": True,
                    "query": query,
                    "results": data.get("RelatedTopics", [])[:num_results],
                    "abstract": data.get("Abstract", ""),
                    "source": "duckduckgo"
                }
            else:
                return {"success": False, "error": f"Search failed: {response.status_code}"}
        except Exception as e:
            logger.error(f"Web search failed: {e}")
            return {"success": False, "error": str(e)}

    async def http_request(self, url: str, method: str = "GET", headers: Optional[Dict] = None,
                          body: Optional[Dict] = None) -> dict:
        try:
            client = await self._get_client()

            response = await client.request(
                method=method.upper(),
                url=url,
                headers=headers or {},
                json=body if method.upper() in ("POST", "PUT", "PATCH") else None
            )

            content_type = response.headers.get("content-type", "")
            if "application/json" in content_type:
                data = response.json()
            else:
                data = response.text[:10000]

            return {
                "success": True,
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "data": data
            }
        except Exception as e:
            logger.error(f"HTTP request failed: {e}")
            return {"success": False, "error": str(e)}

    async def close(self):
        if self._client and not self._client.is_closed:
            await self._client.aclose()
