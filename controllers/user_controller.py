from models.user import UserRepository
from views.user_view import UserView


class UserController:
    """Model과 View를 연결하는 Controller. 입력 처리·흐름 제어를 담당."""

    def __init__(self, repository: UserRepository, view: UserView):
        self._repo = repository
        self._view = view

    def list_users(self) -> None:
        users = self._repo.get_all()
        self._view.show_user_list(users)

    def create_user(self) -> None:
        name = self._view.prompt("이름")
        email = self._view.prompt("이메일")
        if not name or not email:
            self._view.show_error("이름과 이메일은 필수 입력값입니다.")
            return
        user = self._repo.add(name, email)
        self._view.show_success(f"사용자가 추가되었습니다.")
        self._view.show_user(user)

    def update_user(self) -> None:
        raw_id = self._view.prompt("수정할 사용자 ID")
        if not raw_id.isdigit():
            self._view.show_error("유효한 ID를 입력하세요.")
            return
        user = self._repo.get(int(raw_id))
        if user is None:
            self._view.show_error(f"ID {raw_id}에 해당하는 사용자가 없습니다.")
            return
        self._view.show_user(user)
        name = self._view.prompt("새 이름")
        email = self._view.prompt("새 이메일")
        updated = self._repo.update(int(raw_id), name, email)
        self._view.show_success("사용자 정보가 수정되었습니다.")
        self._view.show_user(updated)

    def delete_user(self) -> None:
        raw_id = self._view.prompt("삭제할 사용자 ID")
        if not raw_id.isdigit():
            self._view.show_error("유효한 ID를 입력하세요.")
            return
        ok = self._repo.delete(int(raw_id))
        if ok:
            self._view.show_success(f"ID {raw_id} 사용자가 삭제되었습니다.")
        else:
            self._view.show_error(f"ID {raw_id}에 해당하는 사용자가 없습니다.")

    def run(self) -> None:
        actions = {
            "1": self.list_users,
            "2": self.create_user,
            "3": self.update_user,
            "4": self.delete_user,
        }
        while True:
            self._view.show_menu()
            choice = self._view.prompt("선택")
            if choice == "0":
                print("종료합니다.")
                break
            action = actions.get(choice)
            if action:
                action()
            else:
                self._view.show_error("잘못된 메뉴 선택입니다.")
