
def showDetailed(mangas):
        print(
f"""
Title : {mangas.get_title()}
Author : {mangas.get_author()}
Artist : {mangas.get_artist()}
Tags : {', '.join(mangas.get_tags())}
Followers : {mangas.get_followers()}
Rating : {mangas.get_rating()}
Total Chapters : {mangas.get_total_chapters()}
Release Year : {mangas.get_release_year()}
Status : {mangas.get_status()}
Description : 
\t{mangas.get_description()}
Link : {mangas.get_link()}
"""
        )

def showList(count, manga_data):
        print(f"""
{count+1}. {manga_data[count].get_title()} 
Followers : {manga_data[count].get_followers()} | \
Rating : {manga_data[count].get_rating()} | \
Chapters : {manga_data[count].get_total_chapters()} | \
Release Year : {manga_data[count].get_release_year()} | \
Status : {manga_data[count].get_status()} | \
Author : {manga_data[count].get_author()} | \
Artist : {manga_data[count].get_artist()} | \
Tags : {', '.join(manga_data[count].get_tags())}
""")