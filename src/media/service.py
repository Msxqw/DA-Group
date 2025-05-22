from src.Service.base import BaseService
from src.db.domain.models import Photo

class PhotoServer(BaseService):
    model = Photo
