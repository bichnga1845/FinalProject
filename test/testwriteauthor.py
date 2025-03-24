from libs.JsonFileFactory import JsonFileFactory
from models.Author import Author

authors=[]
authors.append(Author("A1", "John", "Male", "USA", "3", "Coca"))
authors.append(Author("A2", "Sang", "Male", "Vietnam", "5", "Anime"))
authors.append(Author("A3", "Anna", "Female", "USA", "7", "Books"))
authors.append(Author("A4", "George", "Male", "UK", "8", "Movies"))
authors.append(Author("A5", "Kim", "Female", "Korea", "2", "Traveling"))
authors.append(Author("A6", "Sofia", "Female", "Russia", "4", "Sports"))
authors.append(Author("A7", "David", "Male", "Canada", "6", "Cycling"))
authors.append(Author("A8", "Nina", "Female", "Germany", "10", "Music"))
authors.append(Author("A9", "Elena", "Female", "Italy", "3", "Art"))
authors.append(Author("A10", "Liam", "Male", "Australia", "5", "Gaming"))
authors.append(Author("A11", "Sophie", "Female", "Spain", "9", "Photography"))
authors.append(Author("A12", "Ethan", "Male", "USA", "4", "Books"))
authors.append(Author("A13", "Charlotte", "Female", "UK", "3", "Yoga"))
authors.append(Author("A14", "Mason", "Male", "Canada", "7", "Music"))
authors.append(Author("A15", "Amelia", "Female", "India", "5", "Pets"))
authors.append(Author("A16", "Luca", "Male", "Italy", "6", "Fashion"))
authors.append(Author("A17", "Ava", "Female", "France", "8", "Art"))
authors.append(Author("A18", "Leo", "Male", "Germany", "9", "Football"))
authors.append(Author("A19", "Sofia", "Female", "France", "4", "Traveling"))
authors.append(Author("A20", "Jack", "Male", "USA", "5", "Sports"))
authors.append(Author("A21", "Isabella", "Female", "USA", "3", "Movies"))
authors.append(Author("A22", "James", "Male", "UK", "6", "Cycling"))
authors.append(Author("A23", "Amos", "Male", "Israel", "2", "Technology"))
authors.append(Author("A24", "Maya", "Female", "India", "4", "Photography"))
authors.append(Author("A25", "Zoe", "Female", "Australia", "5", "Traveling"))
authors.append(Author("A26", "Daniel", "Male", "USA", "7", "Books"))
authors.append(Author("A27", "Grace", "Female", "Canada", "5", "Yoga"))
authors.append(Author("A28", "Jacob", "Male", "UK", "6", "Art"))
authors.append(Author("A29", "Olivia", "Female", "Italy", "8", "Movies"))
authors.append(Author("A30", "William", "Male", "Australia", "10", "Gaming"))

#write data into Json:
filename="authors.json"
path=f"../dataset/{filename}"
JsonFileFactory().write_data(authors,path)