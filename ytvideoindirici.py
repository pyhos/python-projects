from pytube import YouTube

url = input("İndirilicek video linkini yazınız.")
yt = YouTube(url)

print(f"Video başlığı {yt.title}")
islem = input("Videoyu indirmek istiyormusunuz? (e/h): ")
if(islem == "e" or islem == "E"):
    print("Video indiriliyor.")
    stream = yt.streams.filter(progressive=True).first()
    stream.download()
    print("Video indirildi.")
else:
    print("İşlem iptal edildi.") 