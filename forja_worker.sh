#!/bin/bash
API_URL="https://bfriplrxtleleplhpgwd.supabase.co/rest/v1/memoria?evento=eq.Comando%20Forja&order=created_at.desc&limit=1"
API_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU"

echo "🔱 Akame Operária: Aguardando ordens da Forja..."

last_cmd=""

while true; do
  # Busca o último comando enviado pelo site
  response=$(curl -s -X GET "$API_URL" -H "apikey: $API_KEY" -H "Authorization: Bearer $API_KEY")
  
  # Extrai o detalhe do comando
  current_cmd=$(echo "$response" | grep -oP '(?<="detalhes":")[^"]*')

  if [ "$current_cmd" != "$last_cmd" ] && [ ! -z "$current_cmd" ]; then
    echo "🛠️ Nova ordem recebida: $current_cmd"
    # Aqui a Akame pode executar o comando ou criar um arquivo
    echo "✅ Executando criação de: $current_cmd"
    last_cmd="$current_cmd"
    # Feedback visual no Termux
    termux-toast "Akame: Processando $current_cmd"
  fi
  sleep 5
done
