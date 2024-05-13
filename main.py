from pytube import YouTube


def download(url, mode='both'):
    ytobject = YouTube(url)
    if mode == 'both':
        ytobject = ytobject.streams.get_highest_resolution()
        file_type = 'mp4'
    elif mode == 'audio':
        ytobject = ytobject.streams.filter(only_audio=True)
        ytobject = ytobject[0]
        file_type = 'mp3'
    elif mode == 'video':
        file_type = 'mp4'
        ytobject = ytobject.streams.filter(only_video=True)
        ytobject = ytobject[0]

    else:
        print("Sorry, this is not a preset...")
    try:
        ytobject.download(output_path='./', filename=f'{ytobject.title}.{file_type}')
    except Exception as e:
        print("An error has occurred")
        print(e)
    # print("Download is completed successfully")