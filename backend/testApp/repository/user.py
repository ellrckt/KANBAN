from testApp.utils.repository import SQLAlchemyRepository
from testApp.models.user import User


class UserRepository(SQLAlchemyRepository):
    model = User
