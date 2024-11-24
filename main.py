import sqlite3


def initialize_db():
    conn = sqlite3.connect('posts.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            author TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(post_id) REFERENCES posts(id)
        )
    ''')

    conn.commit()
    conn.close()


def add_post(title, content, author):
    conn = sqlite3.connect('posts.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO posts (title, content, author) VALUES (?, ?, ?)
    ''', (title, content, author))

    conn.commit()
    conn.close()


def get_posts():
    conn = sqlite3.connect('posts.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM posts')
    posts = cursor.fetchall()

    conn.close()
    return posts


# Функция для добавления комментария
def add_comment(post_id, content, author):
    conn = sqlite3.connect('posts.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO comments (post_id, content, author) VALUES (?, ?, ?)
    ''', (post_id, content, author))

    conn.commit()
    conn.close()


# Функция для получения комментариев к посту
def get_comments(post_id):
    conn = sqlite3.connect('posts.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM comments WHERE post_id = ?', (post_id,))
    comments = cursor.fetchall()

    conn.close()
    return comments


# Инициализация базы данных
initialize_db()

# Пример добавления поста
#add_post('Как получить премию', 'Как получить премию за победу в олимпиаде.', 'МистерВалера')

# Пример добавления комментариев
#add_comment(3, 'Никак.', 'Анонимус')
#add_comment(3, 'Напиши сюда @TochnoNeSkam.', 'Главный')

# Пример получения и отображения всех постов
for post in get_posts():
    print(f'ID поста: {post[0]}, Заголовок: {post[1]}, Автор: {post[3]}, Создан: {post[4]}')

    # Получение и отображение комментариев
    comments = get_comments(post[0])
    for comment in comments:
        print(f'\tКомментарий ID: {comment[0]}, Содержимое: {comment[2]}, Автор: {comment[3]}, Создан: {comment[4]}')