import pytest
from models.user import User
from views.user_view import UserView


@pytest.fixture
def view():
    return UserView()


class TestUserViewOutput:
    def test_show_user(self, view, capsys):
        user = User(1, "홍길동", "hong@example.com")
        view.show_user(user)
        out = capsys.readouterr().out
        assert "1" in out
        assert "홍길동" in out
        assert "hong@example.com" in out

    def test_show_user_list(self, view, capsys):
        users = [
            User(1, "홍길동", "hong@example.com"),
            User(2, "김철수", "kim@example.com"),
        ]
        view.show_user_list(users)
        out = capsys.readouterr().out
        assert "홍길동" in out
        assert "김철수" in out

    def test_show_user_list_empty(self, view, capsys):
        view.show_user_list([])
        out = capsys.readouterr().out
        assert "없습니다" in out

    def test_show_success(self, view, capsys):
        view.show_success("처리 완료")
        out = capsys.readouterr().out
        assert "성공" in out
        assert "처리 완료" in out

    def test_show_error(self, view, capsys):
        view.show_error("잘못된 입력")
        out = capsys.readouterr().out
        assert "오류" in out
        assert "잘못된 입력" in out

    def test_show_menu(self, view, capsys):
        view.show_menu()
        out = capsys.readouterr().out
        assert "1" in out
        assert "2" in out
        assert "0" in out


class TestUserViewInput:
    def test_prompt_returns_stripped_input(self, view, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "  홍길동  ")
        result = view.prompt("이름")
        assert result == "홍길동"

    def test_prompt_label_passed_to_input(self, view, monkeypatch):
        received = {}
        monkeypatch.setattr("builtins.input", lambda prompt: received.update({"p": prompt}) or "값")
        view.prompt("이름")
        assert "이름" in received["p"]
