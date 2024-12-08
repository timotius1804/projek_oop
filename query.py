from abc import ABC, abstractmethod
import random
from display import showDetailed, showList

class QueryManga:
    def __init__(self, strategy, mangas):
        self.mangas = mangas
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy

    def get_manga(self):
        return self.strategy.get_manga(self.mangas)

class Strategy(ABC):
    @abstractmethod
    def get_manga(self, mangas):
        pass

class RandomManga(Strategy):
    def get_manga(self, mangas):
        if len(mangas) == 0:
            print("No Manga Found")
        random_manga = random.choice(mangas)
        showDetailed(random_manga)
        

class TopRatedManga(Strategy):
    def get_manga(self, mangas):
        if len(mangas) == 0:
            print("No Manga Found")
        top_rated_manga = sorted(mangas, key=lambda x: x.get_rating(), reverse=True)
        i = 0
        max_page = len(mangas) // 10
        if len(mangas) <= 10:
            max_page = 1
        if len(mangas) % 10 != 0 and len(mangas) > 10:
            max_page += 1
        while 0 <= i < len(mangas):
            print(f"Page {((i+1)//10)+1} of {max_page}")
            for j in range(min(10, len(mangas) - i)):
                showList(i+j, top_rated_manga)
            print(f"Page {((i+1)//10)+1} of {max_page}")
            print("n : Next Page")
            print("p : Previous Page")
            print("q : Quit")
            choice = input("Input Choice : ")
            if choice == 'n':
                i += 10
            elif choice == 'p':
                i -= 10
            elif choice == 'q':
                break
            elif choice in [str(x) for x in range(i+1, i+11)]:
                print("1. Show Details")
                print("2. Delete Manga")
                print("3. Edit Manga")
                print("4. Exit")
                details = input("Input choice : ")
                if details == '1':
                    showDetailed(top_rated_manga[int(choice)-1])
                    input("Press Enter to Continue")
                elif details == '2':
                    mangas.remove(top_rated_manga[int(choice)-1])
                    print(f"{top_rated_manga[int(choice)-1].get_title()} has been deleted")
                    top_rated_manga.remove(top_rated_manga[int(choice)-1])
                    input("Press Enter to Continue")
                elif details == '3':
                    print("Edit")
                elif details == '4':
                    break
            else:
                print("Invalid Choice")

def query_manga(mangas, mangas_dict):
    strategy = QueryManga(None, mangas)
    while True:
        print("1. Random Manga (Query)")
        print("2. Top Rated Manga (List)")
        print("3. Exit")
        choice = input("Input Choice : ")
        if choice == '1':
            strategy.set_strategy(RandomManga())
            strategy.get_manga()
        elif choice == '2':
            strategy.set_strategy(TopRatedManga())
            strategy.get_manga()
        elif choice == '3':
            break
        else:
            print("Invalid Choice")
        