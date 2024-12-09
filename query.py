# Nama : Timotius
# NIM  : 232203088
from abc import ABC, abstractmethod
import random
from display import showDetailed
from page import showPage

class QueryManga:
    def __init__(self, strategy, mangas, mangas_dict):
        self.mangas = mangas
        self.strategy = strategy
        self.mangas_dict = mangas_dict
    
    def set_strategy(self, strategy):
        self.strategy = strategy

    def get_manga(self):
        return self.strategy.get_manga(self.mangas, self.mangas_dict)

class Strategy(ABC):
    @abstractmethod
    def get_manga(self, mangas, mangas_dict):
        pass

class RandomManga(Strategy):
    def get_manga(self, mangas, mangas_dict):
        if len(mangas) == 0:
            print("No Manga Found")
        random_manga = random.choice(mangas)
        showDetailed(random_manga)

class TopFollowedManga(Strategy):
    def get_manga(self, mangas, mangas_dict):
        showPage(mangas, mangas_dict, '2')
        
class TopRatedManga(Strategy):
    def get_manga(self, mangas, mangas_dict):
        showPage(mangas, mangas_dict, '1')

class MangaByGenre(Strategy):
    def tag_parameters(self, tag_choices):
        print("Tags : ")
        tags = ["Action", "Fantasy", "Adventure", 
                "Comedy", "Drama", "Romance", 
                "School Life", "Shounen"]
        while True:
            for i, tag in enumerate(tags):
                print(f"{i+1}. {tag}")
            print(f"Current Tags : {', '.join(tag_choices)}")
            try:
                input_tag = int(input("Select tags to toggle (press 0 to confirm) :"))
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
        
    def get_manga(self, mangas, mangas_dict):
        included_tags = ["Action", "Fantasy", "Adventure", 
                         "Comedy", "Drama", "Romance", 
                         "School Life", "Shounen"]
        self.tag_parameters(included_tags)
        showPage(mangas, mangas_dict, '4', included_tags)

class MangaByTitle(Strategy):
    def get_manga(self, mangas, mangas_dict):
        title = input("Input Title : ")
        for manga in mangas:
            if manga.get_title().lower() == title.lower():
                showDetailed(manga)
                return


def query_manga(mangas, mangas_dict):
    strategy = QueryManga(None, mangas, mangas_dict)
    while True:
        print("1. Random Manga (Query)")
        print("2. Top Rated Manga (List)")
        print("3. Top Followed Manga (List)")
        print("4. Manga by Genre (List)")
        print("5. Manga by Title (Query)")
        print("6. Exit")
        choice = input("Input Choice : ")
        if choice == '1':
            strategy.set_strategy(RandomManga())
            strategy.get_manga()
        elif choice == '2':
            strategy.set_strategy(TopRatedManga())
            strategy.get_manga()
        elif choice == '3':
            strategy.set_strategy(TopFollowedManga())
            strategy.get_manga()
        elif choice == '4':
            strategy.set_strategy(MangaByGenre())
            strategy.get_manga()
        elif choice == '5':
            strategy.set_strategy(MangaByTitle())
            strategy.get_manga()
        else:
            print("Invalid Choice")
        