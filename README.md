# consolemvc

Python MVC 패턴 스켈레톤 프로젝트입니다. Model / Controller / View 패키지 구조와 역할 분리를 확인하기 위한 콘솔 애플리케이션입니다.

## 파일 구조

```
consolemvc/
├── main.py                          # 진입점 — 의존성 조립(DI)만 담당
├── models/
│   ├── __init__.py
│   └── user.py                      # User 데이터 클래스 + UserRepository (저장/조회/수정/삭제)
├── views/
│   ├── __init__.py
│   └── user_view.py                 # 출력 전담 — 비즈니스 로직 없음
└── controllers/
    ├── __init__.py
    └── user_controller.py           # 입력 처리 + Model/View 연결 + 흐름 제어
```

## 역할 분리 포인트

| 계층 | 파일 | 책임 |
|------|------|------|
| **Model** | `models/user.py` | 데이터 구조 정의 + CRUD 로직. View/Controller 참조 없음 |
| **View** | `views/user_view.py` | 화면 출력 + 사용자 입력 수집. 계산 없음 |
| **Controller** | `controllers/user_controller.py` | Model 호출 → View 렌더링 순서 제어. 양쪽을 주입받아 조율 |
| **Entry point** | `main.py` | 세 계층을 인스턴스화해서 연결 (의존성 주입) |

## 실행

```powershell
python main.py
```
