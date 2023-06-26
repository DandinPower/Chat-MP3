# Chat-MP3

This project uses the OpenAI API to transcribe MP3 audio files and then perform text processing on the transcriptions. The tool provides two main features: 

1. Get Transcription By MP3: This function takes an MP3 file as input and returns the transcription of the audio.
2. Asked Question About the Transcription: This function allows you to ask a question about a previously generated transcription and it will return an answer based on the context of the transcription.

## Pre-requisites

Before running the program, there are several packages and tools you need to install:

1. `ffmpeg`: This is used for handling multimedia data. Install it by following instructions provided on the [FFMPEG website](https://www.ffmpeg.org/download.html).

2. Python dependencies: The project uses several Python packages which can be installed by running:
```
pip install -r requirements.txt
```

## Configuration

You need to setup your environment variables:

1. Create a `.env` file in the root of the project.
2. Add `OPENAI_API` variable to the `.env` file with your OpenAI API key as its value. It should look like this:
```
OPENAI_API=<Your OpenAI API Key>
```

## Running the program

To run the program, use the following command:
```
python main.py
```
This will launch the Gradio interface where you can upload your MP3 files and get the transcription. You can also ask a question about the transcription.

## Code Overview

The project includes the following main Python files:

1. `src/audio_processor.py`: Contains the `AudioProcesser` class which is responsible for audio processing tasks such as splitting the audio into segments, transcribing the audio, and deleting directories.

2. `src/text_processor.py`: Contains the `TextProcessor` class which uses OpenAI API to generate an answer to a question based on the provided transcription.

3. `main.py`: The main script that uses Gradio to build the interface and uses `AudioProcesser` and `TextProcessor` to process the uploaded MP3 file and generate an answer to the question.

Please make sure to have all the necessary permissions and consider the usage cost of the OpenAI API.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or submit a pull request.

## Contact

For any questions or inquiries, please contact [tomhot246@gmail.com](mailto:tomhot246@gmail.com).