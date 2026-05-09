import pytest

@pytest.fixture
def sample_users():
    print("[fixture: setup]")
    return [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]

def test_first_user(sample_users):
    assert sample_users[0]["name"] == "Alice"

def test_count(sample_users):
    assert len(sample_users) == 2

@pytest.fixture
def temp_file(tmp_path):
    p = tmp_path / "data.txt"
    p.write_text("hello", encoding="utf-8")
    return p

def test_file_content(temp_file):
    assert temp_file.read_text(encoding="utf-8") == "hello"
