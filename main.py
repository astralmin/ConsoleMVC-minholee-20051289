import sys
from pathlib import Path

# 패키지 루트를 sys.path에 추가 (직접 실행 시 필요)
sys.path.insert(0, str(Path(__file__).parent))

from models.user import UserRepository
from views.user_view import UserView
from controllers.user_controller import UserController


def main():
    repository = UserRepository()
    view = UserView()
    controller = UserController(repository, view)

    # 초기 샘플 데이터
    repository.add("홍길동", "hong@example.com")
    repository.add("김철수", "kim@example.com")

    controller.run()


if __name__ == "__main__":
    main()
