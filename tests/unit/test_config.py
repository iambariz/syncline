import pytest
from pydantic import ValidationError

from syncline.config import Settings


def test_loads_from_explicit_values() -> None:
    settings = Settings(  # type: ignore[call-arg]
        _env_file=None,  # type: ignore[call-arg]
        source_token="pat-eu1-source",
        target_token="pat-eu1-target",
        api_key="secret",
    )
    assert settings.source_token == "pat-eu1-source"
    assert settings.migrations_dir == "migrations"


def test_reads_env_vars_with_prefix(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SYNCLINE_SOURCE_TOKEN", "pat-eu1-a")
    monkeypatch.setenv("SYNCLINE_TARGET_TOKEN", "pat-eu1-b")
    monkeypatch.setenv("SYNCLINE_API_KEY", "k")
    monkeypatch.setenv("SYNCLINE_MIGRATIONS_DIR", "elsewhere")

    settings = Settings(_env_file=None)  # type: ignore[call-arg]

    assert settings.target_token == "pat-eu1-b"
    assert settings.migrations_dir == "elsewhere"


def test_missing_required_settings_fail_fast(monkeypatch: pytest.MonkeyPatch) -> None:
    for var in ("SYNCLINE_SOURCE_TOKEN", "SYNCLINE_TARGET_TOKEN", "SYNCLINE_API_KEY"):
        monkeypatch.delenv(var, raising=False)

    with pytest.raises(ValidationError) as exc_info:
        Settings(_env_file=None)  # type: ignore[call-arg]

    missing = {error["loc"][0] for error in exc_info.value.errors()}
    assert missing == {"source_token", "target_token", "api_key"}
