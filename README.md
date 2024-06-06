

To access the Open Api UI you must use the follow link [Swagger UI](http://localhost:8080/docs)


Run the application locally with `uvicorn app.main:app --port=8080 --reload`



Alembic 

`alembic revision --autogenerate -m "Create a baseline migrations"`

`alembic upgrade head`