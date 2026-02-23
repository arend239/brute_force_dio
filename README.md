🛡️ Cybersecurity Lab: Brute Force & Mitigation com Medusa

Este repositório documenta um laboratório prático de auditoria de segurança focado em ataques de força bruta (Brute Force) e técnicas de mitigação. O objetivo é simular cenários reais de invasão em ambientes controlados para entender vulnerabilidades comuns e como corrigi-las.

---

## Tecnologias e Ferramentas

- **SO Atacante:** Kali Linux (Rolling Edition)

- **SO Alvo:** Metasploitable 2 (Linux vulnerável por design)

- **Ferramentas:** * `Nmap`: Varredura de rede e enumeração de serviços.

    - `Medusa`: Ataques de força bruta modular e paralelo.

    - `DVWA`: Aplicação web para testes de vulnerabilidades.

- **Rede:** VirtualBox Host-Only.

## 1. Configuração do Ambiente

Para garantir a ética e segurança dos testes, as máquinas foram configuradas em uma rede **Host-Only**. Isso impede que o tráfego de ataque saia para a internet física.

> **Configuração IP:**
>
> - **Kali Linux:** `192.168.56.X`
>
> - **Metasploitable 2:** `192.168.56.Y`
>

`ip addr`
##  2. Fase de Reconhecimento (Footprinting)

Antes de atacar, realizamos uma varredura para identificar portas abertas e versões de serviços.

```
nmap -sV -p- 192.168.56.101
```

**Descobertas Críticas:**

- Porta 21 (FTP) - Versão: vsftpd 2.3.4

- Porta 445 (SMB) - Versão: Samba 3.X

- Porta 80 (HTTP) - Executando Apache com DVWA.

---

## 3. Cenários de Ataque

### A. Força Bruta em FTP

O FTP é um serviço comum para transferência de arquivos, mas frequentemente expõe credenciais fracas.

**Comando utilizado:**

Bash

```
medusa -h 192.168.56.101 -u msfadmin -P wordlists/common_passwords.txt -M ftp
```

- **Resultado:** `ACCOUNT FOUND: [ftp] User: msfadmin Password: msfadmin`

- **Impacto:** Acesso total aos arquivos do servidor.


### B. Password Spraying em SMB

Testamos uma única senha contra vários usuários possíveis, evitando account lockout.

---

## 4. Medidas de Mitigação (Prevenção)

1. **Políticas de Complexidade:** Senhas com no mínimo 12 caracteres, incluindo símbolos e números.

2. **MFA (Autenticação de Dois Fatores):** Essencial para serviços críticos como FTP e acesso Web.

3. **Fail2Ban:** Configurar o servidor para bloquear IPs que falham mais de 3 tentativas em 5 minutos.

4. **Desativação de Serviços Legados:** Se o FTP não for necessário, deve ser substituído por SFTP ou desativado.

_"Os IPs utilizados neste laboratório foram atribuídos dinamicamente pelo DHCP do VirtualBox, sendo 192.168.56.101 o endereço identificado para o alvo."_