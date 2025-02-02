from testApp.repository.user import UserRepository
from testApp.services.user import UserService

def user_service():
    return UserService(UserRepository)


