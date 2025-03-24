from libs.JsonFileFactory import JsonFileFactory
from models.Reader import Reader

readers = []
readers.append(Reader(1, "My", "Female", "24/03/2025", "09876543456", "HCM", [["B1", 1]]))
readers.append(Reader(2, "Friend", "Male", "15/08/1995", "0934212345", "HCM", [["B2", 2]]))
readers.append(Reader(3, "Alice", "Female", "01/07/2000", "0988123456", "HCM", [["B3", 1], ["B4", 2]]))
readers.append(Reader(4, "Bob", "Male", "22/10/1993", "0976543210", "Ha Noi", [["B5", 3]]))
readers.append(Reader(5, "Cathy", "Female", "10/05/2001", "0923456789", "Da Nang", [["B6", 1], ["B7", 4]]))
readers.append(Reader(6, "Dan", "Male", "04/02/1990", "0934123456", "HCM", [["B8", 2]]))
readers.append(Reader(7, "Emma", "Female", "19/06/2002", "0978123456", "HCM", [["B9", 1]]))
readers.append(Reader(8, "Frank", "Male", "13/09/1985", "0912123456", "Ha Noi", [["B10", 2]]))
readers.append(Reader(9, "Grace", "Female", "25/12/1997", "0945123456", "HCM", [["B11", 1]]))
readers.append(Reader(10, "Harry", "Male", "17/11/1992", "0912345678", "HCM", [["B12", 3]]))
readers.append(Reader(11, "Ivy", "Female", "22/07/1996", "0932567890", "Da Nang", [["B13", 2]]))
readers.append(Reader(12, "Jack", "Male", "02/02/1994", "0971234567", "HCM", [["B14", 1]]))
readers.append(Reader(13, "Kathy", "Female", "09/03/1998", "0907890123", "HCM", [["B15", 2]]))
readers.append(Reader(14, "Leo", "Male", "18/04/1990", "0918765432", "HCM", [["B16", 1]]))
readers.append(Reader(15, "Mia", "Female", "05/10/2000", "0946758392", "HCM", [["B17", 3]]))
readers.append(Reader(16, "Nick", "Male", "27/08/1994", "0934126789", "HCM", [["B18", 2]]))
readers.append(Reader(17, "Olivia", "Female", "15/05/1995", "0912456789", "Ha Noi", [["B19", 1]]))
readers.append(Reader(18, "Paul", "Male", "06/01/1991", "0938765432", "HCM", [["B20", 2]]))
readers.append(Reader(19, "Quincy", "Male", "28/09/1987", "0945678901", "HCM", [["B21", 1]]))
readers.append(Reader(20, "Rita", "Female", "12/12/1999", "0916543210", "Da Nang", [["B22", 3]]))
readers.append(Reader(21, "Sam", "Male", "14/03/1993", "0978901234", "HCM", [["B23", 2]]))
readers.append(Reader(22, "Tina", "Female", "23/07/2001", "0929876543", "HCM", [["B24", 1]]))
readers.append(Reader(23, "Ursula", "Female", "17/09/1998", "0983412345", "HCM", [["B25", 2]]))
readers.append(Reader(24, "Victor", "Male", "19/06/1990", "0913212345", "HCM", [["B26", 1]]))
readers.append(Reader(25, "Wendy", "Female", "20/03/1995", "0987654321", "HCM", [["B27", 3]]))
readers.append(Reader(26, "Xander", "Male", "11/11/1992", "0934109876", "HCM", [["B28", 1]]))
readers.append(Reader(27, "Yara", "Female", "04/06/2003", "0923456789", "Ha Noi", [["B29", 2]]))
readers.append(Reader(28, "Zane", "Male", "30/12/1989", "0943212345", "HCM", [["B30", 1]]))
readers.append(Reader(29, "Anna", "Female", "15/08/1997", "0912345678", "Da Nang", [["B1", 2]]))
readers.append(Reader(30, "John", "Male", "12/01/1988", "0923456789", "HCM", [["B2", 1]]))

#write data into Json:
filename="readers.json"
path=f"../dataset/{filename}"
JsonFileFactory().write_data(readers,path)