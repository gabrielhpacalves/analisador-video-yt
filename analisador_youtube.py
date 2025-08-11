import os
from pytubefix import YouTube
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def download_audio(url):
    print("Baixando o áudio do vídeo...")
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        out_file = audio_stream.download(output_path="./temp")
        
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        
        print(f"Áudio baixado e salvo como: {new_file}")
        return new_file
    except Exception as e:
        print(f"Erro ao baixar o áudio: {e}")
        return None

def transcribe_audio(audio_path):
    print("Iniciando a transcrição do áudio...")
    try:
        with open(audio_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        print("Transcrição concluída.")
        return transcript.text
    except Exception as e:
        print(f"Erro na transcrição: {e}")
        return None

def summarize_text(text):
    print("Gerando o resumo do texto...")
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente útil. Sua tarefa é resumir o texto fornecido de forma clara e concisa."},
                {"role": "user", "content": f"Resuma o seguinte texto:\n\n{text}"}
            ]
        )
        summary = response.choices[0].message.content
        print("Resumo concluído.")
        return summary
    except Exception as e:
        print(f"Erro ao gerar o resumo: {e}")
        return None

def main(url):
    audio_file_path = download_audio(url)
    if not audio_file_path:
        return

    transcribed_text = transcribe_audio(audio_file_path)
    if not transcribed_text:
        return

    summary = summarize_text(transcribed_text)
    if summary:
        print("\n--- Resumo do Vídeo ---")
        print(summary)

    try:
        os.remove(audio_file_path)
        print(f"\nArquivo temporário removido: {audio_file_path}")
    except OSError as e:
        print(f"Erro ao remover arquivo temporário: {e}")

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=tm6zdzjOjSg"
    main(video_url)
