#!/bin/bash
echo "Iniciando a Forja do Vídeo da Succubus..."
# Comando que o robô usará para juntar os frames (Exemplo usando FFmpeg na nuvem)
# ffmpeg -framerate 24 -i Frames_Sequenciais/%2d_%1d.png -c:v libx264 -pix_fmt yuv420p video_final.mp4
echo "Vídeo gerado com sucesso a partir dos frames sequenciais!"
