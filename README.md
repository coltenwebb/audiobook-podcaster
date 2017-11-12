# audiobook-podcaster

I've found myself in the situation where I have an audiobook as a folder on my PC, but want to listen to it on the go.

This is a audiobook server, using podcast technology. You can listen to the audiobooks on your phone/whatever using any podcast app. No need to download glitchy apps!

## Setup

Clone the repository.

```
git clone https://github.com/SirSpoony/audiobook-podcaster.git
```

To make sure it works, add an audiobook to `./audiobooks/` (just put the folder in there, for example `./audiobooks/book/chapter01.mp3` is a file that would be found)

Start the server using `python serve.py`. Using a browser, navigate to `localhost:8000/gen` and you will see a list of available podcast xml files.

If this all works, you can edit `serve.py` and change `PORT` and `HOST` to what you want.

### Dependencies
- feedgen >0.6.1
