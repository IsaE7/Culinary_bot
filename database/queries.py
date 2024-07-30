class Queries:
    CREATE_SURVEY_TABLE = """
    CREATE TABLE IF NOT EXISTS survey_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        visit_date DATE,
        instagram_name TEXT,
        food_rating TEXT,
        cleanliness_rating TEXT,
        extra_comments TEXT
    )
    """

    DROP_CATEGORIES = "DROP TABLE IF EXISTS CATEGORIES"

    CREATE_CATEGORIES_TABLE = """
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """

    POPULATE_CATEGORIES = """
    INSERT INTO categories (name) VALUES 
    ('Breakfasts'),
    ('Soups'),
    ('Basic'),
    ('Beverage')
    """

    DROP_DISHES = "DROP TABLE IF EXISTS dishes"

    CREATE_DISHES_TABLE = """
    CREATE TABLE IF NOT EXISTS dishes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price INTEGER,
        cover TEXT,
        categories_id INTEGER,
        FOREIGN KEY (categories_id) REFERENCES categories(id)
    )
    """

    POPULATE_DISHES = '''
        INSERT INTO dishes (name, price , cover, categories_id) VALUES 
        ("blinchiki", 100, "images/blinchiki.jpg", 1),
        ("borsch", 150, "images/borsch.jpg", 2),
        ("plov", 200, "images/plov.jpg", 3),
        ("ice cola", 80, "images/ice_kola.jpg", 4)
        '''

    GET_CATEGORIES = '''
        SELECT id, name FROM categories
    '''

    GET_RECIPES_BY_CATEGORY = '''
        SELECT name, price, cover FROM dishes WHERE cover = ?
    '''

    CREATE_USER_WARNINGS_TABLE = ('''
    CREATE TABLE IF NOT EXISTS user_warnings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        chat_id INTEGER,
        counter INTEGER DEFAULT 0
    )
    ''')
