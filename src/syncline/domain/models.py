from collections.abc import Iterable

from pydantic import BaseModel, ConfigDict, Field


class EnumOption(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    label: str
    value: str
    display_order: int = Field(alias="displayOrder", default=0)
    hidden: bool = False


class PropertyDefinition(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    label: str
    type: str
    field_type: str = Field(alias="fieldType")
    group_name: str = Field(alias="groupName")
    description: str = ""
    display_order: int = Field(alias="displayOrder", default=-1)
    options: list[EnumOption] = []
    hubspot_defined: bool = Field(alias="hubspotDefined", default=False)
    calculated: bool = False

    @property
    def is_managed(self) -> bool:
        """User-defined custom properties are the only ones syncline manages."""
        return not self.hubspot_defined and not self.calculated


def filter_managed(props: Iterable[PropertyDefinition]) -> list[PropertyDefinition]:
    return [p for p in props if p.is_managed]


class PropertyGroup(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    label: str
    display_order: int = Field(alias="displayOrder", default=0)
