class Queries:
    CREATE_SURVEY_TABLE = """
    CREATE TABLE IF NOT EXISTS survey_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        visit_date DATE,
        instagram_name TEXT,
        food_rating INTEGER,
        cleanliness_rating INTEGER,
        extra_comments TEXT
    )
    """