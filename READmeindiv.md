# Movie Collection Manager

The Movie Collection Manager is a Python program that allows users to organize and manage a collection of movies using a SQL relational database. The program uses SQLite to store movie information, including titles, genres, release years, and ratings. Users can view their movie collection, add new movies, update existing movie ratings, and delete movies from the database. The purpose of this project is to demonstrate how Python can interact with a SQL database to perform basic database operations.

## Instructions for Build and Use

Steps to build and/or run the software:

1. Install Python 3 and Visual Studio Code on your computer.
2. Download or clone the project repository from GitHub and open the project folder in Visual Studio Code.
3. Open the terminal in VS Code and run the main Python program using `python main.py`. The program will create the SQLite database and movies table if they do not already exist.

Instructions for using the software:

1. Run the program to display the Movie Collection Manager menu.
2. Select an option to view all movies, add a new movie, update an existing movie's rating, or delete a movie.
3. Follow the prompts to enter movie information or select an existing movie. The program will save changes to the SQLite database. Select the exit option when finished.

## Development Environment

To recreate the development environment, you need the following software and/or libraries:

* Python 3
* Visual Studio Code with the Python extension
* SQLite database using Python's built-in `sqlite3` library

## Useful Websites to Learn More

I found these websites useful for learning about the technologies used in this project:

* [Python SQLite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
* [SQLite Official Documentation](https://www.sqlite.org/docs.html)
* [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Add the ability to search for movies by title or genre.
* [ ] Create a graphical user interface instead of using a terminal-based menu.
* [ ] Add the ability to sort movies by rating or release year.
* [ ] Improve input validation to prevent incorrect movie information from being entered.