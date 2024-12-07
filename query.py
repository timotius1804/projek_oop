from abc import ABC, abstractmethod
import random

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
        random_manga = random.choice(mangas)
        self.display_manga_details(random_manga)

    def display_manga_details(self, random_manga):
        print(
f"""
Title : {random_manga.get_title()}
Author : {random_manga.get_author()}
Artist : {random_manga.get_artist()}
Tags : {', '.join(random_manga.get_tags())}
Followers : {random_manga.get_followers()}
Rating : {random_manga.get_rating()}
Total Chapters : {random_manga.get_total_chapters()}
Release Year : {random_manga.get_release_year()}
Status : {random_manga.get_status()}
Description : 
\t{random_manga.get_description()}
Link : {random_manga.get_link()}
"""
        )

class TopRatedManga(Strategy):
    def get_manga(self, mangas):
        top_rated_manga = sorted(mangas, key=lambda x: x.get_rating(), reverse=False)
        i = 0
        max_page = len(mangas) // 10
        if len(mangas) % 10 != 0 and len(mangas) > 10:
            max_page += 1
        while 0 <= i < len(mangas):
            print(f"Page {((i+1)//10)+1} of {max_page}")
            for j in range(min(10, len(mangas) - i)):
                print(f"""
{i+j+1}. {top_rated_manga[i+j].get_title()} 
Followers : {top_rated_manga[i+j].get_followers()} | \
Rating : {top_rated_manga[i+j].get_rating()} | \
Chapters : {top_rated_manga[i+j].get_total_chapters()} | \
Release Year : {top_rated_manga[i+j].get_release_year()} | \
Status : {top_rated_manga[i+j].get_status()} | \
Author : {top_rated_manga[i+j].get_author()} | \
Artist : {top_rated_manga[i+j].get_artist()} | \
Tags : {', '.join(top_rated_manga[i+j].get_tags())}
""")
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
            elif choice in range(i, i+10):
                print()

def query_manga(mangas, mangas_dict):
    strategy = QueryManga(None, mangas)
    while True:
        print("1. Random Manga (Query)")
        print("2. Top Rated Manga (List)")
        print("3. Exit")
        choice = input("Input Choice : ")
        if choice == '1':
            strategy.set_strategy(RandomManga())
        elif choice == '2':
            strategy.set_strategy(TopRatedManga())
        elif choice == '3':
            break
        else:
            print("Invalid Choice")
        strategy.get_manga()