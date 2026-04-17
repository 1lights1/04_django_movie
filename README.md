# 🎬 영화 추천 커뮤니티 서비스 (04-pjt)

## 📌 프로젝트 개요

Django를 활용하여 영화 데이터를 생성(Create), 조회(Read), 수정(Update), 삭제(Delete)할 수 있는 웹 애플리케이션을 구현하였다.
사용자는 영화 정보를 등록하고, 목록을 확인하며, 상세 정보를 조회 및 수정/삭제할 수 있다.

---

## 🎯 프로젝트 목표

* Django Model과 ORM 이해
* CRUD 기능 구현
* 사용자 입력 검증 (Form 활용)
* URL 설계 및 유지보수 고려
* HTTP Method 제한 적용
* 협업을 통한 Git 브랜치 전략 경험

---

## 🛠️ 개발 환경

* Python 3.11
* Django 5.2
* HTML / CSS (Bootstrap 5)
* Git / GitHub / GitLab

---

## 📁 프로젝트 구조

```
mypjt/
 ├── mypjt/
 │    ├── settings.py
 │    ├── urls.py
 │
 ├── movies/
 │    ├── models.py
 │    ├── forms.py
 │    ├── views.py
 │    ├── urls.py
 │    ├── templates/
 │         └── movies/
 │             ├── base.html
 │             ├── index.html
 │             ├── detail.html
 │             ├── create.html
 │             └── update.html
 │
 ├── manage.py
 ├── requirements.txt
```

---

## ⚙️ 기능 구현

### ✅ F401 프로젝트 구성

* Django 프로젝트 및 앱 생성

### ✅ F402 Model Class

```python
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    director = models.CharField(max_length=50)
```

---

### ✅ F403 Form Class

```python
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
```

---

### ✅ F404 index (전체 조회)

* 모든 영화 목록 출력
* 카드 UI로 시각화

---

### ✅ F405 create (생성)

* GET: 입력 폼 제공
* POST: 데이터 검증 후 저장

---

### ✅ F406 detail (상세 조회)

* 선택한 영화 정보 출력
* 수정 / 삭제 기능 제공

---

### ✅ F407 update (수정)

* 기존 데이터 자동 입력
* POST 시 수정 반영

---

### ✅ F408 delete (삭제)

* POST 요청으로 삭제
* 삭제 후 index로 이동

---

### ⭐ F409 AI 기능 (선택)

* 생성형 AI API를 활용하여 감독 정보 생성
* 감독 프로필 및 대표작 데이터 저장

---

## 🔐 비기능적 요구사항

### ✅ NF401 URL 유지보수

* `app_name`과 `name`을 활용하여 URL 관리

### ✅ NF402 HTTP Method 제한

* GET / POST 요청을 구분하여 처리

---

## 🎨 UI 개선 사항

* Bootstrap Grid 시스템 적용
* 카드형 UI로 영화 목록 구현
* truncate 필터로 긴 텍스트 제한
* 버튼 및 레이아웃 개선

---

## 👥 협업 방식

### 🔹 브랜치 전략

```
develop
 ├── feature/setup-project
 ├── feature/model-form
 ├── feature/read-delete
 ├── feature/create-update
 └── feature/ai-feature
```

---

### 🔹 역할 분담

| 역할 | 담당 기능                              |
| -- | ---------------------------------- |
| A  | Model, Form, index, detail, delete |
| B  | create, update, UI, AI 기능          |

---

### 🔹 협업 흐름

1. feature 브랜치에서 작업
2. develop 브랜치로 병합
3. 통합 테스트 진행
4. 최종 main 브랜치 병합

---

## ⚠️ 어려웠던 점

* HTTP Method 제한 처리
* 템플릿 상속 구조 설계
* Git 브랜치 충돌 방지
* 협업 시 역할 분리

---

## 💡 배운 점

* Django의 MVT 구조 이해
* ModelForm을 활용한 데이터 검증
* Git 브랜치 전략의 중요성
* 협업 시 코드 구조 설계의 필요성

---

## 🚀 실행 방법

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 📌 결과

* CRUD 기능 완전 구현
* 사용자 친화적 UI 구성
* 협업 기반 프로젝트 완성

```
```
