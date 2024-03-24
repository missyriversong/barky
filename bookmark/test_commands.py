# how would I test Barky?
# First, I wouldn't test barky, I would test the reusable modules barky relies on:
# commands.py and database.py

# we will use pytest: https://docs.pytest.org/en/stable/index.html
import pytest
# should we test quit? No, its behavior is self-evident and not logic dependent
def test_quit_command():
    pass

# okay, should I test the other commands?
# not really, they are tighly coupled with sqlite3 and its use in the database.py module

#? set up db and command, how can we use these? @pytest.fixture
#? don't understand the overlap is there with test_database.py, how do we test both commands and database modules at the same time? 
import os
from database import DatabaseManager
from commands import CreateBookmarksTableCommand, AddBookmarkCommand, ListBookmarksCommand, DeleteBookmarkCommand, ImportGitHubStarsCommand, EditBookmarkCommand

@pytest.fixture
def database_manager() -> DatabaseManager:   
    filename = "test_bookmarks.db"
    dbm = DatabaseManager(filename)
    yield dbm
    dbm.__del__()          
    os.remove(filename)

@pytest.fixture
def create_bookmark() -> CreateBookmarksTableCommand:    
    pass


def test_create_bookmarks_table():
    #arrange - set up data 
    #act - create_bookmark uses databasemanager?
    #not sure how to connect command to databasemanager
    create_bookmark()   #invalid syntax error, can't call execute(), can't call fixture directly...?
    testbookmark.create_table(
        "testbookmark.db",
        {
            "id": "integer primary key autoincrement",
            "title": "text not null",
            "url": "text not null",
            "notes": "text",
            # "date_added": "text not null", leaving this out still couldn't figure out deprecated
        },
        )

    #assert - table made?
    assert "testbookmark.db" is True




@pytest.fixture
def add_bookmark() -> AddBookmarkCommand:    
    pass


def test_add_bookmark():
    add_bookmark()   #invalid syntax error using execute():, without : error no attribute execute... 
    testbookmark.add(
        data = {
            "title": "test_title",
            "url": "http://example.com",
            "notes": "test notes",
        }
    )

    #assert - data added...?  test_database...? redundant...? 
    conn = database_manager.connection
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM bookmarks WHERE title='test_title' ''')    
    
    assert cursor.fetchone()[0] == 1    



