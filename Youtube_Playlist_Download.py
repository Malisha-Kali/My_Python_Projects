from pytube import YouTube

base_url = "Your Youtube URL (without index)"
start_index = 2
end_index = 4

for x in range(start_index, end_index + 1):
    YT_Link = base_url + str(x)
    try:
        YT_Download = YouTube(YT_Link).streams.get_highest_resolution().download()
        print(f"Downloaded video {x} Successfully")
    except Exception as e:
        print(f"Error downloading video {x}: {str(e)}")
