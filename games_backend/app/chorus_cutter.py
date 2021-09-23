from pychorus.helpers import find_and_output_chorus
from pydub import AudioSegment

def process_one_song(input_path, output_path):
    # CONSTANTS
    chorus_len = 15
    fade_msec = 2000
    msec = 1000
    # CONSTANTS
    
    start = find_and_output_chorus(input_path, None, chorus_len)*msec
    end = start+chorus_len*msec
    song = AudioSegment.from_mp3(input_path)
    extract = song[start:end]
    extract = extract.fade_in(fade_msec).fade_out(fade_msec)
    extract.export(output_path, format="mp3")