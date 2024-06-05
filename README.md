# PaperConf API

PaperConf is a RESTful API for managing academic conferences, papers, reviewers, and reviews. It provides endpoints for performing various actions such as user registration, paper submission, reviewer assignment, and review submission.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-repo/paperconf.git
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Make migations:

   ```
   python manage.py makemigrations
   ```

4. Set up the database:

   ```
   python manage.py migrate
   ```

5. Run the development server:

   ```
   python manage.py runserver
   ```

6. The API will be accessible at `http://localhost:8000/api/`.

## API Endpoints

### Users

`POST /api/user/register/`: Register a new user.
`POST /api/user/login/`: Log in with existing credentials.
`POST /api/user/logout/`: Log out the current user.
`GET /api/user/info/`: Retrieve details of the logged-in user.

### Conferences

`POST /api/conferences/conf/new`: Create a new conference.
`GET /api/conferences/`: List all conferences.
`GET /api/conferences/conf/<str:conf>/`: Retrieve details of a specific conference.
`PUT /api/conferences/conf/<str:conf>/`: Update details of a conference.
`DELETE /api/conferences/conf/<str:conf>/`: Delete a conference.

### Papers

`POST /api/papers/conf/<str:conf>/paper/new/`: Submit a new paper.
`GET /api/papers/user/`: List all papers.
`GET /api/papers/user/paper/<int:pk>/`: Retrieve details of a specific paper.
`PUT /api/papers/user/paper/<int:pk>/`: Update details of a paper.
`DELETE /api/papers/user/paper/<int:pk>/`: Delete a paper.

### Reviews

`POST /api/reviews/conf/<str:conf>/paper/<int:pk>/review/create/`: Submit a new review for a paper.
`GET /api/reviews/conf/<str:conf>/paper/<int:pk>/`: List all reviews.
`GET /api/reviews/conf/<str:conf>/paper/<int:pk>/review/<int:review_pk>/`: Retrieve details of a specific review.
`PUT /api/reviews/conf/<str:conf>/paper/<int:pk>/review/<int:review_pk>/`: Update details of a review.
`DELETE /api/reviews/conf/<str:conf>/paper/<int:pk>/review/<int:review_pk>/`: Delete a review.

## Authentication

Authentication is required for most endpoints. Use the token received upon successful login for authentication by including it in the Authorization header of your requests:

```
Authorization: Bearer <access_token>
```

## Feedback and Support

If you encounter any issues or have suggestions for improvement, please open an issue on GitHub. We welcome your feedback and contributions!

## License

This project is licensed under the [MIT License](https://github.com/babypluto-ai/paperconf/blob/updates/LICENSE).
