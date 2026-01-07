
CREATE TABLE IF NOT EXISTS crime_incidents
(
    incident_id INTEGER PRIMARY KEY,
    crime_type TEXT NOT NULL,
    crime_category TEXT,
    incident_datetime TEXT NOT NULL,
    incident_date TEXT NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
    hour INTEGER NOT NULL,
    minute INTEGER NOT NULL,
    day_of_week TEXT,
    is_weekend INTEGER,
    quarter INTEGER,
    time_of_day TEXT,
    neighbourhood TEXT,
    x_coordinate REAL,
    y_coordinate REAL,
    has_coordinates INTEGER,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- Neighbourhood dimension table
CREATE TABLE IF NOT EXISTS dim_neighbourhood
(
    neighbourhood_id INTEGER PRIMARY KEY,
    neighbourhood_name TEXT UNIQUE NOT NULL,
    region TEXT
);


CREATE TABLE IF NOT EXISTS dim_crime_type
(
    crime_type_id INTEGER PRIMARY KEY,
    crime_type TEXT UNIQUE NOT NULL,
    crime_category TEXT
);


CREATE TABLE IF NOT EXISTS dim_date (
    date_id INTEGER PRIMARY KEY,
    date TEXT UNIQUE NOT NULL,
    year INTEGER,
    month INTEGER,
    month_name TEXT,
    quarter INTEGER,
    day_of_month INTEGER,
    day_of_week TEXT,
    day_of_year INTEGER,
    is_weekend INTEGER
);
