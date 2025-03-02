-- Drop existing tables if they exist
DROP TABLE IF EXISTS cars;
DROP TABLE IF EXISTS manufacturers;
DROP TABLE IF EXISTS owners;

-- Create manufacturers table
CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    country TEXT NOT NULL
);

-- Create owners table
CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age INT CHECK (age > 18),
    city TEXT NOT NULL
);

-- Create cars table
CREATE TABLE cars (
    id SERIAL PRIMARY KEY,
    model TEXT NOT NULL,
    year INT CHECK (year >= 1886), -- First car invented in 1886
    manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE,
    owner_id INT REFERENCES owners(id) ON DELETE SET NULL,
    price NUMERIC CHECK (price > 0),
    is_electric BOOLEAN DEFAULT FALSE,
    mileage INT CHECK (mileage >= 0) DEFAULT 0
);

-- Insert manufacturers
INSERT INTO manufacturers (name, country) VALUES
    ('Toyota', 'Japan'),
    ('Ford', 'USA'),
    ('Tesla', 'USA'),
    ('BMW', 'Germany'),
    ('Hyundai', 'South Korea');

-- Insert owners
INSERT INTO owners (name, age, city) VALUES
    ('Alice', 30, 'New York'),
    ('Bob', 45, 'Los Angeles'),
    ('Charlie', 25, 'San Francisco'),
    ('David', 35, 'Chicago'),
    ('Eve', 40, 'Tokyo');

-- Insert cars
INSERT INTO cars (model, year, manufacturer_id, owner_id, price, is_electric, mileage) VALUES
    ('Camry', 2020, 1, 1, 25000, FALSE, 30000),
    ('Mustang', 2018, 2, 2, 35000, FALSE, 45000),
    ('Model S', 2022, 3, 3, 79999, TRUE, 12000),
    ('X5', 2019, 4, 4, 55000, FALSE, 40000),
    ('Elantra', 2021, 5, 5, 22000, FALSE, 20000);
