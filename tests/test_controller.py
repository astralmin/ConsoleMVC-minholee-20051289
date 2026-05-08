import pytest
from unittest.mock import MagicMock, call
from models.user import User, UserRepository
from controllers.user_controller import UserController


@pytest.fixture
def repo():
    return UserRepository()


@pytest.fixture
def mock_view():
    return MagicMock()


@pytest.fixture
def ctrl(repo, mock_view):
    return UserController(repo, mock_view)


class TestListUsers:
    def test_empty_list(self, ctrl, mock_view):
        ctrl.list_users()
        mock_view.show_user_list.assert_called_once_with([])

    def test_with_users(self, ctrl, repo, mock_view):
        repo.add("홍길동", "hong@example.com")
        ctrl.list_users()
        users = mock_view.show_user_list.call_args[0][0]
        assert len(users) == 1
        assert users[0].name == "홍길동"


class TestCreateUser:
    def test_success(self, ctrl, repo, mock_view):
        mock_view.prompt.side_effect = ["홍길동", "hong@example.com"]
        ctrl.create_user()
        assert len(repo.get_all()) == 1
        mock_view.show_success.assert_called_once()
        mock_view.show_user.assert_called_once()

    def test_empty_name_shows_error(self, ctrl, repo, mock_view):
        mock_view.prompt.side_effect = ["", "hong@example.com"]
        ctrl.create_user()
        assert len(repo.get_all()) == 0
        mock_view.show_error.assert_called_once()

    def test_empty_email_shows_error(self, ctrl, repo, mock_view):
        mock_view.prompt.side_effect = ["홍길동", ""]
        ctrl.create_user()
        assert len(repo.get_all()) == 0
        mock_view.show_error.assert_called_once()


class TestUpdateUser:
    def test_success(self, ctrl, repo, mock_view):
        repo.add("홍길동", "hong@example.com")
        mock_view.prompt.side_effect = ["1", "홍길동(수정)", "new@example.com"]
        ctrl.update_user()
        assert repo.get(1).name == "홍길동(수정)"
        mock_view.show_success.assert_called_once()

    def test_invalid_id_format(self, ctrl, mock_view):
        mock_view.prompt.side_effect = ["abc"]
        ctrl.update_user()
        mock_view.show_error.assert_called_once()

    def test_nonexistent_id(self, ctrl, mock_view):
        mock_view.prompt.side_effect = ["999"]
        ctrl.update_user()
        mock_view.show_error.assert_called_once()


class TestDeleteUser:
    def test_success(self, ctrl, repo, mock_view):
        repo.add("홍길동", "hong@example.com")
        mock_view.prompt.return_value = "1"
        ctrl.delete_user()
        assert repo.get(1) is None
        mock_view.show_success.assert_called_once()

    def test_invalid_id_format(self, ctrl, mock_view):
        mock_view.prompt.return_value = "abc"
        ctrl.delete_user()
        mock_view.show_error.assert_called_once()

    def test_nonexistent_id(self, ctrl, mock_view):
        mock_view.prompt.return_value = "999"
        ctrl.delete_user()
        mock_view.show_error.assert_called_once()


class TestRun:
    def test_exit_on_zero(self, ctrl, mock_view, capsys):
        mock_view.prompt.return_value = "0"
        ctrl.run()
        mock_view.show_menu.assert_called_once()

    def test_invalid_choice_shows_error(self, ctrl, mock_view):
        mock_view.prompt.side_effect = ["9", "0"]
        ctrl.run()
        mock_view.show_error.assert_called_once()
