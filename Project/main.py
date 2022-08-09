import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

# pip install pyaudio
# pip install pydub
# pip install pandas
# pip install gTTS


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language,tld="com", slow=False)
    myobj.save(filename)
    

# This function returns pydubs audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')

    # 1 - Generate kripya dheyan dijiye
    start = 000
    finish = 2680
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 2 is from-city

    # 3 - Generate se chalkar
    start = 8570
    finish = 9330
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 4 is via-city

    # 5 - Generate ke raaste
    start = 10530
    finish = 11500
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6 is to-city

    # 7 - Generate ko jaane wali
    start = 12000
    finish = 13000
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8 generate  gaadi sakhya
    start = 2900
    finish = 3900
    audioProcessed = audio[start:finish]
    audioProcessed.export("8_hindi.mp3", format="mp3")

    # 9 is train no and name

    # 10 - Generate apne nirdharit sme 
    start = 15550
    finish = 17200
    audioProcessed = audio[start:finish]
    audioProcessed.export("10_hindi.mp3", format="mp3")

    # 11 Generate pr platform no
    start = 19900
    finish = 21000
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")

    # 12 is platform number

    # 13 - Generate se jaegi
    start = 21800
    finish = 23000
    audioProcessed = audio[start:finish]
    audioProcessed.export("13_hindi.mp3", format="mp3")

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 - Generate from-city
        textToSpeech(item['from'], '2_hindi.mp3')

        # 4 - Generate via-city
        # textToSpeech(item['via'], '4_hindi.mp3')
        textToSpeech(item.get('via'), '4_hindi.mp3')

        # 6 - Generate to-city
        # textToSpeech(item['to'], '6_hindi.mp3')
        # textToSpeech(df.get('to'), '6_hindi.mp3')
        textToSpeech(item.get('to'), '6_hindi.mp3')

        # 9 - Generate train no and name
        # textToSpeech(item['train_no'] + " " + item['train_name'], '9_hindi.mp3')
        textToSpeech(str(item.get('train_no')) + " " + item.get('train_name'), '9_hindi.mp3')

        # 12 - Generate platform number
        # textToSpeech(item['platform'], '12_hindi.mp3')
        textToSpeech(item.get('platform'), '12_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,14)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")