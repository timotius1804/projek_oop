from api import MangaAPI
from manga import Manga
from string import punctuation, whitespace
import time
from query import query_manga
from add import add_manga




def write_data(obj_list):
    with open("manga.txt", "w", encoding="UTF-8") as f:
        for i in obj_list:
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
            obj = Manga(*temp[:11], temp[11:])
            result.append(obj)
            result_dict[obj.get_manga_id()] = obj
    return result, result_dict

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
            if int(choice) == 5:
                break
            eval(commands[int(choice) - 1])(mangas, mangas_dict)
        else:
            print("Invalid Choice")
    write_data(mangas)

if __name__ == "__main__":
    main()