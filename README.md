
# Online Learing Platform (OLP)

This repository contains the backend system for an online learning platform. The system is developed using Django and PostgreSQL as the database management system.

Setup Instructions

Clone the Repository:
```bash
git clone https://github.com/Raghib6/OLP.git
```
Install Dependencies:

Navigate to the project directory and install the required Python dependencies using pip:

```bash
pip install -r requirements.txt
```
Run the Application:
```bash
python manage.py runserver
```
The application should now be accessible at 
```bash
http://localhost:8000
```


## API Reference

#### Get all courses

```http
  GET /api/courses
```

#### Filter courses by different properties

```http
  GET /api/courses/?instructor=Abrar
```


#### Retrieve a specific courses

```http
  GET /api/courses/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. Id of course to fetch |


#### Create a course

```http
  POST /api/courses/create/
```

#### Enroll into a course

```http
  POST /api/enrollments/
```



