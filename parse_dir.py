import os

# Returns a list of the files in a path
def listfiles(path):
    return [
        f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))
    ]


# Returns a list of the directories in a path
def listdirs(path):
    return [
        d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))
    ]


# Returns a list of tuples (file_name, file_path). File name doesn't have an extension
def getbooks(root):
    if not os.path.isdir('./audiobooks'):
        print('There is no audiobooks directory. Create ./audiobooks')

    books = []
    for book_dir in listdirs(root):
        book_dir_path = os.path.join(root, book_dir)

        # List the files in the directory
        files_in_dir = listfiles(book_dir_path)
        # Sorts the files alphabetically
        files_in_dir.sort()
        # List of tuples (file_name, file_path), also making sure they are one of the accepted audio file formats
        acceptable_extensions = {
            '.mp3', '.wav', '.aiff', '.m4a', '.m4b', '.m4p'
        }
        files = [(os.path.splitext(f)[0], os.path.join(book_dir_path, f))
                 for f in files_in_dir
                 if (os.path.splitext(f)[1].lower() in acceptable_extensions)]

        books.append((book_dir, files))
    return books


# For debug purposes
if __name__ == "__main__":
    root = './audiobooks'
    books = getbooks(root)
    print(books)
