from libs.JsonFileFactory import JsonFileFactory
from models.User import User

users=[]
users.append(User("john","123","John","Male","12/03/2000","09876567","Hồ ch minh","admin"))
users.append(User("sang","123",role="admin"))

#write data into Json:
filename="users.json"
path=f"../dataset/{filename}"
JsonFileFactory().write_data(users,path)


