from dao.movie import MovieDAO
'''Импортируем паттерн для сохранения данных бизнес логики в БД'''

class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)
    '''Получаем ключ из view и передаем методу dao для получения данных о фильме по ключу'''

    def get_all(self, filters):
        if filters.get('director_id') is not None:
            movies = self.dao.get_by_director_id(filters.get('director_id'))
        elif filters.get('genre_id') is not None:
            movies = self.dao.get_by_genre_id(filters.get('genre_id'))
        elif filters.get('year') is not None:
            movies = self.dao.get_by_year(filters.get('year'))
        else:
            movies = self.dao.get_all()

        return movies
        '''Получаем через view-filter данные запроса и выдаем данные о фильме'''

    def create(self, movie_d):
        return self.dao.create(movie_d)
        '''Получаем данные (словарь) о новом фильме и сохраняем в БД через dao create movie'''

    def update(self, movie_d):
        self.dao.update(movie_d)
        return self.dao
        '''Получаем данные для обновления фильма в формате словаря, обращаемся к БД через dao update'''

    def delete(self, bid):
        self.dao.delete(bid)
        '''Удаляем фильм из БД по идентификатору через dao.delete'''
