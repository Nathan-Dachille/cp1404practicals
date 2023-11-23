"""Queries user for a Wikipedia page title or search phrase and prints summary."""
import wikipedia

MENU = """(S)earch Wikipedia
(G)et Page Summary"""


def main():
    """Ask user to search Wikipedia or Get a page summary."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "":
        if choice == "S":
            query = input("Enter your search query: ")
            search_wikipedia(query)
        elif choice == "G":
            page_title = input("Return summary for page: ")
            get_page_summary(page_title)
        else:
            print("Invalid Choice. ")
        print(MENU)
        choice = input(">>> ").upper()


def search_wikipedia(query):
    """Search Wikipedia for a specific query and prints results."""
    titles = wikipedia.search(query)
    print(f"The query '{query}' returned {len(titles)} results: ")
    for title in titles:
        print(title)


def get_page_summary(page_title):
    """Returns title, summary and url of Wikipedia Page."""
    try:
        summary = wikipedia.summary(page_title, auto_suggest=False)
        print(page_title)
        print(summary)
        print(f"Get more information at: {wikipedia.page(page_title, auto_suggest=False).url}")

    except (wikipedia.DisambiguationError, wikipedia.PageError) as error:
        print(error)


if __name__ == '__main__':
    main()
