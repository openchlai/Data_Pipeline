#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import hashlib


BASE = os.path.dirname(os.path.realpath(__file__))
MEDIA = BASE + '/media'
JSON = MEDIA + '/JSON'


def sortstorage():
    print("""Manage Directories""")

    if not os.path.isdir(MEDIA + "/WAV"):
        print("""Create WAV Directory""")
        cmd = "mkdir -p " + MEDIA + "/WAV"
        os.system(cmd)

    if not os.path.isdir(MEDIA + "/MP3"):
        print("""Create MP3 Directory""")
        cmd = "mkdir -p " + MEDIA + "/MP3"
        os.system(cmd)

    if not os.path.isdir(MEDIA + "/JSON"):
        print("""Create JSON Directory""")
        cmd = "mkdir -p " + MEDIA + "/JSON"
        os.system(cmd)

    if not os.path.isdir(JSON + "/STATS"):
        print("""Create STATS Directory""")
        cmd = "mkdir -p " + JSON + "/STATS"
        os.system(cmd)

    return True


def sortmedia():
    print("""Sort Initial Media""")
    media = {}

    if not len(os.listdir(MEDIA + "/WAV")):
        print("""Check for Demo Media""")
        if os.path.isdir(MEDIA + "/demo") and os.listdir(MEDIA + "/demo"):
            print("""Use Demo Media""")
            for x in os.listdir(MEDIA + "/demo"):
                f = hashlib.sha256(x.encode()).hexdigest()
                cmd = "cp " + MEDIA + "/demo/" + x + " " + MEDIA + "/WAV/" + f + ".wav"
                os.system(cmd)

    if len(os.listdir(MEDIA + "/WAV")):
        print("""Process Master JSON from WAV""")
        for x in os.listdir(MEDIA + "/WAV"):
            media[x.split(".")[0]] = {}
            media[x.split(".")[0]]['wav'] = True

    with open(JSON + "/master.json", 'w') as fp:
        fp.write(json.dumps(media, indent=4))

    return True


def convertmedia():
    print("""Convert Media from WAV to MP3""")
    # https://gist.github.com/dominicthomas/52e610c9cd4083408371

    tasks = 0

    with open(JSON + "/master.json", 'r') as fp:
        dat = json.loads(fp.read())

    if len(list(dat.keys())):
        # print("""Process Conversion""")
        for x in list(dat.keys()):
            if not os.path.isfile(MEDIA + "/MP3/" + x + ".mp3"):
                print("""Process Conversion""", x)
                tasks += 1
                dat[x]['mp3'] = True
                cmd = "ffmpeg -i " + MEDIA + "/WAV/" + x + ".wav -ab 320k -ac 2 "
                cmd += "-ar 44100 -joint_stereo 0 " + MEDIA + "/MP3/" + x + ".mp3 "
                cmd += "> /dev/null 2>&1"
                os.system(cmd)

    if tasks:
        print("""Processed Conversions""", tasks)
        with open(JSON + "/master.json", 'w') as fp:
            fp.write(json.dumps(dat, indent=4))

    return True


def mediastats():
    print("""Gather Metadata like bit rates, duration etc""")

    with open(JSON + "/master.json", 'r') as fp:
        dat = json.loads(fp.read())


    if len(list(dat.keys())):
        print("""Extract MP3 Stats""", len(dat))

        for x in list(dat.keys()):
            print("""Gather MP3 Stats""", x)
            # https://opensource.com/article/17/6/ffmpeg-convert-media-file-formats
            # https://github.com/slhck/ffmpeg-bitrate-stats
            # we use chunk size of 10 sec

            """
            cmd = "ffmpeg-bitrate-stats -a time -c 10 -of json " + MEDIA
            cmd += "/MP3/" + x + ".mp3 > " + JSON + "/STATS/" + x + ".json"
            os.system(cmd)
            ffprobe -v quiet -show_format -show_streams -print_format json 
            """

            cmd = "ffprobe -v quiet -show_format -show_streams -print_format json "
            cmd += MEDIA + "/MP3/" + x + ".mp3 > " + JSON + "/STATS/" + x + ".json"
            os.system(cmd)

            dat[x]['stats'] = True


            """
            cmd = "sox " + MEDIA + "/WAV/" + x + " -n stat > " + MEDIA
            cmd += "/STATS/" + x.split(".")[0] + ".txt"
            os.system(cmd)

            with open(MEDIA + "/STATS/" + x.split(".")[0] + ".txt", 'r') as fp:
                meta = fp.readline()

            dat[x]['stats'] = {}

            for i in meta.split("\n"):
                keyval = i.split(" ")
                dat[x]['stats'][keyval[0]] = " ".join(keyval[1:])
            """

        with open(JSON + "/master.json", 'w') as fp:
            fp.write(json.dumps(dat, indent=4))

    return True


if __name__ == '__main__':
    x = sortstorage()
    if x:
        x = sortmedia()
        if x:
            x = convertmedia()
            if x:
                x = mediastats()
