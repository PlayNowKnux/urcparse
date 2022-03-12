import urcparse, pydub, sys

version = 1

args = sys.argv

data = urcparse.parse(open(args[1], "r").read())

print("URC to Audio Compiler v" + str(version))

exportf = data.metadata["ExportFile"]
music = pydub.AudioSegment.from_file(data.metadata["BaseFile"])

print(data.__soundlist__)
print(data.events)
print(str(data.events[0]))
sounds = {}

# open("log.json", "w").write(json.dumps(dict(data)))

for sound in data.sounds:
    sounds[sound.path] = pydub.AudioSegment.from_file(sound.path)

print(sounds)

# print offsets and how many bars they have
warningBars = []
for i in range(0, len(data.timeChanges)):
    if i != 0:
        ms_num = data.timeChanges[i].offset - data.timeChanges[i - 1].offset
        qnote = data.timeChanges[i - 1].bar_len() / 4
        bnum = data.timeChanges[i - 1].bar_num(ms_num)
        remainingBar = ms_num - (data.timeChanges[i - 1].bar_len() * (int(bnum) or 1))
        # print the number of bars for the previous offset
        print("\t" + str(bnum) + " bars (" + str(ms_num) + "/" + str(
            data.timeChanges[i - 1].bar_len() * (int(bnum) or 1)) + " ms)")
        if qnote > remainingBar > 0:
            warningBars.append([int(bnum) + data.timeChanges[i - 1].startBar, remainingBar, int(qnote)])

    print(str(data.timeChanges[i]))

print("")
for i in warningBars:
    print("!!! Bar " + str(i[0]) + " is " + str(i[1]) + " ms long! (Quarter note is " + str(i[2]) + " ms)")

for i in data.events:
    gain = 0
    if i.has_param("gain"):
        gain = int(i.params["gain"])
    music = music.overlay(sounds[i.event], position=i.time, gain_during_overlay=gain)

music.export(out_f=exportf, format="mp3")
