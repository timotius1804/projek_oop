class Manga:
    def __init__(self, manga_id: int, title: str, total_chapters: int, followers: int, rating: float, release_year: int, status: str, author: str, artist: str, description: str, link: str, tags: list) -> None:
        self.__manga_id = manga_id
        self.__title = title
        self.__total_chapters = total_chapters
        self.__followers = followers
        self.__rating = rating
        self.__release_year = release_year
        self.__status = status
        self.__author = author
        self.__artist = artist
        self.__description = description
        self.__link = link
        self.__tags = tags

    def get_followers(self) -> int:
        return self.__followers

    def get_manga_id(self) -> int:
        return self.__manga_id
    
    def get_title(self) -> str:
        return self.__title
    
    def get_rating(self) -> float:
        return self.__rating
    
    def get_total_chapters(self) -> int:
        return self.__total_chapters
    
    def get_release_year(self) -> int:
        return self.__release_year
    
    def get_description(self) -> str:
        return self.__description
    
    def get_status(self) -> str:
        return self.__status
    
    def get_author(self) -> str:
        return self.__author
    
    def get_artist(self) -> str:
        return self.__artist
    
    def get_tags(self) -> list:
        return self.__tags
    

    def get_link(self) -> str:
        return self.__link