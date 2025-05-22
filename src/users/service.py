from src.Service.base import BaseService
from src.db.domain.models import User

class UserService(BaseService):
    model = User