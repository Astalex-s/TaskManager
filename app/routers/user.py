from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"])


# Получение списка пользователей
@router.get('/')
async def all_users():
    pass


# Получение пользователя по его id
@router.get('/user_id')
async def usr_by_id():
    pass


# Создание нового пользователя
@router.post('/create')
async def create_user():
    pass


# Обновление данных пользователя
@router.put('/update')
async def update_user():
    pass


# Удаление выбранного пользователя
@router.delete('/delete')
async def delete_user():
    pass
