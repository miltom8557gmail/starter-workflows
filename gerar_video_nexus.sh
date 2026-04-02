#!/bin/bash
echo "🎬 [CINEMA]: Fundindo frames em vídeo de alta definição..."
ffmpeg -y -framerate 24 -i Frames_Sequenciais/%d_%d.png -c:v libx264 -pix_fmt yuv420p nexus_showcase.mp4
echo "✅ [SUCESSO]: Vídeo 'nexus_showcase.mp4' gerado com sucesso!"
