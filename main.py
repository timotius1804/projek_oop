# Nama : Timotius
# NIM  : 232203088

from api import MangaAPI
from manga import Manga
from string import punctuation, whitespace
import time
from query import query_manga
from add import add_manga
from update import edit_manga

def write_data(obj_list):
    with open("manga.txt", "w", encoding="UTF-8") as f:
        for data in obj_list:
            i = data.get_data()
            strippables = punctuation + whitespace
            cleaned_desc =" ".join([x.strip(strippables) for x in i[9].split()])
            f.write(f"{i[0]}|{i[1]}|{i[2]}|{i[3]}|{i[4]}|{i[5]}|{i[6]}|{i[7]}|{i[8]}|{cleaned_desc}|{i[10]}|{'|'.join(i[11])}\n")

def read_data():
    result = []
    result_dict = {}
    with open("manga.txt", "r", encoding="UTF-8") as f:
        data = f.readlines()
        for manga in data:
            temp = [x.strip() for x in manga.split("|")]
            if len(temp) < 12:
                print(f"Data is incomplete (Title : {temp[1]}, ID : {temp[0]})")
                continue
            if temp[0] == "":
                print(f"Manga ID is empty (Title : {temp[1]})")
                continue
            if temp[1] == "":
                print(f"Title is empty (ID : {temp[0]})")
                continue
            try:
                if int(temp[2]) < 0:
                    print(f"Total Chapters must be a positive integer (Title : {temp[1]})")
                    continue
            except ValueError:
                print(f"Total Chapters must be an integer (Title : {temp[1]})")
                continue
            try:
                if int(temp[3]) < 0:
                    print(f"Followers must be a positive integer (Title : {temp[1]})")
                    continue
            except ValueError:
                print(f"Follower must be an integer (Title : {temp[1]})")
                continue
            try:
                if float(temp[4]) < 0 or float(temp[4]) > 10:
                    print(f"Rating must be between 0 and 10 (Title : {temp[1]})")
                    continue
            except ValueError:
                print(f"Rating must be a float (Title : {temp[1]})")
                continue
            try:
                if int(temp[5]) < 1798 or int(temp[5]) > 2024:
                    print(f"Release Year must be between 1798 and 2024 (Title : {temp[1]})")
                    continue
            except ValueError: 
                print(f"Release Year must be an integer (Title : {temp[1]})")
                continue
            if temp[6] not in ["Ongoing", "Completed", "Hiatus", "Cancelled"]:
                print(f"Invalid Status : {temp[6]} (Title : {temp[1]})")
                continue
            if temp[7] == "":
                print(f"Author is empty (Title : {temp[1]})")
                continue
            if temp[8] == "":
                print(f"Artist is empty (Title : {temp[1]})")
                continue
            if temp[9] == "":
                print(f"Description is empty (Title : {temp[1]})")
                continue
            if temp[10] == "":
                print(f"Link is empty (Title : {temp[1]})")
                continue
            if temp[11:] == []:
                print(f"Tags are empty (Title : {temp[1]})")
                continue
            invalid_tags = False
            for tag in temp[11:]:
                if tag not in ["Action", "Fantasy", "Adventure", "Comedy", "Drama", "Romance", "School Life", "Shounen"]:
                    print(f"Invalid Tag : {tag} (Title : {temp[1]})")
                    invalid_tags = True
                    break
            if invalid_tags:
                continue

            obj = Manga(temp[0], temp[1], int(temp[2]), int(temp[3]), float(temp[4]), int(temp[5]), *temp[6:11], temp[11:])
            result.append(obj)
            result_dict[obj.get_manga_id()] = obj
    return result, result_dict

def delete_manga(mangas, mangas_dict):
    choice = input("Input Manga ID : ")
    if choice not in mangas_dict:
        print("Manga ID not found")
        return
    for i in mangas:
        if i.get_manga_id() == choice:
            print(f"{i.get_title()} has been deleted")
            mangas.remove(i)
            del mangas_dict[choice]
            return

def main():
    start = time.time()
    mangas, mangas_dict = read_data()
    while True:
        print("1. Add Manga")
        print("2. Query Manga")
        print("3. Edit Manga")
        print("4. Delete Manga")
        print("5. Exit")
        choice = input("Input Choice : ")
        commands = ("add_manga", "query_manga", "edit_manga", "delete_manga", "exit")
        if choice in "12345":
            try:
                choice = int(choice)
                if choice == 5:
                    break
            except:
                print("Invalid Choice")
            eval(commands[int(choice) - 1])(mangas, mangas_dict)
        else:
            print("Invalid Choice")
    write_data(mangas)

if __name__ == "__main__":
    main()