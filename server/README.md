# 🏠 LocaDwell API

## 📝 Description

API for LocaDwell. LocaDwell is a web application that allows users to book rooms in hotels and leave reviews about their experience. The application is built using the Django REST Framework.

## 💻 Technology

| Technology            | Use                           |
| --------------------- | ----------------------------- |
| Python                | Main programming language     |
| Django                | Web framework                 |
| Django REST Framework | Toolkit for building Web APIs |
| SQLite3               | Database                      |
| SimpleJWT             | Authentication                |

## 🎁 Features

### 👥 User Management

-   **Register a new user:** Users can create a new account using their email.
-   **Login:** Users can log in to their account.
-   **Token Refresh:** Users can refresh their access token.
-   **Logout:** Users can log out from their account.
-   **Get user list:** Users can view the list of all users.
-   **Get user detail:** Users can view detailed information about a specific user.
-   **Update user details:** Users can update the details of their account.
-   **Delete a user:** Users can delete their account.

### 🏨 Room Management

-   **Get room list:** Users can view a list of available rooms.
-   **Get room detail:** Users can view detailed information about a specific room.
-   **Create a new room:** Admins can create new rooms.
-   **Update a room:** Admins can update the details of existing rooms.
-   **Delete a room:** Admins can delete rooms.

### 📅 Reservation Management

-   **Get reservation list:** Users can view a list of their reservations.
-   **Get reservation detail:** Users can view detailed information about a specific reservation.
-   **Create a new reservation:** Users can create new reservations.
-   **Update a reservation:** Users can update the details of their existing reservations.
-   **Delete a reservation:** Users can delete their reservations.
-   **Get reservations for a specific room:** Users can view all reservations for a specific room.
-   **Get reservations for a specific user:** Admins can view all reservations made by a specific user.

### 📝 Review Management

-   **Get review list:** Users can view a list of all reviews.
-   **Get review detail:** Users can view detailed information about a specific review.
-   **Create a new review:** Users can create new reviews.
-   **Update a review:** Users can update their existing reviews.
-   **Delete a review:** Users can delete their reviews.
-   **Get reviews for a specific room:** Users can view all reviews for a specific room.
-   **Get reviews for a specific user:** Users can view all reviews made by a specific user.

### 🖼️ Media Management

-   **Get media list:** Users can view a list of all media.
-   **Get media detail:** Users can view detailed information about a specific media.
-   **Create a new media:** Users can upload new media.
-   **Update a media:** Users can update the details of existing media.
-   **Delete a media:** Users can delete media.

## 🌐 API Endpoints

This section provides detailed information about the API endpoints of our application.

### User Management

| Method   | Endpoint                      | Description                    |
| -------- | ----------------------------- | ------------------------------ |
| `POST`   | `/api/users/register/`        | Register a new user            |
| `POST`   | `/api/users/login/`           | Login a user                   |
| `POST`   | `/api/users/logout/`          | Logout a user                  |
| `POST`   | `/api/users/token/refresh/`   | Refresh user token             |
| `GET`    | `/api/users/`                 | Get a list of all users        |
| `GET`    | `/api/users/<int:pk>/`        | Get details of a specific user |
| `PUT`    | `/api/users/<int:pk>/update/` | Update user details            |
| `DELETE` | `/api/users/<int:pk>/delete/` | Delete a user                  |

### Room Management

| Method   | Endpoint                      | Description                    |
| -------- | ----------------------------- | ------------------------------ |
| `GET`    | `/api/rooms/`                 | Get a list of all rooms        |
| `GET`    | `/api/rooms/<int:pk>/`        | Get details of a specific room |
| `POST`   | `/api/rooms/create/`          | Create a new room              |
| `PUT`    | `/api/rooms/<int:pk>/update/` | Update room details            |
| `DELETE` | `/api/rooms/<int:pk>/delete/` | Delete a room                  |

### Reservation Management

| Method   | Endpoint                             | Description                              |
| -------- | ------------------------------------ | ---------------------------------------- |
| `GET`    | `/api/reservations/`                 | Get a list of all reservations           |
| `GET`    | `/api/reservations/<int:pk>/`        | Get details of a specific reservation    |
| `POST`   | `/api/reservations/create/`          | Create a new reservation                 |
| `PUT`    | `/api/reservations/<int:pk>/update/` | Update reservation details               |
| `DELETE` | `/api/reservations/<int:pk>/delete/` | Delete a reservation                     |
| `GET`    | `/api/reservations/room/<int:pk>/`   | Get all reservations for a specific room |
| `GET`    | `/api/reservations/user/<int:pk>/`   | Get all reservations for a specific user |

### Review Management

| Method   | Endpoint                        | Description                         |
| -------- | ------------------------------- | ----------------------------------- |
| `GET`    | `/api/reviews/`                 | Get a list of all reviews           |
| `GET`    | `/api/reviews/<int:pk>/`        | Get details of a specific review    |
| `POST`   | `/api/reviews/create/`          | Create a new review                 |
| `PUT`    | `/api/reviews/<int:pk>/update/` | Update review details               |
| `DELETE` | `/api/reviews/<int:pk>/delete/` | Delete a review                     |
| `GET`    | `/api/reviews/room/<int:pk>/`   | Get all reviews for a specific room |
| `GET`    | `/api/reviews/user/<int:pk>/`   | Get all reviews for a specific user |

### Media Management

| Method   | Endpoint                      | Description                     |
| -------- | ----------------------------- | ------------------------------- |
| `GET`    | `/api/media/`                 | Get a list of all media         |
| `GET`    | `/api/media/<int:pk>/`        | Get details of a specific media |
| `POST`   | `/api/media/create/`          | Create a new media              |
| `PUT`    | `/api/media/<int:pk>/update/` | Update media details            |
| `DELETE` | `/api/media/<int:pk>/delete/` | Delete a media                  |

## 🚀 Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/ShokhrukhbekYuldoshev/locadwell
    ```

2. **Navigate to the `locadwell` directory:**

    ```bash
    cd locadwell
    ```
