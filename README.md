
3. Instalar o FFmpeg
Este projeto depende do FFmpeg para processamento de áudio. Siga as instruções no site oficial para instalá-lo e adicioná-lo à variável de ambiente PATH do seu sistema.

4. Configurar a Chave da API da OpenAI
Para usar as APIs de transcrição e resumo, você precisa de uma chave de API da OpenAI.

Vá para a sua página de chaves da API e crie uma nova chave.

Importante: Não cole a chave diretamente no código. Em vez disso, defina-a como uma variável de ambiente no seu terminal, antes de rodar o script.

# Para Windows PowerShell
$env:OPENAI_API_KEY="SUA_CHAVE_AQUI"

# Para macOS e Linux
export OPENAI_API_KEY="SUA_CHAVE_AQUI"

Substitua SUA_CHAVE_AQUI pela sua chave real.

5. Executar o Script
Depois de todas as configurações, você pode rodar o script.

python analisador_youtube.py

O script irá baixar, transcrever e resumir o vídeo, e o resumo será impresso no terminal.

Personalizando o Projeto
Você pode alterar a URL do vídeo que será analisado, editando a variável video_url no final do arquivo analisador_youtube.py.

if __name__ == "__main__":
    # Substitua a URL abaixo pela URL do vídeo que você quer analisar
    video_url = "https://www.youtube.com/watch?v=tm6zdzjOjSg"
    main(video_url)
