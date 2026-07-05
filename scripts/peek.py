from syncline.client.hubspot import HubSpotClient
from syncline.config import Settings
from syncline.domain.models import filter_managed

settings = Settings()  # type: ignore[call-arg]
client = HubSpotClient(settings.source_token)
props = client.get_properties("contacts")
custom = filter_managed(props)
print(f"{len(props)} total, {len(custom)} managed")
