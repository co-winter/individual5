"""Movie Collection Manager - CSE 310 SQL Relational Databases module."""

import sqlite3
from pathlib import Path

DATABASE = Path(__file__).with_name("movies.db")


def connect_database():
    connection = sqlite3.connect(DATABASE)
    connection.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT NOT NULL,
            release_year INTEGER NOT NULL,
            rating REAL NOT NULL CHECK (rating >= 0 AND rating <= 10)
        )
    """)
    connection.commit()
    return connection


def view_movies(connection):
    rows = connection.execute(
        "SELECT id, title, genre, release_year, rating FROM movies ORDER BY id"
    ).fetchall()
    if not rows:
        print("No movies saved yet.")
        return
    print("\nID | Title | Genre | Year | Rating")
    print("-" * 55)
    for movie_id, title, genre, year, rating in rows:
        print(f"{movie_id} | {title} | {genre} | {year} | {rating:.1f}/10")


def ask_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def ask_number(prompt, minimum, maximum, whole=False):
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw) if whole else float(raw)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if minimum <= value <= maximum:
            return value
        print(f"Enter a number between {minimum} and {maximum}.")


def add_movie(connection):
    title = ask_text("Movie title: ")
    genre = ask_text("Genre: ")
    year = ask_number("Release year: ", 1888, 2100, whole=True)
    rating = ask_number("Rating (0-10): ", 0, 10)
    connection.execute(
        "INSERT INTO movies (title, genre, release_year, rating) VALUES (?, ?, ?, ?)",
        (title, genre, year, rating),
    )
    connection.commit()
    print("Movie added successfully!")


def choose_movie(connection):
    view_movies(connection)
    if connection.execute("SELECT COUNT(*) FROM movies").fetchone()[0] == 0:
        return None
    movie_id = ask_number("Enter movie ID: ", 1, 2147483647, whole=True)
    movie = connection.execute("SELECT id FROM movies WHERE id = ?", (movie_id,)).fetchone()
    if movie is None:
        print("No movie exists with that ID.")
        return None
    return movie_id


def update_movie(connection):
    movie_id = choose_movie(connection)
    if movie_id is None:
        return
    print("1. Title  2. Genre  3. Release year  4. Rating")
    field = input("Choose a field to update: ").strip()
    if field == "1":
        column, value = "title", ask_text("New title: ")
    elif field == "2":
        column, value = "genre", ask_text("New genre: ")
    elif field == "3":
        column, value = "release_year", ask_number("New release year: ", 1888, 2100, whole=True)
    elif field == "4":
        column, value = "rating", ask_number("New rating (0-10): ", 0, 10)
    else:
        print("Invalid field selection.")
        return
    # The column name comes from fixed choices above, not user-provided SQL.
    connection.execute(f"UPDATE movies SET {column} = ? WHERE id = ?", (value, movie_id))
    connection.commit()
    print("Movie updated successfully!")


def delete_movie(connection):
    movie_id = choose_movie(connection)
    if movie_id is None:
        return
    confirm = input("Delete this movie? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Deletion cancelled.")
        return
    connection.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
    connection.commit()
    print("Movie deleted successfully!")


def main():
    with connect_database() as connection:
        while True:
            print("\n===== MOVIE COLLECTION MANAGER =====")
            print("1. View all movies")
            print("2. Add a movie")
            print("3. Update a movie")
            print("4. Delete a movie")
            print("5. Exit")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                view_movies(connection)
            elif choice == "2":
                add_movie(connection)
            elif choice == "3":
                update_movie(connection)
            elif choice == "4":
                delete_movie(connection)
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()
