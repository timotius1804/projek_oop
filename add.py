# To-Do:
# 1. Integrate write_data function to here and make it into a class
# 2. Add choice function for user input to set parameters for the manga (e.g: tags, title)
# 3. Add function to edit manga record manually
# 4. Add function to delete manga record manually
# 5. Add function to add manga record manually
# 6. 

from api import MangaAPI
import uuid
from manga import Manga

class AddManga:
    def add_manual(self, mangas, mangas_dict):
        manga_id = uuid.uuid4()
        if manga_id in mangas_dict:
            for i in range(10):
                manga_id = uuid.uuid4()
                if manga_id not in mangas_dict:
                    break
            print("Failed to generate unique ID")
        title = input("Title : ")
        if title == '':
            print("Title cannot be empty")
            return
        try:
            followers = int(input("Followers : "))
            if followers < 0:
                print("Followers cannot be negative")
                return
        except ValueError:
            print("Followers must be an integer")
            return
        try:
            rating = float(input("Rating : "))
            if rating < 0 or rating > 10:
                print("Rating must be between 0 and 10")
                return
        except ValueError:
            print("Rating must be a float")
            return
        try:
            total_chapters = int(input("Total Chapters : "))
            if total_chapters < 0:
                print("Total Chapters cannot be negative")
                return
        except ValueError:
            print("Total Chapters must be an integer")
            return
        
        try:
            release_year = int(input("Release Year : "))
            if release_year < 1798 or release_year > 2024:
                print("Invalid Release Year (Must be between 1798 and 2024)")
                return
        except ValueError:
            print("Release Year must be an integer")
            return
        statuses = ["Ongoing", "Completed", "Hiatus", "Cancelled"]
        print("Statuses : ")
        for i, status in enumerate(statuses):
            print(f"{i+1}. {status}")
        status = input("Status : ")
        if status == '' or status not in statuses:
            print("Invalid Status")
            return
        author = input("Author : ")
        if author == '':
            print("Author cannot be empty")
            return
        artist = input("Artist : ")
        if artist == '':
            print("Artist cannot be empty")
            return
        tag_list = ["Action", "Fantasy", "Adventure", "Comedy", "Drama", "Romance", "School Life", "Shounen"]
        print("Tags : ")    
        for i, tag in enumerate(tag_list):
            print(f"{i+1}. {tag}")
        tags = input("Tags (comma separated) : ").split(",")
        if tags == []:
            print("Tags cannot be empty")
            return
        for i in tags:
            if i not in tag_list:
                print(f"Invalid Tag : {i}")
                return
        description = input("Description : ")
        if description == '':
            print("Description cannot be empty")
            return
        
        link = f"https://mangadex.org/title/{manga_id}"

        obj = Manga(manga_id, title, total_chapters, followers, rating, release_year, status, author, artist, description, link, tags)
        mangas.append(obj)
        mangas_dict[obj.get_manga_id()] = obj

    def tag_parameters(self, tag_choices):
        print("Tags : ")
        tags = ["Action", "Fantasy", "Adventure", "Comedy", "Drama", "Romance", "School Life", "Shounen"]
        while True:
            for i, tag in enumerate(tags):
                print(f"{i+1}. {tag}")
            print(f"Current Tags : {', '.join(tag_choices)}")
            try:
                input_tag = int(input("Select tags to toggle (press 0 to exit) :"))
                if input_tag == 0:
                    break
                if input_tag not in range(1, 9):
                    print("Invalid Choice")
                    continue
            except ValueError:
                print("Invalid Choice")
                continue
            if tags[input_tag-1] in tag_choices:
                tag_choices.remove(tags[input_tag-1])
            else:
                tag_choices.append(tags[input_tag-1])
        
    def add_api_custom(self, mangas, mangas_dict):
        included_tags = ["Action", "Fantasy", "Adventure", "Comedy", "Drama", "Romance", "School Life", "Shounen"]
        tags_mode = "OR"

        while True:
            print('Current Settings : ')
            print(f"Included Tags : {', '.join(included_tags)}")
            print(f"Tags Mode : {tags_mode}")
            print("1. Change Included Tags")
            print("2. Change Tags Mode")
            print("3. Confirm")
            try:
                choice = int(input("Input Choice : "))
            except ValueError:
                print("Invalid Choice")
                continue
            if choice == 1:
                self.tag_parameters(included_tags)
            elif choice == 2:
                print("Tags Mode : ")
                print("1. OR")
                print("2. AND")
                tag_choice = input("Input Choice : ")
                if tag_choice not in ["1", "2"]:
                    print("Invalid Choice")
                    continue
                if tag_choice == "1":
                    tags_mode = "OR"
                else:
                    tags_mode = "AND"
            elif choice == 3:
                break

        api = MangaAPI(included_tags, tags_mode).getData()
        for i in api:
            if i[0] in mangas_dict:
                obj = Manga(*i[:11], i[11:])
                mangas_dict[i[0]] = obj
            else:
                obj = Manga(*i[:11], i[11:])
                mangas.append(obj)
                mangas_dict[obj.get_manga_id()] = obj

    def add_latest(self, mangas, mangas_dict):
        api = MangaAPI(["Action", "Fantasy", "Adventure", "Comedy", "Drama", "Romance", "School Life", "Shounen"], "OR").getData()
        for i in api:
            if i[0] in mangas_dict:
                obj = Manga(*i[:11], i[11:])
                mangas_dict[i[0]] = obj
            else:
                obj = Manga(*i[:11], i[11:])
                mangas.append(obj)
                mangas_dict[obj.get_manga_id()] = obj

def add_manga(mangas, mangas_dict):
    while True:
        add = AddManga()
        print("1. Add Manually")
        print("2. Add from API (Custom)")
        print("3. Add 50 Latest Mangas")
        print("4. Exit")
        choice = input("Input Choice : ")
        if choice == '1':
            add.add_manual(mangas, mangas_dict)
        elif choice == '2':
            add.add_api_custom(mangas, mangas_dict)
        elif choice == '3':
            add.add_latest(mangas, mangas_dict)
        elif choice == '4':
            break
        else:
            print("Invalid Choice")
            
