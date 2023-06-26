import os
import openai
import scipy.io.wavfile as wavfile
from dotenv import load_dotenv
from pydub import AudioSegment
from tqdm import tqdm
load_dotenv()

openai.api_key = os.getenv('OPENAI_API')

SEGMENT_DURATION = 5  # units is min
MSECONDS_IN_MIN = 60 * 1000
TEMP_FOLDER_PATH = 'temp'

class AudioProcesser:
    @staticmethod
    def split_mp3(file_path, temp_folder):
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
        audio = AudioSegment.from_mp3(file_path)
        segment_duration = SEGMENT_DURATION * MSECONDS_IN_MIN
        segments = [audio[i:i + segment_duration] for i in range(0, len(audio), segment_duration)]
        with tqdm(total=len(segments), desc="Splitting") as pbar:
            for i, segment in enumerate(segments):
                segment_file = os.path.join(temp_folder, f"segment{i}.mp3")
                segment.export(segment_file, format="mp3")
                pbar.update(1)
    
    @staticmethod
    def delete_directory(directory_path):
        try:
            if os.path.exists(directory_path):
                for root, dirs, files in os.walk(directory_path, topdown=False):
                    for file_name in files:
                        file_path = os.path.join(root, file_name)
                        os.remove(file_path)
                    for dir_name in dirs:
                        dir_path = os.path.join(root, dir_name)
                        os.rmdir(dir_path)
                os.rmdir(directory_path)
                return f"Directory '{directory_path}' successfully deleted!"
            else:
                return f"Directory '{directory_path}' not found!"
        except Exception as e:
            return f"An error occurred while deleting directory '{directory_path}': {str(e)}"
    
    @staticmethod
    def transcribe_mp3(mp3_file_path):
        AudioProcesser.delete_directory(TEMP_FOLDER_PATH)
        print('Start splitting mp3 file into segments...')
        AudioProcesser.split_mp3(mp3_file_path, TEMP_FOLDER_PATH)
        transcript_text = ""
        segment_files = [f for f in os.listdir(TEMP_FOLDER_PATH) if f.endswith(".mp3")]
        print('Start transcribing...')
        with tqdm(total=len(segment_files), desc="Transcribing") as pbar:
            for segment_file_name in segment_files:
                segment_path = os.path.join(TEMP_FOLDER_PATH, segment_file_name)
                audio_file = open(segment_path, "rb")
                try:
                    transcript = openai.Audio.transcribe("whisper-1", audio_file, language='zh')
                    segment_transcript = transcript["text"]
                    transcript_text += segment_transcript + "\n"
                except openai.error.APIError as e:
                    print(f"Error transcribing segment: {segment_file_name}. Error: {e}")
                pbar.update(1)
        os.remove(mp3_file_path)
        return transcript_text
    
    @staticmethod
    def save_audio_as_mp3(audio_tuple, output_file_path):
        sample_rate, audio_data = audio_tuple
        wavfile.write('temp.wav', sample_rate, audio_data)
        audio = AudioSegment.from_wav('temp.wav')
        audio.export(output_file_path, format='mp3')
        os.remove('temp.wav')