CREATE TABLE IF NOT EXISTS exercises (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unieke ID voor elke oefening
    name TEXT NOT NULL,                    -- Naam van de oefening
    sets INTEGER NOT NULL,                 -- Aantal sets
    reps INTEGER NOT NULL,                 -- Aantal reps per set
    date TEXT DEFAULT CURRENT_DATE         -- Datum waarop de oefening werd toegevoegd
);