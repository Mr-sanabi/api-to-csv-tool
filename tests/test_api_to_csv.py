import csv
from types import SimpleNamespace

from src.api_client import fetch_users
from src.storage import save_csv
from src.transformer import extract_user_row


def test_transformer_handles_missing_nested_values():
    row = extract_user_row({"id": 1, "name": "Ada"})
    assert row["city"] is None
    assert row["company"] is None


def test_fetch_users_rejects_invalid_json(monkeypatch):
    response = SimpleNamespace(raise_for_status=lambda: None, json=lambda: (_ for _ in ()).throw(ValueError("bad json")))
    monkeypatch.setattr("src.api_client.requests.get", lambda *args, **kwargs: response)
    assert fetch_users("https://example.com/users") is None


def test_save_csv_creates_parent(tmp_path):
    path = tmp_path / "nested" / "users.csv"
    save_csv(path, [{"id": 1, "name": "Ada"}])
    with path.open(encoding="utf-8", newline="") as file:
        assert list(csv.DictReader(file))[0]["name"] == "Ada"
