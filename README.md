# RCDIDN V1.0 — HACKER KILLER

```
██████╗  ██████╗ ██████╗ ██╗██████╗ ███╗   ██╗
██╔══██╗██╔════╝ ██╔══██╗██║██╔══██╗████╗  ██║
██████╔╝██║      ██║  ██║██║██║  ██║██╔██╗ ██║
██╔══██╗██║      ██║  ██║██║██║  ██║██║╚██╗██║
██║  ██║╚██████╗ ██████╔╝██║██████╔╝██║ ╚████║
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚═════╝╚═╝  ╚═══╝
```

<p align="center">
  <b>Active Defense System — Turning Your Server Into a Hacker Trap Machine</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Encryption-AES--256--GCM-red?style=for-the-badge&logo=shield&logoColor=white"/>
  <img src="https://img.shields.io/badge/Features-38-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Novel%20Contributions-9-purple?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Dependencies-1%20only-yellow?style=for-the-badge"/>
</p>

<p align="center">
  <i>Radioactive Cognitive Data Indonesia — Defensive Security System</i><br/>
  Created by <b>Muhamad Fadhil Faturohman</b>
</p>

---

## Table of Contents

1. [Why RCDIDN Was Built](#why-rcdidn-was-built)
2. [What You Get — 38 Features, 1 File](#what-you-get--38-features-1-file)
3. [9 Novel Research Contributions](#9-novel-research-contributions)
4. [Quick Start](#quick-start--2-commands)
5. [Full Installation Guide](#full-installation-guide)
6. [Security Architecture](#security-architecture)
7. [Commander Shell Reference](#commander-shell-reference)
8. [CLI Reference](#cli-reference)
9. [Setting Up the AI Honeypot](#setting-up-the-ai-honeypot-multi-provider)
10. [HIVE-MIND Webhook Setup](#hive-mind-webhook-setup)
11. [24/7 Auto-Run Setup](#247-auto-run-setup)
12. [File Locations](#file-locations)
13. [Environment Variables](#environment-variables)
14. [FAQ](#faq)
15. [License & Attribution](#license--attribution)

---

## Why RCDIDN Was Built

Every day, servers around the world are silently probed, scanned, and broken into. Developers and small server owners face the same dead end with every existing tool:

| Tool | The Real Problem |
|------|-----------------|
| **Fail2ban** | Purely reactive — blocks IPs *after* the attack. No intelligence collected. Attackers rotate IPs and walk straight back in. |
| **Cowrie** | Excellent SSH honeypot in isolation, but complex to configure, narrow in scope (SSH only), and generates no actionable legal evidence. |
| **ModSecurity** | Powerful WAF, but completely web-layer only — blind to port scanners, SSH brute force, and network-level intrusion. |

**None of these tools fight back. None study the attacker. None produce evidence for prosecution.**

RCDIDN solves all of this simultaneously with one Python file and one dependency.

---

## What You Get — 38 Features, 1 File

### Core Defense (7 features)

| # | Feature | Description |
|---|---------|-------------|
| 01 | True AES-256-GCM Engine | PBKDF2HMAC (600k iterations, SHA-256) + AES-GCM authenticated encryption |
| 02 | Zero-Knowledge Vault | Encrypts files into `~/.rcdidn_vault` — no plaintext key ever stored on disk |
| 03 | Immutable Lock | Locks vault files at OS level (`chattr +i` / `chflags uchg`) |
| 04 | Encrypted Shadow Manifest | AES-GCM encrypted map of original → vault file locations |
| 05 | MIRAGE DROP Canary | Replaces real files with adaptive fake credentials (CSPRNG-generated per deployment) |
| 06 | Automatic Git Shield | Auto-updates `.gitignore` with specific RCDIDN filenames only |
| 07 | Anti-Debugging & Memory Wipe | Wipes master key from RAM after use; blocks debugger-based reverse engineering |

### Honeypot & Tarpit (3 features)

| # | Feature | Port | Description |
|---|---------|------|-------------|
| 08 | AI Interrogator | 2323 | Fake Linux terminal powered by **Gemini, OpenAI, Anthropic Claude, or DeepSeek** — hard-limited to 100 API calls/session |
| 09 | Endless Tarpit SSH | 2222 | Fake SSH that freezes attacker scanning tools — auto-expires after 1 hour |
| 10 | Endless Tarpit MySQL | 3306 | Fake MySQL that freezes attacker tools — auto-expires after 1 hour |

### IPS Firewall (2 features)

| # | Feature | Description |
|---|---------|-------------|
| 11 | Omniversal Auto-Blacklist | Bans attacker IPs via `iptables` / `netsh` / `route` — IP validated before any subprocess call |
| 12 | Background IPS Daemon | Runs silently as a separate process 24/7 |

### Sentinel UI — Psychological Counterattack (7 features)

| # | Feature | Description |
|---|---------|-------------|
| 13 | PHP Sentinel Injection | Injects security logic into `index.php` — vault path never disclosed |
| 14 | Pre-Ransomed Camouflage | Shows fake LockBit ransomware page to automated web scanners |
| 15 | RCE Mirror Shield | Reflects injected commands back at the attacker (XSS-safe via `textContent`) |
| 16 | WebRTC VPN Piercer | Extracts attacker's real IP even through VPN or proxy |
| 17 | Voice of God | Attacker's browser speaks: *"Target Locked. Disconnect now."* |
| 18 | ISP Abuse Auto-Draft | Animated fake legal report submission targeting attacker's ISP |
| 19 | ZIP Bomb Trap | Returns a fake 10GB response to crash backup-scanning tools |

### Threat Intelligence (8 features)

| # | Feature | Description |
|---|---------|-------------|
| 20 | PHANTOM CLOCK | Measures LLM dwell time vs static tarpit — novel research metric |
| 21 | MINDPRINT Profiling | Classifies attackers into behavioral personas per session |
| 22 | MIRAGE DROP Hit Tracker | Logs every canary file access with IP, timestamp, and SHA-256 hash |
| 23 | Threat Intelligence Dashboard | Real-time ASCII dashboard generated from live log data |
| 24 | HTML Report Generator | Chart.js report ready for conference and academic presentation |
| 25 | Structured JSON Logging | Every event logged as JSON — fully SIEM-compatible |
| 26 | Geolocation IP Enrichment | HTTPS lookup: country, city, ISP, ASN per attacker IP |
| 27 | HIVE-MIND Webhook | HTTP POST sync to configurable central threat intel aggregation server |

### System (5 features)

| # | Feature | Description |
|---|---------|-------------|
| 28 | Self-Test Suite | 6 unit tests verifying all core cryptographic and logging functions |
| 29 | Log Rotation | Automatic rotation at 5MB per log file — prevents unbounded disk growth |
| 30 | Vault Authentication | Requires Master Password for all vault operations (Zero-Knowledge) |
| 31 | Vault Backup Reminder | Prompts backup after every run |
| 32 | Interactive Commander Shell | Metasploit-style menu with all 38 features accessible by name |

### Advanced Cyber Warfare (6 features)

| # | Feature | Description |
|---|---------|-------------|
| 33 | TEMPORAL DECEPTION GRID | 7 timing profiles: `off`, `random_chaos`, `busy_server`, `flapping`, `degrading`, `recovering`, `tarpit_extreme` |
| 34 | DARK MIRROR | Detects attacker OS and tools from initial packet, presents matching fake terminal environment |
| 35 | HONEYPOT ECONOMICS | Calculates dollar-value economic damage imposed on attacker operations |
| 36 | DIGITAL PHEROMONE | Deploys 5 bait file types; measures hit latency per bait category |
| 37 | GHOST NETWORK | Simulates 10 fake enterprise hosts (DC, DB, Web, Backup, Monitor, CI/CD, SMB, Mail, Redis, LDAP) |
| 38 | REGULATORY TRAP | Generates forensic-grade evidence bundles with SHA-256 chain of custody |

---

## 9 Novel Research Contributions

> None of the following features exist in any prior open-source tool — not Cowrie, not Fail2ban, not Honeyd, not any published honeypot framework.

### Novel #1 — PHANTOM CLOCK
The world's first tool to empirically measure how much longer an LLM-powered fake terminal retains an attacker compared to a static tarpit. Logs per-session dwell time, command count, engagement score, and a direct AI vs tarpit effectiveness multiplier.

> Target: *"PHANTOM CLOCK: Measuring Attacker Engagement in LLM-Powered Deception Terminals"* — USENIX Security, IEEE S&P

### Novel #2 — MINDPRINT
Cross-session behavioral fingerprinting that classifies each session into `APT_CANDIDATE`, `PERSISTENT`, `BOTNET_NODE`, `SCRIPTKIDDIE`, or `RESEARCHER` based on hit frequency, port patterns, tool signatures, and timing variance.

> Target: *"Beyond IP: Cross-Server Behavioral Fingerprinting for Attacker Re-identification"* — DEF CON, Black Hat, IEEE S&P

### Novel #3 — MIRAGE DROP
CSPRNG-regenerated canaries on every deployment — each fake AWS key, database password, and Stripe token is unique. Cannot be fingerprinted because no two deployments are identical.

> Target: *"Adaptive Canaries: Dynamic Credential Deception Resistant to Attacker Fingerprinting"* — NDSS, Black Hat Arsenal

### Novel #4 — TEMPORAL DECEPTION GRID
Seven switchable timing profiles (`busy_server`, `flapping`, `degrading`, `recovering`, `random_chaos`, `tarpit_extreme`, `off`) that corrupt the scanner's timing model and cause automated tools to misfire, time out, or misclassify the server.

> Target: *"Time as Deception: Controlled Temporal Manipulation in Interactive Honeypots"* — USENIX Security, NDSS

### Novel #5 — DARK MIRROR
Detects attacker OS and tool stack from initial packet data (UA strings, protocol signatures, binary patterns) then presents a familiar-looking terminal environment — Kali attackers see a Kali shell, Windows attackers see CMD. Logs per-session fingerprint data to a dedicated `dark_mirror.log`.

> Target: *"Target-Adaptive Deception: Real-Time Attacker Environment Mirroring in Interactive Honeypots"*

### Novel #6 — HONEYPOT ECONOMICS
Multiplies attacker hourly operational cost × total dwell time, calculates total financial damage in USD. Every second an attacker spends in a tarpit is a second not spent attacking another target — this makes it auditable.

> Target: *"Measuring Defensive ROI: Quantifying Economic Costs Imposed on Adversaries Through Active Deception"* — RSA Conference, Black Hat

### Novel #7 — DIGITAL PHEROMONE
Five distinct bait file types (`exposed_env`, `fake_admin`, `git_exposed`, `phpinfo_bait`, `backup_bait`) that actively attract scanner traffic. Logs to a dedicated `pheromone.log` for hit latency analysis per bait category — a metric never published before.

> Target: *"Digital Pheromones: Measuring Attacker Attraction Latency Across Deception Bait Types"*

### Novel #8 — GHOST NETWORK
Single-host simulation of 10 distinct fake enterprise hosts via round-robin connection assignment. Each connection receives a different host identity with appropriate banner, OS, role, and fake responses: Domain Controller (Exchange SMTP), Production DB (MySQL), Web Frontend (Apache), Backup Server (SSH), Monitoring (Grafana), CI/CD (Jenkins), File Server (SMB), Mail Server (Postfix), Redis Cache, LDAP Auth Server.

> Target: *"Ghost Network: Single-Host Simulation of Enterprise Topologies for Lateral Movement Detection"* — DEF CON, Black Hat Arsenal

### Novel #9 — REGULATORY TRAP
SHA-256 hashes all collected log files, embeds a cryptographic chain of custody into the evidence report, and packages everything into a `chmod 600` password-protected ZIP. Generates formatted reports ready to submit to ID-CERT Indonesia, BSSN, and INTERPOL.

> Target: *"Legal-Grade Honeypot Evidence: Chain of Custody Automation for Cybercrime Prosecution"* — INTERPOL Cybercrime Conference

---

## Quick Start — 2 Commands

```bash
pip install cryptography
python3 rcdidn.py
```

That's it. The interactive commander opens with all 38 features ready.

> **IMPORTANT: Never run `python3 rcdidn.py` from inside VSCode's debugger.** The green play button activates `sys.gettrace()`, which triggers RCDIDN's anti-debugging protocol. Always run from a terminal. If you need to use coverage tools, set `RCDIDN_NO_DESTRUCT=1` first.

---

## Full Installation Guide

### Linux / Ubuntu / Debian (Recommended)

```bash
# Step 1: Update and install Python
sudo apt update && sudo apt install -y python3 python3-pip

# Step 2: Download RCDIDN
git clone https://github.com/[username]/rcdidn
cd rcdidn

# Step 3: Install the only dependency
pip install cryptography

# Step 4: Run self-test (all 6 must show PASS)
RCDIDN_NO_DESTRUCT=1 python3 rcdidn.py --test

# Step 5: Run RCDIDN
python3 rcdidn.py
```

### Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY rcdidn.py .
RUN pip install cryptography
EXPOSE 2222 2323 3306 4444 8080
CMD ["python", "rcdidn.py", "--ips_daemon"]
```

```bash
docker build -t rcdidn .
docker run -d \
  --name rcdidn \
  -p 2222:2222 -p 2323:2323 -p 3306:3306 -p 4444:4444 -p 8080:8080 \
  -e RCDIDN_AI_PROVIDER="gemini" \
  -e RCDIDN_AI_KEY="your_api_key_here" \
  -v rcdidn_data:/root/.sys_meta_rcdidn \
  -v rcdidn_vault:/root/.rcdidn_vault \
  --restart always \
  rcdidn
```

### Shared Hosting (cPanel)

```bash
pip3 install cryptography --user
python3 rcdidn.py --run
```

> Note: Honeypot ports (2222, 2323, 3306, 4444, 8080) are blocked on shared hosting. Vault encryption, MIRAGE DROP canary deployment, PHP Sentinel injection, and JSON logging all work normally.

---

## Security Architecture

### Cryptographic Stack

```
Encryption Algorithm  :  AES-256-GCM
                         Authenticated Encryption with Associated Data
                         Provides confidentiality + integrity + authenticity.
                         Detects any tampering before decryption begins.

Key Derivation        :  PBKDF2HMAC
  Hash function       :  SHA-256
  Iterations          :  600,000
                         NIST recommends ≥ 210,000 for SHA-256 as of 2023.
                         RCDIDN exceeds this by 2.8× for future-proof resistance.
  Salt                :  32 bytes — os.urandom() — unique per vault — stored on disk
  Output key length   :  32 bytes (AES-256)

Nonce per file        :  12 bytes — os.urandom() — unique per file per encryption
                         GCM nonce reuse is catastrophic; RCDIDN enforces uniqueness
                         with no exceptions — new nonce for every encryption operation.

Zero-Knowledge        :  The Master Password NEVER touches disk in any form.
                         Only the cryptographic salt is stored.
                         Salt alone = useless without the password.
                         Password alone = useless without the salt.

Memory hygiene        :  del master_key; gc.collect()
                         Executed immediately after every cryptographic operation.
```

### Security Audit — Complete Patch Record

#### Critical — Fixed

| ID | Vulnerability | Fix Applied |
|----|---------------|-------------|
| C1 | **IP Injection** — attacker IP passed to `iptables` without validation | `is_valid_ip()` using Python `ipaddress` module — rejects non-IP before any subprocess call |
| C2 | **Path Disclosure** — vault path embedded in generated PHP sentinel | PHP now logs to local `rcdidn_web.log` only |
| C3 | **Unsafe `kill -9`** — PID from untrusted file passed to `sudo kill` | PID validated via regex + range check + `/proc/{pid}` existence |
| C4 | **DOM-based XSS** — URL `?cmd=` inserted via `innerHTML` | Replaced with `textContent` + `createElement` |

#### High — Fixed

| ID | Fix Applied |
|----|-------------|
| H1 | PRNG replaced with `secrets.choice()` for all canary generation |
| H2 | `MAX_TARPIT_SECONDS=3600` — tarpit sessions auto-close after 1 hour |
| H3 | `MAX_GEO_CACHE=5000` — oldest GeoIP entry evicted at limit |
| H4 | `digestmod=hashlib.sha256` added to `hmac.new()` |
| H5 | `conn.settimeout(30)` before every `recv()` |
| H6 | Ghost Network refactored to thread-per-connection |

#### Additional Fixes (v1.0 → current)

| Fix | Description |
|-----|-------------|
| Anti-debug safe flag | `RCDIDN_NO_DESTRUCT=1` env var prevents self-destruct during `coverage run` / `pytest-cov` |
| Salt size corrected | Salt is now 32 bytes (matches documented specification) |
| Gitignore specificity | `*.bin` replaced with specific RCDIDN filenames only |
| Temporal profiles | All 7 profiles now implemented: `off`, `random_chaos`, `busy_server`, `flapping`, `degrading`, `recovering`, `tarpit_extreme` |
| PID verification | `cmd_status()` now verifies daemon is alive via `os.kill(pid, 0)` |
| Pheromone ZIP | `backup_2024_prod.zip` written as proper bytes, not encoded string |
| Dedicated log files | Dark Mirror, Economics, Pheromone, Ghost Network each write to dedicated log files |
| HIVE-MIND | Actual HTTP POST webhook with configurable URL and auth header |
| DARK MIRROR | Real OS/tool fingerprinting from initial packet data |
| GHOST NETWORK | 10 distinct fake enterprise hosts with authentic banners |

---

## Commander Shell Reference

Run `python3 rcdidn.py` to enter the interactive commander:

```
RCDIDN > help

  CORE DEFENSE
  run          → Vault files + deploy MIRAGE DROP canaries
  restart      → Re-lock files with current key
  restore      → Decrypt all files back to original
  gk           → Rotate Master Password

  IPS & HONEYPOT
  ips start    → Start IPS + AI Honeypot + Ghost Network
  ips stop     → Stop all honeypot daemons

  THREAT INTELLIGENCE
  stats        → Live threat intelligence dashboard
  profile      → MINDPRINT attacker behavioral profiling
  dwelltime    → PHANTOM CLOCK LLM dwell time analysis
  canary       → MIRAGE DROP canary hit tracker
  report       → Generate HTML threat intelligence report

  NOVEL RESEARCH FEATURES
  temporal                    → TEMPORAL DECEPTION GRID status
  temporal profile <n>        → Switch profile:
                                 off|random_chaos|busy_server|flapping|
                                 degrading|recovering|tarpit_extreme
  mirror                      → DARK MIRROR (Port 8080)
  mirror stats                → Dark Mirror session statistics
  economics                   → HONEYPOT ECONOMICS
  pheromone deploy [target]   → Deploy bait files
  pheromone stats             → Pheromone hit statistics
  ghostnet                    → GHOST NETWORK (Port 4444)
  ghostnet stats              → Ghost Network topology hit stats
  evidence collect            → Collect all forensic evidence
  evidence report interpol    → INTERPOL format
  evidence report idcert      → ID-CERT Indonesia format
  evidence report bssid       → BSSN Indonesia format

  SYSTEM
  test         → Run self-test suite (6 unit tests)
  status       → Show vault and daemon status
  help         → Show this menu
  exit         → Exit commander

  AI CONFIG
  setkey       → Set AI provider + key
  aikey        → Show active AI provider and key status
  hiveset      → Configure HIVE-MIND webhook URL
```

---

## CLI Reference

```bash
python rcdidn.py                   # open interactive commander shell
python rcdidn.py --run             # vault all sensitive files immediately
python rcdidn.py --restore         # restore all files from vault
python rcdidn.py --status          # show system status
python rcdidn.py --test            # run self-test suite (6 unit tests)
python rcdidn.py --stats           # show ASCII threat intelligence dashboard
python rcdidn.py --report          # generate HTML threat report
sudo python rcdidn.py --install    # install as systemd service (24/7)
sudo python rcdidn.py --uninstall  # remove systemd service
```

---

## Setting Up the AI Honeypot (Multi-Provider)

The AI Interrogator on port 2323 uses your LLM API key to respond to attacker commands with convincing fake terminal output, maximizing dwell time.

**Step 1 — Open the commander**
```
python3 rcdidn.py
```

**Step 2 — Set your API key**
```
RCDIDN > setkey

  Select your preferred AI Provider:
  1) Gemini (Google) - Default (free tier available)
  2) OpenAI (ChatGPT)
  3) Anthropic (Claude)
  4) DeepSeek

  Choice (1-4) [default: 1]: 1
  API Key: AIzaSyABCDEF...

  [+] API key and provider saved to ~/.bashrc
  [+] AI Honeypot ACTIVATED via GEMINI
  [+] Run 'ips start' to launch AI Interrogator on port 2323
```

**Step 3 — Launch all honeypots**
```
RCDIDN > ips start
  [+] HoneyPort 'AI-Interrogator' active on port 2323 [AI]
  [+] HoneyPort 'Fake-SSH'        active on port 2222 [TARPIT]
  [+] HoneyPort 'Fake-MySQL'      active on port 3306 [TARPIT]
  [+] Ghost Network active on port 4444 — simulating 10 fake enterprise hosts
```

> **Rate limiting:** Each session is hard-capped at 100 API calls. After the cap, RCDIDN returns convincing static fallback responses. For zero cost, use Google Gemini's free tier.

---

## HIVE-MIND Webhook Setup

HIVE-MIND syncs attacker intelligence to a central aggregation server via HTTP POST in real time.

```
RCDIDN > hiveset
  Webhook URL: https://your-server.com/api/hive
  Secret key (optional): your_secret_token
```

**Expected POST body:**
```json
{
  "timestamp": "2026-03-17T10:30:00",
  "ip": "1.2.3.4",
  "location": "CN",
  "isp": "AS4134 Chinanet",
  "source": "prod-server-01",
  "version": "RCDIDN_V1.0"
}
```

The secret is sent as `X-RCDIDN-Key` header for server-side authentication.

---

## 24/7 Auto-Run Setup

### Linux — systemd (Recommended)

```bash
sudo python3 rcdidn.py --install

systemctl status rcdidn
journalctl -u rcdidn -f
sudo python3 rcdidn.py --uninstall
```

### Linux — crontab (Alternative)

```bash
crontab -e
# Add:
@reboot sleep 15 && python3 /root/rcdidn.py --ips_daemon
```

### Windows — Task Scheduler

1. Search "Task Scheduler" → Create Basic Task
2. Trigger: **When the computer starts**
3. Action: **Start a program** → `python`
4. Arguments: `C:\path\to\rcdidn.py --ips_daemon`
5. ✅ Run whether user is logged on or not
6. ✅ Run with highest privileges

---

## File Locations

| Path | Contents |
|------|---------|
| `~/.rcdidn_vault/` | All encrypted files (`*.enc`) |
| `~/.sys_meta_rcdidn/sys_crypto_salt.bin` | Cryptographic salt (32 bytes) — never the password |
| `~/.sys_meta_rcdidn/sys_kern_meta.log` | Main structured JSON log (SIEM-compatible, 5MB rotation) |
| `~/.sys_meta_rcdidn/phantom_clock.log` | PHANTOM CLOCK dwell sessions |
| `~/.sys_meta_rcdidn/canary_hits.log` | MIRAGE DROP canary access log |
| `~/.sys_meta_rcdidn/dark_mirror.log` | DARK MIRROR attacker OS and tool profiles |
| `~/.sys_meta_rcdidn/economics.log` | HONEYPOT ECONOMICS calculation history |
| `~/.sys_meta_rcdidn/pheromone.log` | DIGITAL PHEROMONE bait deployment and hit records |
| `~/.sys_meta_rcdidn/ghost_network.log` | GHOST NETWORK pivot attempt records |
| `~/.sys_meta_rcdidn/legal_evidence/` | REGULATORY TRAP — evidence ZIP + password file (chmod 600) |
| `./core_system_map.bin` | Encrypted Shadow Manifest (per project directory) |
| `./rcdidn_web.log` | PHP Sentinel web event log (web-accessible directory only) |

---

## Environment Variables

| Variable | Description |
|----------|-------------|
| `RCDIDN_AI_KEY` | LLM API key for the AI Interrogator on port 2323 |
| `RCDIDN_AI_PROVIDER` | AI provider: `gemini` (default) \| `openai` \| `anthropic` \| `deepseek` |
| `RCDIDN_HIVE_URL` | HTTP endpoint for HIVE-MIND threat intel sync (optional) |
| `RCDIDN_HIVE_SECRET` | Auth token sent as `X-RCDIDN-Key` header (optional) |
| `RCDIDN_NO_DESTRUCT` | Set to `1` to disable self-destruct during coverage/profiling |

---

## FAQ

**Q: Do I need any technical knowledge to run RCDIDN?**
No. `pip install cryptography` followed by `python3 rcdidn.py` is the entire installation.

**Q: Do I need an AI API key?**
No. 37 of 38 features work without any key. The AI Interrogator falls back to convincing static responses. Type `setkey` at any time to activate AI mode.

**Q: Will RCDIDN slow down my server?**
No. The IPS daemon uses minimal CPU at idle. Honeypot ports only activate when something connects to them.

**Q: What if I forget my Master Password?**
There is no recovery mechanism by design. RCDIDN uses True AES-256-GCM with Zero-Knowledge key derivation. Write it down immediately.

**Q: Can a botnet flood the honeypots and crash my server?**
No. Each honeypot port has a `threading.Semaphore(200)` hard limit. Tarpit sessions auto-expire after 1 hour. The banned-IP set is capped at 10,000 entries.

**Q: Can I use the VSCode debug button?**
No — never. Set `RCDIDN_NO_DESTRUCT=1` if you need to run with a profiler or coverage tool. For normal use, always run from a terminal.

**Q: Is the fake ransomware Sentinel page legal?**
Yes. Displaying a deceptive page to automated attack tools on your own server is a recognized and published honeypot technique.

**Q: How do I configure HIVE-MIND?**
Run `hiveset` in the commander and enter your aggregation server URL. The server should accept HTTP POST with a JSON body. See [HIVE-MIND Webhook Setup](#hive-mind-webhook-setup).

**Q: What ports does RCDIDN use?**
`2222` (fake SSH tarpit), `2323` (AI Interrogator), `3306` (fake MySQL tarpit), `4444` (Ghost Network — 10 fake hosts), `8080` (Dark Mirror — OS fingerprinting).

**Q: How do I report a real attacker to authorities?**
Run `evidence collect` then `evidence report interpol` (international), `evidence report idcert` (Indonesia ID-CERT), or `evidence report bssid` (BSSN Indonesia).

---

## License & Attribution

RCDIDN V1.0 — HACKER KILLER is created by **Muhamad Fadhil Faturohman**.

Licensed under the **MIT License**.

**You are free to:**
- ✅ Use for personal, educational, research, and commercial purposes
- ✅ Modify and distribute freely
- ✅ Include in open-source or closed-source products

**One rule that cannot be waived:**

> The name **Muhamad Fadhil Faturohman** and **RCDIDN V1.0 — HACKER KILLER** must remain clearly visible in all copies, derivative works, and any commercial product or service that incorporates this software.

---

<div align="center">

*"Every server touched by RCDIDN becomes a research laboratory.*
*Every attacker becomes a data point. Every attack becomes knowledge."*

— Muhamad Fadhil Faturohman
Contact: muhamadfadhilfaturohman@gmail.com

</div>
