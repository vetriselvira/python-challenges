def get_filename(name):
    name = name.split('/')
    return name[-1]


print(get_filename("C:/Projects/pil_tests/ascii/edabit.txt")) # "edabit.txt"

print(get_filename("C:/Users/johnsmith/Music/Beethoven_5.mp3")) # "Beethoven_5.mp3"

print(get_filename("ffprobe.exe")) # "ffprobe.exe"
