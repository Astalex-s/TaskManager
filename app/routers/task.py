from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["task"])


# Получение всего списка задач
@router.get('/')
async def all_task():
    pass


# Получение задачи по её id
@router.get('/task_id')
async def task_by_id():
    pass


# Создание новой задачи
@router.post('/create')
async def create_task():
    pass


# Изменение.обновление задачи
@router.put('/update')
async def update_task():
    pass


# Удаление выбраной задачи
@router.delete('/delete')
async def delete_task():
    pass
