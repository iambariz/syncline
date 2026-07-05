from syncline.client.hubspot import HubSpotClient
from syncline.config import Settings

settings = Settings()  # type: ignore[call-arg]
client = HubSpotClient(settings.source_token)
props = client.get_properties("contacts")
print(f"{len(props)} contact properties")
for prop in props[:10]:
    print(prop["name"], "|", prop["type"], "|", prop["label"])