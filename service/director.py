from dao.director import DirectorDAO

class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)
    '''Получаем ключ из view и передаем методу dao для получения данных о режиссере по ключу'''

    def get_all(self):
        return self.dao.get_all()
    '''Получаем данные из БД о всех режиссерах'''

