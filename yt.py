from pytube import YouTube

def downloadvideo(link):
  youtubeObject = YouTube(ytlink)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
      youtubeObject.download()
  except:
    print("ERROR")
  print("Holy moly it worked")

ytlink = input("YouTube URL: ")
downloadvideo(link)
