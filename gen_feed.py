import os
from feedgen.feed import FeedGenerator
import parse_dir


# Generates the .xml files in the ./gen directory
def gen_feed(host):
    # Make sure we have somewhere to save the files
    if not os.path.isdir('./gen'):
        print('There is no audiobooks directory. Create ./audiobooks')

    # Uses parse_dir.py to get the books and files
    books = parse_dir.getbooks('./audiobooks')

    for (book, files) in books:
        # Creates a new feed for each book
        fg = FeedGenerator()
        fg.load_extension('podcast')

        fg.podcast.itunes_category('Audiobook')

        for (file_name, file_path) in files:
            # the 1: removes the period because the base dir is ./audiobooks
            url = host + file_path[1:]

            fe = fg.add_entry()
            fe.id(url)
            fe.title(file_name)
            fe.description('Segment of the book')
            fe.enclosure(url, str(os.path.getsize(file_path)), 'audio/mpeg')

        fg.title('Audiobook: ' + book)
        fg.link(href=host, rel='self')
        fg.description('A book')
        fg.rss_str(pretty=True)

        # Saves the file
        fg.rss_file(os.path.join('./gen/', book + '.xml'))
