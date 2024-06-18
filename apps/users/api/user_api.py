from typing import Annotated
from fastapi import APIRouter, Form
from users.di import CreateUserDep
from users.domain import CreateUserRequest


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
    except Exception:
        pass
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
def login(user_repository: UserRepositoryDep):
    users = user_repository.find_all()
    data = []
    for course in users:
        data.append(course.toDict())
    return data


@user_router.get('/')
def users(user_repository: UserRepositoryDep):
    users = user_repository.find_all()
    data = []
    for course in users:
        data.append(course.toDict())
    return data


