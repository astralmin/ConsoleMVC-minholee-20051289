from models.user import User


class UserView:
    """사용자 관련 출력을 담당하는 View. 비즈니스 로직 없이 표시만 수행."""

    def show_user(self, user: User) -> None:
        print(f"[사용자] ID={user.user_id} | 이름={user.name} | 이메일={user.email}")

    def show_user_list(self, users: list[User]) -> None:
        if not users:
            print("등록된 사용자가 없습니다.")
            return
        print("=" * 45)
        print(f"{'ID':>4}  {'이름':<12}  {'이메일'}")
        print("-" * 45)
        for user in users:
            print(f"{user.user_id:>4}  {user.name:<12}  {user.email}")
        print("=" * 45)

    def show_success(self, message: str) -> None:
        print(f"[성공] {message}")

    def show_error(self, message: str) -> None:
        print(f"[오류] {message}")

    def show_menu(self) -> None:
        print("\n--- 사용자 관리 메뉴 ---")
        print("1. 사용자 목록 조회")
        print("2. 사용자 추가")
        print("3. 사용자 수정")
        print("4. 사용자 삭제")
        print("0. 종료")

    def prompt(self, label: str) -> str:
        return input(f"{label}: ").strip()
