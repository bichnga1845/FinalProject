from libs.JsonFileFactory import JsonFileFactory
from models.Book import Book

books=[]
books.append(Book("B1", "Conan", "Detective", "2005", "NXB Kim Dong", 20000, 40, "David"))
books.append(Book("B2", "Solo", "Action", "2020", "Anime", 30000, 100, "Sofia"))
books.append(Book("B3", "Legend", "Action", "2018", "Riot", 50000, 50, "John"))
books.append(Book("B4", "Mystery", "Detective", "2012", "HarperCollins", 25000, 60, "Anna"))
books.append(Book("B5", "Adventure", "Adventure", "2015", "Penguin", 18000, 80, "David"))
books.append(Book("B6", "Titanic", "Drama", "1998", "Random House", 22000, 120, "George"))
books.append(Book("B7", "Fantasy World", "Fantasy", "2017", "Viet Nam", 35000, 200, "John"))
books.append(Book("B8", "Journey", "Action", "2019", "Oxford", 27000, 75, "Sofia"))
books.append(Book("B9", "Warrior", "Action", "2021", "Viet Nam", 33000, 150, "David"))
books.append(Book("B10", "Echo", "Fantasy", "2013", "Viet Nam", 23000, 180, "Kim"))
books.append(Book("B11", "Nightmare", "Horror", "2010", "Riot", 45000, 35, "John"))
books.append(Book("B12", "The Last Stand", "Action", "2022", "Anime", 50000, 100, "Sofia"))
books.append(Book("B13", "Revenge", "Thriller", "2016", "Penguin", 40000, 45, "George"))
books.append(Book("B14", "Darkness", "Horror", "2021", "NXB Kim Dong", 55000, 110, "David"))
books.append(Book("B15", "Hope", "Drama", "2014", "HarperCollins", 20000, 130, "Sofia"))
books.append(Book("B16", "Galaxy", "Science Fiction", "2022", "Random House", 38000, 95, "John"))
books.append(Book("B17", "Universe", "Science Fiction", "2020", "Viet Nam", 47000, 85, "Kim"))
books.append(Book("B18", "Legend of Heroes", "Action", "2018", "Viet Nam", 30000, 70, "David"))
books.append(Book("B19", "Rising Sun", "Adventure", "2015", "Oxford", 25000, 60, "George"))
books.append(Book("B20", "Dragon's Tale", "Fantasy", "2016", "Penguin", 50000, 140, "Sofia"))
books.append(Book("B21", "Forest", "Adventure", "2021", "Viet Nam", 40000, 110, "Kim"))
books.append(Book("B22", "Storm", "Action", "2019", "Riot", 33000, 95, "David"))
books.append(Book("B23", "Underdog", "Drama", "2017", "NXB Kim Dong", 28000, 50, "John"))
books.append(Book("B24", "Kingdom", "Fantasy", "2020", "Viet Nam", 22000, 85, "Sofia"))
books.append(Book("B25", "Epic", "Action", "2018", "Riot", 45000, 110, "George"))
books.append(Book("B26", "Viking", "Adventure", "2021", "Penguin", 50000, 200, "Kim"))
books.append(Book("B27", "Warrior of Fate", "Action", "2022", "Viet Nam", 27000, 120, "David"))
books.append(Book("B28", "Assassin's Creed", "Action", "2019", "Viet Nam", 35000, 90, "John"))
books.append(Book("B29", "Legend of the Sea", "Fantasy", "2014", "Oxford", 25000, 150, "Sofia"))
books.append(Book("B30", "Silent Night", "Horror", "2021", "Random House", 50000, 60, "George"))

#write data into Json:
filename="books.json"
path=f"../dataset/{filename}"
JsonFileFactory().write_data(books,path)
