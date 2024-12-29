# API 문서

## 사용자 인증 API

### 회원가입
- **URL**: `/accounts/signup/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "username": "username",
    "password": "password",
    "profile_image": "image_url"
  }
  ```
- **Response**:
  - `201 Created`: 회원가입 성공
  - `400 Bad Request`: 유효성 검사 실패

### 로그인
- **URL**: `/accounts/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "password"
  }
  ```
- **Response**:
  - `200 OK`: 로그인 성공, JWT 토큰 반환
  - `401 Unauthorized`: 인증 실패

### 로그아웃
- **URL**: `/accounts/logout/`
- **Method**: `POST`
- **Headers**: `Authorization: Bearer <token>`
- **Response**:
  - `200 OK`: 로그아웃 성공

### 프로필 조회
- **URL**: `/accounts/profile/`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer <token>`
- **Response**:
  - `200 OK`: 프로필 정보 반환

### 프로필 수정
- **URL**: `/accounts/profile/`
- **Method**: `PUT`
- **Headers**: `Authorization: Bearer <token>`
- **Request Body**:
  ```json
  {
    "username": "new_username",
    "profile_image": "new_image_url"
  }
  ```
- **Response**:
  - `200 OK`: 프로필 수정 성공

### 팔로우/언팔로우
- **URL**: `/accounts/<int:user_pk>/follow/`
- **Method**: `POST`
- **Headers**: `Authorization: Bearer <token>`
- **Response**:
  - `200 OK`: 팔로우/언팔로우 성공

## 제품 관리 API

### 제품 목록 조회
- **URL**: `/products/`
- **Method**: `GET`
- **Response**:
  - `200 OK`: 제품 목록 반환

### 제품 등록
- **URL**: `/products/`
- **Method**: `POST`
- **Headers**: `Authorization: Bearer <token>`
- **Request Body**:
  ```json
  {
    "title": "Product Title",
    "content": "Product Description",
    "image": "image_url"
  }
  ```
- **Response**:
  - `201 Created`: 제품 등록 성공

### 제품 상세 조회
- **URL**: `/products/<int:product_pk>/`
- **Method**: `GET`
- **Response**:
  - `200 OK`: 제품 상세 정보 반환

### 제품 수정
- **URL**: `/products/<int:product_pk>/`
- **Method**: `PUT`
- **Headers**: `Authorization: Bearer <token>`
- **Request Body**:
  ```json
  {
    "title": "Updated Title",
    "content": "Updated Description",
    "image": "updated_image_url"
  }
  ```
- **Response**:
  - `200 OK`: 제품 수정 성공

### 제품 삭제
- **URL**: `/products/<int:product_pk>/`
- **Method**: `DELETE`
- **Headers**: `Authorization: Bearer <token>`
- **Response**:
  - `204 No Content`: 제품 삭제 성공