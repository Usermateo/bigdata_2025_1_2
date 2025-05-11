import sqlite3

# Crear/conectar a la base de datos
conn = sqlite3.connect("premier_league.db")
cursor = conn.cursor()

# Crear tabla raw_data
cursor.execute("""
CREATE TABLE IF NOT EXISTS raw_data (
    id INTEGER PRIMARY KEY,
    matchday INTEGER,
    date TEXT,
    time TEXT,
    home_team TEXT,
    home_score INTEGER,
    home_xg REAL,
    away_score INTEGER,
    away_xg REAL,
    away_team TEXT,
    attendance INTEGER,
    referee TEXT,
    stadium TEXT,
    result TEXT,
    aditional_stats TEXT           
);
""")

# Crear tabla processed_data
cursor.execute("""
CREATE TABLE IF NOT EXISTS processed_data (
    id INTEGER PRIMARY KEY,
    season TEXT,
    home_team TEXT,
    away_team TEXT,
    home_score INTEGER,
    away_score INTEGER,
    goal_difference INTEGER,
    winner TEXT,
    home_xg REAL,
    away_xg REAL,
    xg_difference REAL,
    match_result TEXT
);
""")

# Crear tabla report_view
cursor.execute("""
CREATE TABLE IF NOT EXISTS report_view (
    team TEXT PRIMARY KEY,
    total_matches INTEGER,
    wins INTEGER,
    draws INTEGER,
    losses INTEGER,
    goals_for INTEGER,
    goals_against INTEGER,
    goal_difference INTEGER,
    avg_attendance REAL,
    avg_xg_for REAL,
    avg_xg_against REAL,
    win_rate REAL
);
""")

# Confirmar y cerrar conexión
conn.commit()
conn.close()