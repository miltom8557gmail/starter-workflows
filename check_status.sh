#!/bin/bash
# Coleta dados básicos sem precisar do termux-api
BATERIA=$(cat /sys/class/power_supply/battery/capacity 2>/dev/null || echo "N/A")
MEMORIA=$(free -m | awk '/Mem:/ { print $3 "/" $2 "MB" }')
DISCO=$(df -h /data | awk 'NR==2 { print $3 "/" $2 }')

# Envia para a memória da Akame no Supabase
curl -X POST "https://bfriplrxtleleplhpgwd.supabase.co/rest/v1/memoria" \
-H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU" \
-H "Content-Type: application/json" \
-d "{\"evento\": \"Status Termux\", \"detalhes\": \"Bateria: $BATERIA%, RAM: $MEMORIA, Disco: $DISCO\"}"
