from fastapi import HTTPException, status

UserAlReadyExistException = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Пользователь уже существует",
)

IncorrectTokenFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверный формат токена",
)

UnknownPhoto = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Попытка получения неизвестного фото"
)

UnknownVideo = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Попытка получения неизвестного видеопотока"
)