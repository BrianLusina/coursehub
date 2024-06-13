from fastapi import APIRouter
from users.di import UserRepositoryDep


user_router = APIRouter(prefix="/api/users")


@user_router.post('/')
def users(user_repository: UserRepositoryDep):
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


@user_router.get('/')
def users(user_repository: UserRepositoryDep):
    users = user_repository.find_all()
    data = []
    for course in users:
        data.append(course.toDict())
    return data
