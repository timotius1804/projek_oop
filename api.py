
import requests

class MangaAPI:
    def __init__(self, *args):
        self.__tags_mode = args[0]
        self.__included_tags = args[1]
    def getData(self):
        included_tag_names = self.__included_tags
        base_url = "https://api.mangadex.org"
        tags = requests.get(
            f"{base_url}/manga/tag"
        ).json()
        included_tag_ids = [
            tag["id"]
            for tag in tags["data"]
            if tag["attributes"]["name"]["en"]
            in included_tag_names
        ]
        r = requests.get(
            f"{base_url}/manga",
            params={
                "includedTags[]": included_tag_ids,
                "includedTagsMode": self.__tags_mode,
                "limit": 50,
                "originalLanguage[]": ["jp"],
                "availableTranslatedLanguage[]": ["en"],
                "contentRating[]": ["safe"],
            },
        )

        manga_ids = [manga["id"] for manga in r.json()["data"]] 

        manga_datas = []
        for i in manga_ids:
            chapters_data = requests.get(
                f"{base_url}/manga/{i}/feed",
                params={
                    "translatedLanguage[]": ["en"],
                }
            ).json()

            manga_data = requests.get(
                f"{base_url}/manga/{i}",
                params={
                    "translatedLanguage[]": ["en"],
                }
            ).json()
            manga_attributes = manga_data["data"]["attributes"]

            rating_data = requests.get(
                f"{base_url}/statistics/manga/{i}"
            ).json()
            chapter_count = chapters_data["total"]
            try:
                manga_title = manga_attributes["title"]["en"]
            except KeyError:
                if "jp" in manga_attributes["title"]:
                    manga_title = manga_attributes["title"]["jp"]
                elif "ja-ro" in manga_attributes["title"]:
                    manga_title = manga_attributes["title"]["ja-ro"]
            try:
                manga_desc = manga_attributes["description"]["en"]
            except KeyError:
                manga_desc = "No description available"
            manga_link = f"https://mangadex.org/title/{i}"
            release_year = manga_attributes["year"]
            manga_state = manga_attributes["status"].upper()
            manga_author_id = [x["id"] for x in manga_data["data"]["relationships"] if x["type"] == "author"][0]
            manga_artist_id = [x["id"] for x in manga_data["data"]["relationships"] if x["type"] == "artist"][0]
            manga_follows = rating_data["statistics"][i]["follows"]
            manga_author = requests.get(
                f"{base_url}/author/{manga_author_id}"
            ).json()["data"]["attributes"]["name"]
            manga_artist = requests.get(
                f"{base_url}/author/{manga_artist_id}"
            ).json()["data"]["attributes"]["name"]
            manga_rating = rating_data["statistics"][i]["rating"]["average"]
            manga_tags = [tag["attributes"]["name"]["en"] for tag in manga_attributes["tags"] if tag["attributes"]["name"]["en"] in included_tag_names]
            manga_datas.append([i, manga_title, chapter_count, manga_follows, manga_rating, release_year, manga_state, manga_author, manga_artist, manga_desc, manga_link, manga_tags])
        return manga_datas

