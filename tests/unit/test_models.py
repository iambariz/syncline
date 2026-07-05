from syncline.domain.models import PropertyDefinition, filter_managed


def make_property(**overrides: object) -> PropertyDefinition:
    defaults: dict[str, object] = {
        "name": "lead_score",
        "label": "Lead Score",
        "type": "number",
        "fieldType": "number",
        "groupName": "contactinformation",
    }
    return PropertyDefinition.model_validate({**defaults, **overrides})


def test_custom_property_is_managed() -> None:
    assert make_property().is_managed


def test_hubspot_defined_property_is_not_managed() -> None:
    assert not make_property(hubspotDefined=True).is_managed


def test_calculated_property_is_not_managed() -> None:
    assert not make_property(calculated=True).is_managed


def test_filter_managed_keeps_only_custom_properties() -> None:
    props = [
        make_property(name="custom_one"),
        make_property(name="email", hubspotDefined=True),
        make_property(name="score", calculated=True),
    ]

    managed = filter_managed(props)

    assert [p.name for p in managed] == ["custom_one"]
