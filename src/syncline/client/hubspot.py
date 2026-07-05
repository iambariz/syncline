import httpx

from syncline.domain.models import PropertyDefinition


class HubSpotClient:
    def __init__(self, token: str, base_url: str = "https://api.hubapi.com") -> None:
        self._http = httpx.Client(base_url=base_url, headers={"Authorization": f"Bearer {token}"})

    def get_properties(self, object_type: str) -> list[PropertyDefinition]:
        response = self._http.get(f"/crm/v3/properties/{object_type}")
        response.raise_for_status()
        return [PropertyDefinition.model_validate(raw) for raw in response.json()["results"]]
