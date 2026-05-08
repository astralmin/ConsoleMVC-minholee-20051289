class User:
    """사용자 데이터와 비즈니스 로직을 담당하는 Model."""

    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(id={self.user_id}, name='{self.name}', email='{self.email}')"


class UserRepository:
    """User 데이터의 저장·조회·수정·삭제를 담당 (실제 앱에서는 DB 연동)."""

    def __init__(self):
        self._store: dict[int, User] = {}
        self._next_id = 1

    def add(self, name: str, email: str) -> User:
        user = User(self._next_id, name, email)
        self._store[self._next_id] = user
        self._next_id += 1
        return user

    def get(self, user_id: int) -> User | None:
        return self._store.get(user_id)

    def get_all(self) -> list[User]:
        return list(self._store.values())

    def update(self, user_id: int, name: str, email: str) -> User | None:
        user = self._store.get(user_id)
        if user is None:
            return None
        user.name = name
        user.email = email
        return user

    def delete(self, user_id: int) -> bool:
        if user_id not in self._store:
            return False
        del self._store[user_id]
        return True
