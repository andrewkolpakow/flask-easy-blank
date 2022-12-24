from dao.genre import GenreDAO

class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)
    '''Получаем ключ из view и передаем методу dao для получения данных о жанре по ключу'''

    def get_all(self):
        return self.dao.get_all()
    '''Получаем данные из БД о всех жанрах'''