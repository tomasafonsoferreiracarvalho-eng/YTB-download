# YTB-download
# 🎵 YouTube Music Downloader

Script simples em Python para fazer download de músicas do YouTube em **MP3**.

---

## ⚙️ Requisitos

Antes de usar, instala o seguinte:

### 1. Python
Vai a https://python.org/downloads e instala a versão mais recente.  
> ⚠️ Durante a instalação, marca a opção **"Add Python to PATH"**

### 2. yt-dlp
```bash
pip install yt-dlp
```

### 3. ffmpeg
Necessário para converter o áudio para MP3.
```bash
winget install ffmpeg
```
> Depois de instalar, **fecha e abre o cmd de novo** para o reconhecer.

---

## 🚀 Como usar

### 1. Abre o cmd na pasta onde tens o script
Na barra de endereços do explorador de ficheiros, clica na pasta e escreve `cmd`.

### 2. Corre o script com o link do YouTube
```bash
python youtube_downloader.py https://www.youtube.com/watch?v=...
```

O MP3 fica guardado na mesma pasta onde estás.

---

## 📋 Exemplos

```bash
# Vídeo normal
python youtube_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ

# YouTube Shorts
python youtube_downloader.py https://www.youtube.com/shorts/CdoCa3FIv2g
```

---

## ❌ Erros comuns

| Erro | Solução |
|------|---------|
| `ffprobe and ffmpeg not found` | Instala o ffmpeg com `winget install ffmpeg` e reabre o cmd |
| `python não é reconhecido` | Reinstala o Python e marca **"Add Python to PATH"** |
| `No module named yt_dlp` | Corre `pip install yt-dlp` |
| `WARNING: No supported JavaScript runtime` | Instala o Node.js em https://nodejs.org (opcional) |

---

## 📁 Onde fica o ficheiro?

Na pasta onde abriste o cmd. Se abriste o cmd no Ambiente de Trabalho, o MP3 fica no Ambiente de Trabalho.
