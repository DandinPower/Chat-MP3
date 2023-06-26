from src.audio_processor import AudioProcesser
from src.text_processor import TextProcessor
import gradio as gr

TEMP_UPLOAD_MP3_PATH = "uploaded_file.mp3"

def process_audio(audio):
    AudioProcesser.save_audio_as_mp3(audio, TEMP_UPLOAD_MP3_PATH)
    transcript = AudioProcesser.transcribe_mp3(TEMP_UPLOAD_MP3_PATH)
    print("Transcribe Done!")
    return transcript

def asked_question(question, transcription):
    if not transcription:
        return "You don't have any exist transcription!"
    print("Generate Answer...")
    answer = TextProcessor.asked_question_by_text(question, transcription)
    print("Generate Done!")
    return answer

with gr.Blocks() as demo:
    with gr.Tab("Get Transcription By MP3"):
        with gr.Column():
            audio = gr.Audio(label="mp3 file")
        with gr.Column():
            transcript = gr.Text(label="Transcription")
        get_transcription_btn = gr.Button("Get Transcription")
        get_transcription_btn.click(process_audio, inputs=[audio], outputs=[transcript])
    with gr.Tab("Asked Question About the Transcription"):
        with gr.Column():
            question = gr.Textbox(label="Question")
        with gr.Column():
            answer = gr.Text(label="Answer")
        asked_question_btn = gr.Button("Ask Question")
        asked_question_btn.click(asked_question, inputs=[question, transcript], outputs=[answer])

if __name__ == "__main__":
    demo.launch(share=True)