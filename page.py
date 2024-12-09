from display import showDetailed, showList
from update import edit_manga

def showPage(mangas, mangas_dict, mode, tags=[]):
        if len(mangas) == 0:
                print("No Manga Found")
        if mode == '1':
                top_manga = sorted(mangas, key=lambda x: x.get_rating(), reverse=True)
        elif mode == '2':
                top_manga = sorted(mangas, key=lambda x: x.get_followers(), reverse=True)
        elif mode == '3':
                top_manga = sorted(mangas, key=lambda x: x.get_total_chapters(), reverse=True)
        elif mode == '4':
                top_manga = []
                for i in mangas:
                        for j in i.get_tags():
                                if j in tags:
                                        top_manga.append(i)
                                        break
        i = 0
        max_page = len(mangas) // 10
        if len(mangas) <= 10:
                max_page = 1
        if len(mangas) % 10 != 0 and len(mangas) > 10:
                max_page += 1
        while 0 <= i < len(mangas):
                print(f"Page {((i+1)//10)+1} of {max_page}")
                for j in range(min(10, len(mangas) - i)):
                        showList(i+j, top_manga)
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
                                showDetailed(top_manga[int(choice)-1])
                                input("Press Enter to Continue")
                        elif details == '2':
                                mangas.remove(top_manga[int(choice)-1])
                                print(f"{top_manga[int(choice)-1].get_title()} has been deleted")
                                top_manga.remove(top_manga[int(choice)-1])
                                input("Press Enter to Continue")
                        elif details == '3':
                                edit_manga(mangas, mangas_dict, top_manga[int(choice)-1].get_manga_id())
                        elif details == '4':
                                continue
                        else:
                                print("Invalid Choice")