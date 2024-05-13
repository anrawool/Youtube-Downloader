from pytube import YouTube


def download(url):
    ytobject = YouTube(link)
    ytobject = ytobject.streams.get_highest_resolution()
    try:
        ytobject.download(output_path='./')
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
download(link)