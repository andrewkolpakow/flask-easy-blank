# файл для создания DAO и сервисов чтобы импортировать их везде
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO

from service.movie import MovieService
from service.genre import GenreService
from service.director import DirectorService

from setup_db import db

director_dao = DirectorDAO(session=db.session)
'''Создаем экземпляр класса DirectorDAO для упрощения импорта'''

genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)