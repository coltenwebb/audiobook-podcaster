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




def acceptable_files(top , files):
        acceptable_extensions = {
            '.mp3', '.wav', '.aiff', '.m4a', '.m4b', '.m4p'
        }
        files = [(os.path.splitext(f)[0], os.path.join(top, f))
                 for f in files
                 if (os.path.splitext(f)[1].lower() in acceptable_extensions)]
        return files

def getbooks(root):
    ''' Returns a list of tuples (file_name, file_path). File name doesn't have an extension'''
    if not os.path.isdir(root):
        print('There is no audiobooks directory. Create ./audiobooks')

    books = []
    for book_dir in listdirs(root):
        book_dir_path = os.path.join(root, book_dir)

        # List the files in the directory
        files_in_dir = listfiles(book_dir_path)
        # Sorts the files alphabetically
        files_in_dir.sort()
        # List of tuples (file_name, file_path), also making sure they are one of the accepted audio file formats
        files = acceptable_files(book_dir_path, files_in_dir)
        books.append((book_dir, files))
    return books


def getbooks_r(root):
    ''' get books tupple (file_name, file_path)  recursively, dive into subdirectories'''
    if not os.path.isdir(root):
        print('There is no %s directory. Create %s' %(root, root))

    books = []
    for top, dirs, files in os.walk(root, followlinks=True):
        files.sort()
        # create records if any suitable files exists
        files = acceptable_files(top, files)
        if files:
            books.append((top, files))

    return books


# For debug purposes
if __name__ == "__main__":
    root = './audiobooks'
    books = getbooks(root)
    print(books)
