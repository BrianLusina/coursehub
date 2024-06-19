from typing import Annotated
from fastapi import APIRouter, Form
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from apps.users.di.domain_providers import CreateUserDep
from apps.users.domain import CreateUserRequest


user_router = APIRouter(prefix="/api/users")


@user_router.post('/signup')
async def signup(
    email: Annotated[str, Form()],
    name: Annotated[str, Form()], 
    password: Annotated[str, Form()],
    create_user: CreateUserDep
):
    create_user_request = CreateUserRequest(
        email=email,
        name=name,
        password=password
    )
    
    try:
        created_user = await create_user.execute(create_user_request)
        return {
            "status": HTTP_201_CREATED,
            "data": created_user,
            "message": "Successfully created user"
        }
    except Exception as exc:
        return {
            "status": HTTP_400_BAD_REQUEST,
            "message": "Failed to create user",
            "error": exc
        }
    # email = request.form.get('email')
    # name = request.form.get('name')
    # password = request.form.get('password')
    # user = User.query.filter_by(email=email).first()
    # if user: 
    #     return None
    # new_user = User(email=email, name=name,
    #                 password=generate_password_hash(password, method='sha256'))
    # db.session.add(new_user)
    # db.session.commit()
    # response = jsonify(new_user.toDict())
    # response.status_code = 200
    # return response


@user_router.post('/login')
def login(user_repository):
    users = user_repository.find_all()
    data = []
    for course in users:
        data.append(course.toDict())
    return data


@user_router.get('/')
def users(user_repository):
    users = user_repository.find_all()
    data = []
    for course in users:
        data.append(course.toDict())
    return data


