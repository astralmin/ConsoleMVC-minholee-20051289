import pytest
from models.user import User, UserRepository


class TestUser:
    def test_attributes(self):
        user = User(1, "홍길동", "hong@example.com")
        assert user.user_id == 1
        assert user.name == "홍길동"
        assert user.email == "hong@example.com"

    def test_repr(self):
        user = User(1, "홍길동", "hong@example.com")
        assert "1" in repr(user)
        assert "홍길동" in repr(user)
        assert "hong@example.com" in repr(user)


class TestUserRepository:
    @pytest.fixture
    def repo(self):
        return UserRepository()

    def test_add_returns_user(self, repo):
        user = repo.add("홍길동", "hong@example.com")
        assert isinstance(user, User)
        assert user.user_id == 1
        assert user.name == "홍길동"
        assert user.email == "hong@example.com"

    def test_add_auto_increments_id(self, repo):
        u1 = repo.add("홍길동", "hong@example.com")
        u2 = repo.add("김철수", "kim@example.com")
        assert u1.user_id == 1
        assert u2.user_id == 2

    def test_get_existing(self, repo):
        repo.add("홍길동", "hong@example.com")
        user = repo.get(1)
        assert user is not None
        assert user.name == "홍길동"

    def test_get_nonexistent_returns_none(self, repo):
        assert repo.get(999) is None

    def test_get_all_empty(self, repo):
        assert repo.get_all() == []

    def test_get_all_returns_all(self, repo):
        repo.add("홍길동", "hong@example.com")
        repo.add("김철수", "kim@example.com")
        users = repo.get_all()
        assert len(users) == 2

    def test_update_existing(self, repo):
        repo.add("홍길동", "hong@example.com")
        updated = repo.update(1, "홍길동(수정)", "new@example.com")
        assert updated.name == "홍길동(수정)"
        assert updated.email == "new@example.com"

    def test_update_reflects_in_get(self, repo):
        repo.add("홍길동", "hong@example.com")
        repo.update(1, "홍길동(수정)", "new@example.com")
        assert repo.get(1).name == "홍길동(수정)"

    def test_update_nonexistent_returns_none(self, repo):
        assert repo.update(999, "없음", "none@example.com") is None

    def test_delete_existing(self, repo):
        repo.add("홍길동", "hong@example.com")
        assert repo.delete(1) is True
        assert repo.get(1) is None

    def test_delete_nonexistent_returns_false(self, repo):
        assert repo.delete(999) is False

    def test_delete_reduces_count(self, repo):
        repo.add("홍길동", "hong@example.com")
        repo.add("김철수", "kim@example.com")
        repo.delete(1)
        assert len(repo.get_all()) == 1
