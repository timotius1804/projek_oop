from display import showDetailed
def edit_manga(mangas, mangas_dict, id=""):
    if id == "":
        choice = input("Input Manga ID : ")
    else:
        choice = id
    if choice not in mangas_dict:
        print("Manga ID not found")
        return
    for i in mangas:
        if i.get_manga_id() == choice:
            manga_data = i
    while True:
        showDetailed(manga_data)
        print("1. Edit Title")
        print("2. Edit Author")
        print("3. Edit Artist")
        print("4. Edit Followers")
        print("5. Edit Rating")
        print("6. Edit Total Chapters")
        print("7. Edit Release Year")
        print("8. Edit Status")
        print("9. Edit Description")
        print("10. Edit Tags")
        print("0. Exit")
        edit_choice = input("Input Choice : ")
        if edit_choice == '1':
            title = input("Title : ")
            if title == '':
                print("Title cannot be empty")
                continue
            manga_data.set_title(title)
        elif edit_choice == '2':
            author = input("Author : ")
            if author == '':
                print("Author cannot be empty")
                continue
            manga_data.set_author(author)
        elif edit_choice == '3':
            artist = input("Artist : ")
            if artist == '':
                print("Artist cannot be empty")
                continue
            manga_data.set_artist(artist)
        elif edit_choice == '4':
            try:
                followers = int(input("Followers : "))
                if followers < 0:
                    print("Followers cannot be negative")
                    continue
                manga_data.set_followers(followers)
            except ValueError:
                print("Followers must be an integer")
                continue
        elif edit_choice == '5':
            try:
                rating = float(input("Rating : "))
                if rating < 0 or rating > 10:
                    print("Rating must be between 0 and 10")
                    continue
                manga_data.set_rating(rating)
            except ValueError:
                print("Rating must be a float")
                continue
        elif edit_choice == '6':
            try:
                total_chapters = int(input("Total Chapters : "))
                if total_chapters < 0:
                    print("Total Chapters cannot be negative")
                    continue
                manga_data.set_total_chapters(total_chapters)
            except ValueError:
                print("Total Chapters must be an integer")
                continue
        elif edit_choice == '7':
            try:
                release_year = int(input("Release Year : "))
                if release_year < 1798 or release_year > 2024:
                    print("Invalid Release Year (Must be between 1798 and 2024)")
                    continue
                manga_data.set_release_year(release_year)
            except ValueError:
                print("Release Year must be an integer")
                continue
        elif edit_choice == '8':
            statuses = ["Ongoing", "Completed", "Hiatus", "Cancelled"]
            print("Statuses : ")
            for i, status in enumerate(statuses):
                print(f"{i+1}. {status}")
            status = input("Status (e.g: Ongoing, Completed) : ").title()
            if status == '' or status not in statuses:
                print("Invalid Status")
                continue
            manga_data.set_status(status)
        elif edit_choice == '9':
            description = input("Description : ")
            if description == '':
                print("Description cannot be empty")
                continue
            manga_data.set_description(description)
        elif edit_choice == '10':
            tag_list = ["Action", "Fantasy", "Adventure", "Comedy", "Drama", "Romance", "School Life", "Shounen"]
            print("Tags : ")    
            for i, tag in enumerate(tag_list):
                print(f"{i+1}. {tag}")
            tags = input("Tags (e.g: fantasy, adventure, action) : ").split(",")
            tags = [i.strip().title() for i in tags]
            if tags == []:
                print("Tags cannot be empty")
                return
            for i in tags:
                if i not in tag_list:
                    print(f"Invalid Tag : {i}")
                    return
            manga_data.set_tags(tags)
        elif edit_choice == '0':
            break
