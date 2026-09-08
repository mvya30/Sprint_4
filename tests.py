import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_duplicate_name(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')

        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')

        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_too_long(self):
        collector = BooksCollector()
        long_name = 'А' * 41
        collector.add_new_book(long_name)

        assert long_name not in collector.books_genre

    @pytest.mark.parametrize(
    'name, genre',
    [
        ('Властелин колец', 'Фантастика'),
        ('Вий', 'Ужасы'),
        ('Ревизор', 'Комедии'),
    ]
)
    def test_set_book_genre_sets_valid_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    def test_set_book_genre_nonexistent_book(self):
        collector = BooksCollector()
        book_name = 'Несуществующая книга'
        genre = 'Комедии'
        collector.set_book_genre(book_name, genre)

        assert book_name not in collector.books_genre 

    def test_get_book_genre_existing(self):
        collector = BooksCollector()
        collector.add_new_book('Голова профессора Доуэля')
        collector.set_book_genre('Голова профессора Доуэля', 'Фантастика')

        assert collector.get_book_genre('Голова профессора Доуэля') == 'Фантастика'

    @pytest.mark.parametrize(
        'genre, expected_books',
        [('Фантастика', ['Властелин Колец', 'Марсианин', 'Солярис']),
         ('Комедии', ['Юмор', '12 стульев']),
         ('Ужасы',[]),
         ]
    )
    def test_get_with_specific_genre_returns_books(self, genre, expected_books):
        collector = BooksCollector()
        books = {
            'Властелин Колец': 'Фантастика',
            'Марсианин': 'Фантастика',
            'Солярис': 'Фантастика',
            'Юмор': 'Комедии',
            '12 стульев': 'Комедии',
        }
        for name, book_genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, book_genre)

        assert collector.get_books_with_specific_genre(genre) == expected_books


    def test_get_books_genre_returns_all_books_and_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детективы')

        assert collector.get_books_genre() == {'Десять негритят': 'Детективы'}

    def test_get_for_children_returns_books_with_child_friendly_genres(self):
        collector =BooksCollector()
        books = {'Дюна': 'Фантастика',
                 'Смешная книга': 'Комедии',
                 'Шерлок Холмс': 'Детективы',
                 'Страх': 'Ужасы',
        }

        for name, book_genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, book_genre)

        assert collector.get_books_for_children() == ['Дюна', 'Смешная книга']


    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Книга') 
        collector.add_book_in_favorites('Книга')

        assert 'Книга' in collector.favorites

    def test_add_book_in_favorites_already_exists(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 2') 
        collector.add_book_in_favorites('Книга 2')
        collector.add_book_in_favorites('Книга 2')

        assert collector.favorites.count('Книга 2') == 1


    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.delete_book_from_favorites('Шерлок Холмс')

        assert collector.favorites == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Шерлок Холмс')

        assert collector.get_list_of_favorites_books() == ['Дюна', 'Шерлок Холмс']
    