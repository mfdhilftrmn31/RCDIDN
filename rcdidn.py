#!/usr/bin/env python3
# ==============================================================================
# MIT License
#
# Copyright (c) 2026 Muhamad Fadhil Faturohman
# RCDIDN V1.0 — HACKER KILLER (Radioactive Cognitive Data Indonesia)
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in ALL copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# ATTRIBUTION: The name "Muhamad Fadhil Faturohman" and "RCDIDN V1.0"
# MUST remain visible in all copies, derivatives, and commercial products.
# ==============================================================================
"""
RCDIDN V1.0 - HACKER KILLER
Radioactive Cognitive Data Indonesia — Defensive Security System
Creator: Muhamad Fadhil Faturohman
38 FEATURES

Novel Contributions:
  - PHANTOM CLOCK  : LLM Dwell Time Measurement System      [NOVEL #1]
  - MINDPRINT      : Attacker Behavioral Profiling Engine   [NOVEL #2]
  - MIRAGE DROP    : Adaptive Canary Response System        [NOVEL #3]
  - TEMPORAL GRID  : Timing Manipulation Defense            [NOVEL #4]
  - DARK MIRROR    : Attacker Environment Reflection        [NOVEL #5]
  - ECONOMICS      : Attacker Cost Quantification           [NOVEL #6]
  - PHEROMONE      : Active Attacker Attraction System      [NOVEL #7]
  - GHOST NETWORK  : Single-Host Enterprise Simulation      [NOVEL #8]
  - REGULATORY     : Forensic-Grade Evidence Collection     [NOVEL #9]
  - HTML Threat Intelligence Report Generator
  - ASCII Threat Intelligence Dashboard
  - Built-in Self-Test Suite (6 unit tests)

Requirements:
  pip install cryptography
"""

import json
import os
import re
import time
import secrets
import hashlib
import subprocess
import platform
import base64
import random
import string
import sys
import socket
import threading
import urllib.request
import urllib.parse
import argparse
import pathlib
import zipfile
import getpass
import gc
import hmac
import ipaddress
import shutil
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

# ================= ANTI-DEBUGGING & SELF-DESTRUCT =================
# FIX: Tambahkan env flag RCDIDN_NO_DESTRUCT untuk mencegah self-destruct
# saat coverage run, pytest-cov, py-spy, atau profiler Python lain aktif.
# Juga saat CI/CD pipeline menjalankan --test dengan coverage.
if sys.gettrace() is not None and not os.environ.get("RCDIDN_NO_DESTRUCT"):
    print("[!] FATAL: Debugger detected. Initiating Self-Destruct Protocol...")
    print("[!] NOTE: Set RCDIDN_NO_DESTRUCT=1 to disable this for coverage/profiling.")
    try:
        with open(__file__, 'w') as f:
            f.write("# BOOM. RCDIDN SECURED.")
        os.remove(__file__)
    except Exception:
        pass
    sys.exit()

try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives import hashes
    from cryptography.exceptions import InvalidTag
except ImportError:
    print("[-] ERROR: Cryptography module not found. Run: pip install cryptography")
    sys.exit()

# ================= BANNER =================
def print_banner():
    print(r"""
    ██████╗  ██████╗ ██████╗ ██╗██████╗ ███╗   ██╗
    ██╔══██╗██╔════╝ ██╔══██╗██║██╔══██╗████╗  ██║
    ██████╔╝██║      ██║  ██║██║██║  ██║██╔██╗ ██║
    ██╔══██╗██║      ██║  ██║██║██║  ██║██║╚██╗██║
    ██║  ██║╚██████╗ ██████╔╝██║██████╔╝██║ ╚████║
    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚═════╝ ╚═╝  ╚═══╝
    === Radioactive Cognitive Data Indonesia ===
    [*] V1.0 — HACKER KILLER (38 FEATURES)
    [*] Creator: Muhamad Fadhil Faturohman
    [!] KEEP YOUR KEYS IN A SAFE PLACE
    [!] CHECK HOW TO USE THE TOOL IN THE README BEFORE YOU USE IT
    [+] RCDIDN: Turning the Hunted into the Hunter.
    """)

# ================= CONFIGURATION =================
VAULT_DIR     = os.path.join(str(Path.home()), ".rcdidn_vault")
SHADOW_DIR    = os.path.join(str(Path.home()), ".sys_meta_rcdidn")
SALT_FILE     = os.path.join(SHADOW_DIR, "sys_crypto_salt.bin")
MANIFEST_NAME = "core_system_map.bin"
HIDDEN_LOG        = os.path.join(SHADOW_DIR, "sys_kern_meta.log")
IPS_PID_FILE      = os.path.join(SHADOW_DIR, "rcdidn_ips.pid")
CANARY_LOG        = os.path.join(SHADOW_DIR, "canary_hits.log")
DWELL_LOG         = os.path.join(SHADOW_DIR, "phantom_clock.log")
EVIDENCE_DIR      = os.path.join(SHADOW_DIR, "legal_evidence")
# FIX: Log files terpisah per fitur agar sesuai dokumentasi README
DARK_MIRROR_LOG   = os.path.join(SHADOW_DIR, "dark_mirror.log")
ECONOMICS_LOG     = os.path.join(SHADOW_DIR, "economics.log")
PHEROMONE_LOG     = os.path.join(SHADOW_DIR, "pheromone.log")
GHOST_NETWORK_LOG = os.path.join(SHADOW_DIR, "ghost_network.log")

SENSITIVE_EXTS = [
    '.json', '.csv', '.sql', '.env', '.yaml', '.yml',
    '.config', '.ini', '.properties', '.toml', '.xml',
    '.pem', '.key', '.crt', '.p12', '.pfx'
]

MAX_FILE_SIZE = 50 * 1024 * 1024  # Limit 50MB anti-Memory Exhaustion

# In-memory geolocation cache to avoid duplicate API calls
_geo_cache: dict = {}
_temporal_profile = "random_chaos"  # default

# Security constants
MAX_GEO_CACHE        = 5000   # Batas entri cache GeoIP — anti memory leak
MAX_TARPIT_SECONDS   = 3600   # Batas sesi tarpit 1 jam — anti thread exhaustion
MAX_HONEYPOT_THREADS = 200    # Batas max thread concurrent per honeypot port

# Semaphore per port untuk batasi thread honeypot
_honeypot_semaphore: dict = {}

# ================= SYSTEM UTILS =================
def ensure_dirs():
    """Create vault and shadow directories if they do not exist."""
    for d in [VAULT_DIR, SHADOW_DIR, EVIDENCE_DIR]:
        try:
            os.makedirs(d, mode=0o700, exist_ok=True)
        except Exception as e:
            print(f"[-] Failed to create directory {d}: {e}")

def set_immutable(path: str, active: bool = True):
    """Lock or unlock a file at OS level."""
    if not os.path.exists(path) and active is False:
        return
    sys_os = platform.system()
    try:
        if sys_os == "Linux":
            subprocess.run(
                ["sudo", "chattr", "+i" if active else "-i", path],
                capture_output=True, timeout=5
            )
        elif sys_os == "Darwin":
            subprocess.run(
                ["chflags", "uchg" if active else "nouchg", path],
                capture_output=True, timeout=5
            )
        elif sys_os == "Windows":
            if active:
                subprocess.run(["attrib", "+r", "+s", "+h", path], capture_output=True)
                subprocess.run(["icacls", path, "/deny", "Everyone:(D,WD)"], capture_output=True)
            else:
                subprocess.run(["icacls", path, "/remove:d", "Everyone"], capture_output=True)
                subprocess.run(["attrib", "-r", "-s", "-h", path], capture_output=True)
    except Exception as e:
        log_event(
            f"[IMMUTABLE] Failed to {'lock' if active else 'unlock'} {path}: {e}",
            event_type="ERROR"
        )

def update_gitignore():
    """Append RCDIDN protection rules to .gitignore."""
    # FIX: Ganti *.bin dengan nama file spesifik RCDIDN saja
    # agar tidak mengabaikan file binary sah lain di project
    rules = [
        "\n# === RCDIDN Protection ===",
        ".rcdidn_vault/",
        ".sys_meta_rcdidn/",
        "sys_crypto_salt.bin",
        "core_system_map.bin",
        "rc_sentinel.html",
        "rc_ransom.html",
        "rcdidn_report_*.html",
        "rcdidn_web.log"
    ]
    gitignore = ".gitignore"
    try:
        existing = open(gitignore).read() if os.path.exists(gitignore) else ""
        with open(gitignore, "a") as f:
            for rule in rules:
                if rule.strip() not in existing:
                    f.write(rule + "\n")
        print("[+] .gitignore updated with RCDIDN protection rules.")
    except Exception as e:
        log_event(f"[GITIGNORE] Error: {e}", event_type="ERROR")

# ================= STRUCTURED JSON LOGGING =================
def log_event(message: str, event_type: str = "INFO", ip: str = None,
              port: int = None, tool: str = None, country: str = None):
    """Write a structured JSON log entry per line with automatic 5MB rotation."""
    ensure_dirs()
    entry = {
        "timestamp":     time.strftime('%Y-%m-%dT%H:%M:%S'),
        "event":         event_type,
        "message":       message,
        "ip":            ip,
        "port":          port,
        "tool_detected": tool,
        "country":       country,
        "hostname":      socket.gethostname(),
        "os":            platform.system()
    }
    entry = {k: v for k, v in entry.items() if v is not None}

    if not os.path.exists(HIDDEN_LOG):
        open(HIDDEN_LOG, 'w').close()

    try:
        with open(HIDDEN_LOG, 'a') as f:
            f.write(json.dumps(entry) + "\n")
        if os.path.getsize(HIDDEN_LOG) > 5 * 1024 * 1024:
            os.rename(HIDDEN_LOG, f"{HIDDEN_LOG}.{int(time.time())}.bak")
    except Exception:
        pass

def log_to_file(filepath: str, entry: dict):
    """Write JSON entry to a dedicated feature log file with 5MB rotation."""
    ensure_dirs()
    try:
        if not os.path.exists(filepath):
            open(filepath, 'w').close()
        with open(filepath, 'a') as f:
            f.write(json.dumps(entry) + "\n")
        if os.path.getsize(filepath) > 5 * 1024 * 1024:
            os.rename(filepath, f"{filepath}.{int(time.time())}.bak")
    except Exception:
        pass

def read_logs() -> list:
    entries = []
    if not os.path.exists(HIDDEN_LOG):
        return entries
    try:
        with open(HIDDEN_LOG, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        entries.append(json.loads(line))
                    except json.JSONDecodeError:
                        entries.append({"timestamp": "", "event": "LEGACY", "message": line})
    except Exception as e:
        log_event(f"[READ_LOGS] Error: {e}", event_type="ERROR")
    return entries

# ================= GEOLOCATION ENRICHMENT =================
def get_ip_geo(ip: str) -> dict:
    global _geo_cache
    if ip in _geo_cache:
        return _geo_cache[ip]

    default = {
        'country': 'Unknown', 'country_code': 'XX',
        'city': 'Unknown', 'isp': 'Unknown', 'asn': 'Unknown'
    }
    try:
        url = f"https://ipinfo.io/{ip}/json"
        req = urllib.request.Request(url, headers={'User-Agent': 'RCDIDN/1.0'})
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read())
            if 'ip' in data:
                result = {
                    'country':      data.get('country', 'Unknown'),
                    'country_code': data.get('country', 'XX'),
                    'city':         data.get('city', 'Unknown'),
                    'isp':          data.get('org', 'Unknown'),
                    'asn':          data.get('org', 'Unknown')
                }
                if len(_geo_cache) >= MAX_GEO_CACHE:
                    oldest_key = next(iter(_geo_cache))
                    del _geo_cache[oldest_key]
                _geo_cache[ip] = result
                return result
    except Exception as e:
        log_event(f"[GEO] Lookup failed for {ip}: {e}", event_type="ERROR")

    _geo_cache[ip] = default
    return default

# ================= HIVE-MIND WEBHOOK =================
# FIX: Implementasi HTTP webhook nyata. Set env RCDIDN_HIVE_URL untuk aktifkan.
def sync_hive_mind(ip: str, location: str, isp: str):
    """
    Sync attacker threat intel ke central aggregation server via HTTP POST.
    Set RCDIDN_HIVE_URL=https://your-server.com/api/hive untuk aktifkan.
    """
    hive_url = os.environ.get("RCDIDN_HIVE_URL", "").strip()
    entry = {
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S'),
        "ip":        ip,
        "location":  location,
        "isp":       isp,
        "source":    socket.gethostname(),
        "version":   "RCDIDN_V1.0"
    }
    log_event(f"[HIVE-MIND] Synced {ip} | {location} | {isp}", event_type="HIVE")

    if not hive_url:
        return  # Hive URL tidak dikonfigurasi, hanya log lokal

    def _post():
        try:
            payload = json.dumps(entry).encode('utf-8')
            req = urllib.request.Request(
                hive_url,
                data=payload,
                headers={
                    'Content-Type': 'application/json',
                    'User-Agent':   'RCDIDN-HiveMind/1.0',
                    'X-RCDIDN-Key': os.environ.get("RCDIDN_HIVE_SECRET", "")
                },
                method='POST'
            )
            with urllib.request.urlopen(req, timeout=5) as resp:
                log_event(
                    f"[HIVE-MIND] POST OK {resp.status} for {ip}",
                    event_type="HIVE"
                )
        except Exception as e:
            log_event(f"[HIVE-MIND] POST failed for {ip}: {e}", event_type="ERROR")

    threading.Thread(target=_post, daemon=True).start()

# ================= KEY MANAGEMENT & AES-256 ENCRYPTION =================
def derive_true_aes256_key(password: str, salt: bytes) -> bytes:
    """PBKDF2HMAC 600,000 Iterations — membunuh upaya brute-force GPU."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=salt, iterations=600_000
    )
    return kdf.derive(password.encode())

def get_or_create_key(force_new: bool = False) -> bytes:
    """Zero-Knowledge Storage: tidak menyimpan key di disk, hanya salt (32 bytes)."""
    ensure_dirs()
    if force_new or not os.path.exists(SALT_FILE):
        print("\n[!] INITIAL SETUP: Vault Authentication")
        print("[!] RCDIDN uses True AES-256-GCM. If you lose this password, data is PERMANENTLY GONE.")
        while True:
            pwd  = getpass.getpass("    Create Master Password: ")
            pwd2 = getpass.getpass("    Confirm Password: ")
            if pwd == pwd2 and len(pwd) >= 8:
                break
            print("    [-] Passwords do not match or too short (min 8 chars). Try again.\n")
        if os.path.exists(SALT_FILE):
            set_immutable(SALT_FILE, False)
        # FIX: Salt 32 bytes agar sesuai dokumentasi README Security Architecture
        salt = os.urandom(32)
        with open(SALT_FILE, 'wb') as f:
            f.write(salt)
        set_immutable(SALT_FILE, True)
    else:
        set_immutable(SALT_FILE, False)
        with open(SALT_FILE, 'rb') as f:
            salt = f.read()
        set_immutable(SALT_FILE, True)
        pwd = getpass.getpass("\n[?] Enter RCDIDN Master Password: ")
    return derive_true_aes256_key(pwd, salt)

def cmd_generate_key():
    print("[!] WARNING: A new password renders all previously encrypted files UNRECOVERABLE")
    print("    unless you decrypt them first.")
    confirm = input("    Continue? (y/N): ").strip().lower()
    if confirm == 'y':
        get_or_create_key(force_new=True)
    else:
        print("[*] Password rotation cancelled.")

def get_vault_filename(src_path: str, key: bytes) -> str:
    """HMAC Path Obfuscation — hacker tidak bisa tebak nama file asli via LFI."""
    h = hmac.new(key, src_path.encode(), digestmod=hashlib.sha256).hexdigest()
    return f"{h[:16]}.enc"

def encrypt_file(src_path: str, master_key: bytes) -> str:
    if os.path.getsize(src_path) > MAX_FILE_SIZE:
        raise MemoryError("File exceeds 50MB safety limit for RAM buffering.")
    with open(src_path, 'rb') as f:
        data = f.read()
    aesgcm = AESGCM(master_key)
    nonce  = os.urandom(12)
    ciphertext    = aesgcm.encrypt(nonce, data, None)
    vault_filename = get_vault_filename(src_path, master_key)
    vault_path     = os.path.join(VAULT_DIR, vault_filename)
    with open(vault_path, 'wb') as f:
        f.write(nonce + ciphertext)
    set_immutable(vault_path, True)
    return vault_path

def decrypt_file(vault_path: str, original_path: str, master_key: bytes):
    set_immutable(vault_path, False)
    with open(vault_path, 'rb') as f:
        encrypted = f.read()
    nonce      = encrypted[:12]
    ciphertext = encrypted[12:]
    aesgcm = AESGCM(master_key)
    data   = aesgcm.decrypt(nonce, ciphertext, None)
    os.makedirs(os.path.dirname(os.path.abspath(original_path)), exist_ok=True)
    with open(original_path, 'wb') as f:
        f.write(data)

# ================= MIRAGE DROP — ADAPTIVE CANARY SYSTEM =================
def generate_canary(original_path: str) -> str:
    ext = Path(original_path).suffix.lower()
    _upper_digits = string.ascii_uppercase + string.digits
    _all_chars    = string.ascii_letters + string.digits + "/+="
    fake_aws    = "AKIA" + ''.join(secrets.choice(_upper_digits) for _ in range(16))
    fake_secret = ''.join(secrets.choice(_all_chars) for _ in range(40))
    fake_db     = secrets.token_hex(12)
    fake_stripe = "sk_live_" + secrets.token_hex(24)
    fake_token  = secrets.token_hex(32)

    templates = {
        '.env': (
            f"# Application configuration\n"
            f"APP_KEY={secrets.token_hex(16)}\n"
            f"APP_ENV=production\n"
            f"DB_HOST=db.internal\nDB_PORT=5432\nDB_USER=app_user\n"
            f"DB_PASSWORD={fake_db}\n"
            f"AWS_ACCESS_KEY_ID={fake_aws}\n"
            f"AWS_SECRET_ACCESS_KEY={fake_secret}\n"
            f"STRIPE_SECRET_KEY={fake_stripe}\n"
            f"JWT_SECRET={fake_token}\n"
        ),
        '.json': (
            f'{{\n  "aws_access_key": "{fake_aws}",\n'
            f'  "aws_secret": "{fake_secret}",\n'
            f'  "db_password": "{fake_db}",\n'
            f'  "stripe_key": "{fake_stripe}",\n'
            f'  "api_token": "{fake_token}"\n}}\n'
        ),
        '.sql': (
            f"-- Database credentials dump\n"
            f"INSERT INTO users (username, password_hash, api_key) VALUES\n"
            f"  ('admin',  '{hashlib.sha256(fake_db.encode()).hexdigest()[:16]}', '{fake_token}'),\n"
            f"  ('deploy', '{hashlib.sha256(fake_secret.encode()).hexdigest()[:16]}', '{fake_aws}');\n"
        ),
        '.yaml': (
            f"database:\n  password: {fake_db}\n"
            f"aws:\n  access_key: {fake_aws}\n  secret: {fake_secret}\n"
            f"stripe:\n  key: {fake_stripe}\n"
        ),
    }
    return templates.get(
        ext,
        f"# Configuration\nSECRET_KEY={fake_token}\nDB_PASSWORD={fake_db}\nAPI_KEY={fake_aws}\n"
    )

def log_canary_hit(filepath: str, ip: str = "unknown"):
    ensure_dirs()
    entry = {
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S'),
        "event":     "CANARY_HIT",
        "file":      filepath,
        "ip":        ip,
        "canary_hash": (
            hashlib.sha256(open(filepath, 'rb').read()).hexdigest()[:16]
            if os.path.exists(filepath) else "N/A"
        )
    }
    try:
        if not os.path.exists(CANARY_LOG):
            open(CANARY_LOG, 'w').close()
        with open(CANARY_LOG, 'a') as f:
            f.write(json.dumps(entry) + "\n")
    except Exception as e:
        log_event(f"[CANARY] Log error: {e}", event_type="ERROR")

def show_canary_stats():
    if not os.path.exists(CANARY_LOG):
        print("[-] No canary hits recorded yet.")
        return
    hits = defaultdict(list)
    try:
        with open(CANARY_LOG) as f:
            for line in f:
                try:
                    e = json.loads(line.strip())
                    hits[e.get('file', 'unknown')].append(e)
                except Exception:
                    pass
    except Exception as e:
        print(f"[-] Error reading canary log: {e}")
        return

    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║          RCDIDN — MIRAGE DROP CANARY INTELLIGENCE        ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print(f"  {'File':<30} {'Hits':>5}  {'Last Hit':<20}  {'Last IP'}")
    print("  " + "-" * 65)
    for filepath, events in sorted(hits.items(), key=lambda x: -len(x[1])):
        last  = events[-1]
        fname = os.path.basename(filepath)
        print(f"  {fname:<30} {len(events):>5}  {last.get('timestamp','?'):<20}  {last.get('ip','?')}")
    total = sum(len(v) for v in hits.values())
    print(f"\n  Total canary hits : {total}")
    print("╚══════════════════════════════════════════════════════════╝\n")

# ================= ENCRYPTED SHADOW MANIFEST =================
def load_manifest(project_root: str, key: bytes) -> dict:
    manifest_path = os.path.join(project_root, MANIFEST_NAME)
    if os.path.exists(manifest_path):
        set_immutable(manifest_path, False)
        try:
            with open(manifest_path, 'rb') as f:
                encrypted = f.read()
            aesgcm = AESGCM(key)
            nonce  = encrypted[:12]
            data   = aesgcm.decrypt(nonce, encrypted[12:], None)
            set_immutable(manifest_path, True)
            try:
                return json.loads(data.decode('utf-8'))
            except (json.JSONDecodeError, UnicodeDecodeError) as e:
                log_event(f"[MANIFEST] Corrupt manifest detected: {e}", event_type="ERROR")
                backup = manifest_path + f".corrupt_{int(time.time())}"
                shutil.copy(manifest_path, backup)
                raise ValueError(f"Manifest corrupt — backup saved to {backup}")
        except InvalidTag:
            set_immutable(manifest_path, True)
            raise ValueError("Invalid Master Password")
        except Exception as e:
            log_event(f"[MANIFEST] Load error: {e}", event_type="ERROR")
    return {}

def save_manifest(project_root: str, manifest: dict, key: bytes):
    manifest_path = os.path.join(project_root, MANIFEST_NAME)
    set_immutable(manifest_path, False)
    try:
        data   = json.dumps(manifest).encode()
        aesgcm = AESGCM(key)
        nonce  = os.urandom(12)
        ciphertext = aesgcm.encrypt(nonce, data, None)
        with open(manifest_path, 'wb') as f:
            f.write(nonce + ciphertext)
        set_immutable(manifest_path, True)
    except Exception as e:
        log_event(f"[MANIFEST] Save error: {e}", event_type="ERROR")

# ================= CORE OPERATIONS =================
def secure_massal(project_root: str, master_key: bytes):
    ensure_dirs()
    try:
        manifest = load_manifest(project_root, master_key)
    except ValueError:
        sys.exit("[-] WRONG PASSWORD. Aborting.")

    found = 0
    print(f"\n[*] Scanning: {project_root}")
    for root, dirs, files in os.walk(project_root):
        dirs[:] = [d for d in dirs if os.path.join(root, d) not in [VAULT_DIR, SHADOW_DIR]]
        for fname in files:
            fpath = os.path.join(root, fname)
            ext   = Path(fname).suffix.lower()
            if ext not in SENSITIVE_EXTS or fpath in manifest:
                continue
            print(f"  [+] Securing: {fpath}")
            try:
                vault_path = encrypt_file(fpath, master_key)
                canary     = generate_canary(fpath)
                with open(fpath, 'w') as f:
                    f.write(canary)
                manifest[fpath] = vault_path
                found += 1
                log_event(f"Vaulted: {fpath}", event_type="VAULT")
            except Exception as e:
                print(f"  [-] Failed: {fpath}: {e}")
                log_event(f"[VAULT] Error on {fpath}: {e}", event_type="ERROR")
    save_manifest(project_root, manifest, master_key)
    update_gitignore()
    inject_sentinel("index.php")
    log_event(f"[RUN] Secured {found} files in {project_root}", event_type="RUN")
    del master_key
    gc.collect()
    print(f"\n[+] Done. {found} file(s) vaulted. Canaries deployed.")
    print(f"\n{'=' * 57}")
    print(f"[!] BACKUP REMINDER  : {VAULT_DIR}")
    print(f"[!] Losing this directory means ALL encrypted files are UNRECOVERABLE.")
    print(f"{'=' * 57}\n")

def restart_lock(project_root: str, master_key: bytes):
    try:
        manifest = load_manifest(project_root, master_key)
    except ValueError:
        sys.exit("[-] WRONG PASSWORD. Aborting.")

    if not manifest:
        print("[-] No manifest found. Run 'run' first.")
        return
    count = 0
    for original_path, vault_path in manifest.items():
        if os.path.exists(original_path):
            try:
                new_vault = encrypt_file(original_path, master_key)
                canary    = generate_canary(original_path)
                with open(original_path, 'w') as f:
                    f.write(canary)
                manifest[original_path] = new_vault
                print(f"  [+] Re-locked: {original_path}")
                count += 1
            except Exception as e:
                print(f"  [-] Failed: {original_path}: {e}")
                log_event(f"[RESTART] Error {original_path}: {e}", event_type="ERROR")
    save_manifest(project_root, manifest, master_key)
    log_event(f"[RESTART] Re-locked {count} files", event_type="RESTART")
    del master_key
    gc.collect()
    print(f"\n[+] Restart complete. {count} file(s) re-locked.")

def restore_files(project_root: str, master_key: bytes):
    try:
        manifest = load_manifest(project_root, master_key)
    except ValueError:
        sys.exit("\n[!] WRONG PASSWORD OR CORRUPT DATA. Access Denied.")

    if not manifest:
        print("[-] No manifest found. Nothing to restore.")
        return
    restored = 0
    for original_path, vault_path in list(manifest.items()):
        if not os.path.exists(vault_path):
            print(f"  [-] Vault file missing: {vault_path}")
            continue
        try:
            decrypt_file(vault_path, original_path, master_key)
            set_immutable(vault_path, False)
            os.remove(vault_path)
            del manifest[original_path]
            print(f"  [+] Restored: {original_path}")
            restored += 1
        except InvalidTag:
            print(f"\n[!] WRONG PASSWORD OR CORRUPT DATA: Master password does not match.")
            log_event("[RESTORE] Failed: InvalidTag — wrong master key", event_type="ERROR")
            return
        except Exception as e:
            print(f"  [-] Failed to restore {original_path}: {e}")
            log_event(f"[RESTORE] Error {original_path}: {e}", event_type="ERROR")
    if manifest:
        save_manifest(project_root, manifest, master_key)
    else:
        manifest_path = os.path.join(project_root, MANIFEST_NAME)
        if os.path.exists(manifest_path):
            set_immutable(manifest_path, False)
            os.remove(manifest_path)
    log_event(f"[RESTORE] Restored {restored} files", event_type="RESTORE")
    del master_key
    gc.collect()
    print(f"\n[+] Restore complete. {restored} file(s) recovered.")

# ================= NOVEL #4: TEMPORAL DECEPTION GRID =================
# FIX: Implementasi semua profil yang didokumentasikan.
# Profil tersedia: off, random_chaos, busy_server, flapping, degrading, recovering, tarpit_extreme
def temporal_deception_delay():
    """NOVEL #4: TEMPORAL DECEPTION GRID — manipulasi timing untuk hancurkan model mental scanner."""
    global _temporal_profile
    p = _temporal_profile

    if p == "off":
        return

    elif p == "random_chaos":
        # Fully random — scanner tidak bisa membangun baseline apapun
        time.sleep(random.uniform(0.05, 5.0))

    elif p == "busy_server":
        # Konsisten lambat — menyerupai server production under load
        time.sleep(random.uniform(2.0, 4.5))

    elif p == "flapping":
        # FIX: Implementasi baru — bergantian cepat dan lambat tanpa pola
        # Menyerupai server dengan network flapping / load spike
        if random.random() < 0.4:
            time.sleep(random.uniform(0.01, 0.1))   # spike cepat
        else:
            time.sleep(random.uniform(3.0, 8.0))    # drop lambat

    elif p == "degrading":
        # FIX: Implementasi baru — semakin lama semakin lambat (simulated degradation)
        # Menggunakan waktu sejak epoch sebagai basis agar delay bertambah secara global
        base = (time.time() % 3600) / 3600  # 0.0–1.0 dalam satu jam
        delay = 0.5 + base * 9.5            # 0.5s hingga 10s seiring waktu
        time.sleep(delay + random.uniform(-0.2, 0.2))

    elif p == "recovering":
        # FIX: Implementasi baru — lambat di awal, semakin cepat (server pulih dari overload)
        base  = (time.time() % 3600) / 3600
        delay = 10.0 - base * 9.0           # 10s menurun ke 1s seiring waktu
        time.sleep(max(0.1, delay + random.uniform(-0.3, 0.3)))

    elif p == "tarpit_extreme":
        # Delay sangat panjang untuk menjebak attacker secara maksimal
        time.sleep(random.uniform(10.0, 30.0))

def cmd_temporal(cmd: str):
    global _temporal_profile
    parts = cmd.split()
    valid_profiles = ["off", "random_chaos", "busy_server", "flapping", "degrading", "recovering", "tarpit_extreme"]

    if len(parts) == 1:
        print(f"\n[+] Current Temporal Profile: {_temporal_profile.upper()}")
        print(f"  Available profiles: {' | '.join(valid_profiles)}")
        print("  Usage: temporal profile <name>\n")
        return
    if len(parts) == 3 and parts[1] == "profile":
        if parts[2] in valid_profiles:
            _temporal_profile = parts[2]
            print(f"[+] Temporal Deception Grid set to: {_temporal_profile.upper()}")
            log_event(f"Temporal profile changed to {_temporal_profile}", event_type="SYSTEM")
        else:
            print(f"[-] Unknown profile. Available: {' | '.join(valid_profiles)}")

# ================= NOVEL #5: DARK MIRROR =================
# FIX: Implementasi deteksi OS/tool attacker dari initial packet, lalu sajikan
# environment yang familiar untuk meningkatkan engagement dan rasa disorientasi.

# Signature detection patterns
_TOOL_SIGNATURES = {
    b'masscan':      'masscan',
    b'nmap':         'nmap',
    b'zgrab':        'zgrab',
    b'shodan':       'shodan',
    b'censys':       'censys',
    b'sqlmap':       'sqlmap',
    b'gobuster':     'gobuster',
    b'dirb':         'dirb',
    b'nikto':        'nikto',
    b'curl':         'curl',
    b'wget':         'wget',
    b'python':       'python-requests',
    b'Go-http':      'golang-http',
    b'libwww':       'libwww-perl',
    b'Hydra':        'hydra',
    b'Medusa':       'medusa',
}

_OS_SIGNATURES = {
    b'Windows':    'Windows',
    b'Win32':      'Windows',
    b'Linux':      'Linux',
    b'Ubuntu':     'Ubuntu-Linux',
    b'Kali':       'Kali-Linux',
    b'Debian':     'Debian-Linux',
    b'Darwin':     'macOS',
    b'iPhone':     'iOS',
    b'Android':    'Android',
}

# Fake terminal environments tailored per detected OS
# NOTE: callable values are invoked at use-time so dynamic fields (timestamps)
# are evaluated lazily instead of at module-parse time.
_MIRROR_ENVS = {
    'Kali-Linux': (
        b"\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x80(root\xe2\x98\x89kali)-[~]\n\xe2\x94\x94\xe2\x94\x80$ "
    ),
    'Ubuntu-Linux': (
        b"root@ubuntu-prod:~$ "
    ),
    'Windows': (
        b"Microsoft Windows [Version 10.0.19045.3803]\r\n"
        b"(c) Microsoft Corporation. All rights reserved.\r\n\r\n"
        b"C:\\Users\\Administrator> "
    ),
    'macOS': lambda: (
        b"Last login: " + time.strftime('%a %b %d %H:%M:%S').encode() + b" on ttys001\r\n"
        b"MacBook-Pro:~ root$ "
    ),
    'default': (
        b"Ubuntu 22.04.3 LTS \xe2\x80\x94 Welcome\r\nroot@prod-server:~$ "
    ),
}

def _detect_attacker_profile(data: bytes) -> dict:
    """Analisis initial packet untuk mendeteksi OS dan tool attacker."""
    detected_tool = 'unknown'
    detected_os   = 'default'

    for sig, name in _TOOL_SIGNATURES.items():
        if sig.lower() in data.lower():
            detected_tool = name
            break

    for sig, name in _OS_SIGNATURES.items():
        if sig in data:
            detected_os = name
            break

    return {'tool': detected_tool, 'os': detected_os}

def _dark_mirror_handler(conn: socket.socket, addr):
    """Per-connection Dark Mirror handler dengan OS fingerprinting."""
    attacker_ip = addr[0]
    try:
        conn.settimeout(30)
        data = conn.recv(2048)
        if not data:
            return

        # Deteksi profil attacker dari initial packet
        profile = _detect_attacker_profile(data)
        detected_tool = profile['tool']
        detected_os   = profile['os']

        # Sajikan environment yang familiar
        mirror_prompt = _MIRROR_ENVS.get(detected_os, _MIRROR_ENVS['default'])
        if callable(mirror_prompt):
            mirror_prompt = mirror_prompt()

        # Reflect payload balik + tambahkan prompt lingkungan yang familiar
        conn.send(mirror_prompt)
        temporal_deception_delay()

        # Log ke dark_mirror.log terpisah
        entry = {
            "timestamp":    time.strftime('%Y-%m-%dT%H:%M:%S'),
            "event":        "DARK_MIRROR",
            "ip":           attacker_ip,
            "detected_os":  detected_os,
            "detected_tool": detected_tool,
            "payload_len":  len(data),
            "payload_hex":  data[:64].hex()
        }
        log_to_file(DARK_MIRROR_LOG, entry)
        log_event(
            f"Dark Mirror: {attacker_ip} → OS:{detected_os} Tool:{detected_tool}",
            event_type="DARK_MIRROR", ip=attacker_ip
        )

        # Lanjutkan sesi — kirim fake responses
        while True:
            try:
                conn.settimeout(60)
                cmd_data = conn.recv(1024)
                if not cmd_data:
                    break
                cmd = cmd_data.decode('utf-8', errors='ignore').strip()
                if not cmd:
                    conn.send(mirror_prompt)
                    continue

                # Generate fake response sesuai OS
                if detected_os == 'Windows':
                    fake_resp = (
                        f"'{cmd}' is not recognized as an internal or external command,\r\n"
                        f"operable program or batch file.\r\n\r\nC:\\Users\\Administrator> "
                    ).encode()
                else:
                    fake_resp = (
                        f"{cmd}: command not found\n"
                        f"bash: {cmd}: No such file or directory\n"
                    ).encode() + mirror_prompt

                conn.send(fake_resp)

            except socket.timeout:
                break
    except Exception:
        pass
    finally:
        conn.close()

def start_dark_mirror(port=8080):
    """NOVEL #5: DARK MIRROR — sajikan lingkungan familiar sesuai OS attacker."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', port))
        s.listen(10)
        print(f"  [+] Dark Mirror active on port {port}. Profiling attacker OS/tools...")
        while True:
            try:
                conn, addr = s.accept()
                threading.Thread(
                    target=_dark_mirror_handler,
                    args=(conn, addr),
                    daemon=True
                ).start()
            except Exception as e:
                log_event(f"[DARK_MIRROR] Accept error: {e}", event_type="ERROR")
    except Exception as e:
        print(f"[-] Dark Mirror failed: {e}")

def cmd_mirror():
    print("[*] Launching Dark Mirror in background (Port 8080)...")
    print("[*] Dark Mirror will detect attacker OS and present a familiar environment.")
    threading.Thread(target=start_dark_mirror, daemon=True).start()

def show_dark_mirror_stats():
    """Tampilkan statistik Dark Mirror dari log terpisah."""
    if not os.path.exists(DARK_MIRROR_LOG):
        print("[-] No Dark Mirror data yet. Run 'mirror' then 'ips start'.")
        return
    sessions = []
    try:
        with open(DARK_MIRROR_LOG) as f:
            for line in f:
                try:
                    sessions.append(json.loads(line.strip()))
                except Exception:
                    pass
    except Exception:
        pass

    if not sessions:
        print("[-] No Dark Mirror sessions recorded yet.")
        return

    os_freq   = defaultdict(int)
    tool_freq = defaultdict(int)
    for s in sessions:
        os_freq[s.get('detected_os', 'unknown')]     += 1
        tool_freq[s.get('detected_tool', 'unknown')] += 1

    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║        RCDIDN — DARK MIRROR ATTACKER PROFILES            ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print(f"  Total Dark Mirror Sessions : {len(sessions)}")
    print("  TOP DETECTED OS:")
    for os_name, cnt in sorted(os_freq.items(), key=lambda x: -x[1])[:5]:
        print(f"    {os_name:<20} : {cnt}")
    print("  TOP DETECTED TOOLS:")
    for tool, cnt in sorted(tool_freq.items(), key=lambda x: -x[1])[:5]:
        print(f"    {tool:<20} : {cnt}")
    print("╚══════════════════════════════════════════════════════════╝\n")

# ================= NOVEL #6: HONEYPOT ECONOMICS =================
def show_economics():
    """NOVEL #6: HONEYPOT ECONOMICS — kalkulasi kerugian finansial attacker."""
    if not os.path.exists(DWELL_LOG):
        print("[-] No dwell data to calculate economics.")
        return
    total_sec = 0
    sessions  = 0
    try:
        with open(DWELL_LOG) as f:
            for line in f:
                try:
                    e = json.loads(line.strip())
                    total_sec += e.get('session_duration_seconds', 0)
                    sessions  += 1
                except Exception:
                    pass
    except Exception:
        pass

    hours = total_sec / 3600
    cost  = hours * 50.0  # $50/hour attacker operational cost baseline

    # Log ke economics.log terpisah
    econ_entry = {
        "timestamp":       time.strftime('%Y-%m-%dT%H:%M:%S'),
        "event":           "ECONOMICS_CALC",
        "total_sessions":  sessions,
        "total_hours":     round(hours, 4),
        "estimated_cost_usd": round(cost, 2)
    }
    log_to_file(ECONOMICS_LOG, econ_entry)

    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║           RCDIDN — HONEYPOT ECONOMICS (DAMAGE)           ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print(f"  Total Attacker Sessions Trapped : {sessions}")
    print(f"  Total Attacker Time Wasted      : {hours:.2f} Hours")
    print(f"  Estimated Financial Damage      : ${cost:.2f} USD")
    print(f"  (Based on $50/hour attacker operational cost baseline)")
    print("╚══════════════════════════════════════════════════════════╝\n")

# ================= NOVEL #7: DIGITAL PHEROMONE =================
def deploy_pheromones(target: str = "all"):
    """NOVEL #7: DIGITAL PHEROMONE — deploy bait files untuk tarik attacker traffic."""
    # FIX: ZIP content sekarang bytes literal langsung, bukan string encode
    all_baits = {
        "exposed_env": {
            "robots.txt": (
                "User-agent: *\n"
                "Disallow: /.env\n"
                "Disallow: /admin_panel\n"
                "Disallow: /backup_2024_prod.zip\n"
                "Disallow: /config/database.yml\n"
            )
        },
        "fake_admin": {
            "info.php": (
                "<?php echo 'FATAL: Cannot connect to local database using root:root @ 127.0.0.1:3306'; ?>"
            )
        },
        "git_exposed": {
            "README_INTERNAL.txt": (
                "Server migration complete.\n"
                "Backup is at /backup_2024_prod.zip\n"
                "Git repo is at /.git — DO NOT EXPOSE\n"
            )
        },
        "phpinfo_bait": {
            "phpinfo.php": (
                "<?php phpinfo(); ?>"
            )
        },
        "backup_bait": {
            "backup_2024_prod.zip": None  # Binary — handled separately
        },
    }

    # Pilih target bait
    if target == "all":
        selected = {k: v for group in all_baits.values() for k, v in group.items()}
        selected["backup_2024_prod.zip"] = None
    elif target in all_baits:
        selected = all_baits[target]
    else:
        print(f"[-] Unknown pheromone target: {target}")
        print(f"    Available: all, {', '.join(all_baits.keys())}")
        return

    count = 0
    for fname, content in selected.items():
        if not os.path.exists(fname):
            if content is None:
                # FIX: ZIP bytes — tulis bytes literal langsung, bukan encode string
                with open(fname, "wb") as f:
                    f.write(b"PK\x05\x06" + b"\x00" * 18 + b"\x00\x00")
            else:
                with open(fname, "w") as f:
                    f.write(content)
            count += 1
            # Log ke pheromone.log terpisah
            ph_entry = {
                "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S'),
                "event":     "PHEROMONE_DEPLOYED",
                "file":      fname,
                "bait_type": target
            }
            log_to_file(PHEROMONE_LOG, ph_entry)
            log_event(f"Pheromone deployed: {fname}", event_type="PHEROMONE")
    print(f"[+] Deployed {count} Digital Pheromone bait file(s).")

def show_pheromone_stats():
    """Tampilkan statistik Digital Pheromone dari log terpisah."""
    if not os.path.exists(PHEROMONE_LOG):
        print("[-] No pheromone data yet.")
        return
    entries = []
    try:
        with open(PHEROMONE_LOG) as f:
            for line in f:
                try:
                    entries.append(json.loads(line.strip()))
                except Exception:
                    pass
    except Exception:
        pass
    deployed = [e for e in entries if e.get('event') == 'PHEROMONE_DEPLOYED']
    hits     = [e for e in entries if e.get('event') == 'PHEROMONE_HIT']
    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║         RCDIDN — DIGITAL PHEROMONE STATUS                ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print(f"  Bait Files Deployed : {len(deployed)}")
    print(f"  Total Bait Hits     : {len(hits)}")
    for e in deployed:
        hit_count = sum(1 for h in hits if h.get('file') == e.get('file'))
        print(f"    {e.get('file','?'):<35} hits: {hit_count}")
    print("╚══════════════════════════════════════════════════════════╝\n")

def cmd_pheromone(cmd: str):
    parts = cmd.split()
    if "deploy" in cmd:
        target = parts[2] if len(parts) >= 3 else "all"
        deploy_pheromones(target)
    elif "stats" in cmd:
        show_pheromone_stats()
    else:
        print("  Usage: pheromone deploy [all|exposed_env|fake_admin|git_exposed|phpinfo_bait|backup_bait]")
        print("         pheromone stats")

# ================= NOVEL #8: GHOST NETWORK =================
# FIX: Implementasi multi-host simulation nyata.
# Setiap koneksi mendapat "host" berbeda dengan banner dan respons unik.

_GHOST_HOSTS = [
    {
        "name":    "DC-01",
        "os":      "Windows Server 2019",
        "role":    "Domain Controller",
        "banner":  b"220 DC-01.corp.internal ESMTP Microsoft Exchange\r\n",
        "prompt":  b"C:\\Windows\\System32> ",
    },
    {
        "name":    "DB-PROD-01",
        "os":      "Ubuntu 20.04 LTS",
        "role":    "Production Database",
        "banner":  b"5.7.39-log MySQL Community Server\r\n",
        "prompt":  b"mysql> ",
    },
    {
        "name":    "WEB-FRONT-01",
        "os":      "Debian 11",
        "role":    "Web Frontend",
        "banner":  b"Apache/2.4.54 (Debian) OpenSSL/1.1.1n PHP/8.1.12\r\n",
        "prompt":  b"root@web-front-01:~$ ",
    },
    {
        "name":    "BACKUP-SRV",
        "os":      "CentOS 7",
        "role":    "Backup Server",
        "banner":  b"SSH-2.0-OpenSSH_7.4\r\n",
        "prompt":  b"[root@backup-srv ~]$ ",
    },
    {
        "name":    "MONITORING",
        "os":      "Ubuntu 22.04 LTS",
        "role":    "Monitoring / Grafana",
        "banner":  b"HTTP/1.1 200 OK\r\nServer: Grafana/9.3.2\r\n\r\n",
        "prompt":  b"root@monitoring:~$ ",
    },
    {
        "name":    "DEVOPS-01",
        "os":      "Ubuntu 22.04 LTS",
        "role":    "CI/CD Jenkins",
        "banner":  b"HTTP/1.1 200 OK\r\nServer: Jetty(9.4.z-SNAPSHOT)\r\nX-Hudson: 1.395\r\n\r\n",
        "prompt":  b"jenkins@devops-01:~$ ",
    },
    {
        "name":    "FILESERVER",
        "os":      "Windows Server 2016",
        "role":    "File Server / SMB",
        "banner":  b"\x00\x00\x00\x85\xffSMB",  # SMB signature bytes
        "prompt":  b"C:\\FileShare> ",
    },
    {
        "name":    "MAIL-01",
        "os":      "Ubuntu 18.04 LTS",
        "role":    "Mail Server / Postfix",
        "banner":  b"220 mail.corp.internal ESMTP Postfix (Ubuntu)\r\n",
        "prompt":  b"root@mail-01:~$ ",
    },
    {
        "name":    "REDIS-CACHE",
        "os":      "Alpine Linux 3.17",
        "role":    "Redis Cache",
        "banner":  b"+PONG\r\n",
        "prompt":  b"127.0.0.1:6379> ",
    },
    {
        "name":    "LDAP-AUTH",
        "os":      "Debian 10",
        "role":    "LDAP / OpenLDAP",
        "banner":  b"0\x0c\x02\x01\x01a\x07\x0a\x01\x00\x04\x00\x04\x00",  # LDAP BindResponse
        "prompt":  b"ldap> ",
    },
]

# Counter untuk rotasi host agar setiap koneksi mendapat host berbeda
_ghost_host_counter = 0
_ghost_host_lock    = threading.Lock()

def _ghost_network_handler(conn: socket.socket, addr, port: int):
    """
    NOVEL #8: GHOST NETWORK — handler per-koneksi yang mensimulasikan
    satu dari 10 fake enterprise hosts secara round-robin.
    """
    global _ghost_host_counter
    attacker_ip = addr[0]

    try:
        conn.settimeout(120)
        temporal_deception_delay()

        # Pilih host fake secara round-robin
        with _ghost_host_lock:
            host = _GHOST_HOSTS[_ghost_host_counter % len(_GHOST_HOSTS)]
            _ghost_host_counter += 1

        # Kirim banner host
        conn.send(host["banner"])

        # Log ke ghost_network.log terpisah
        gn_entry = {
            "timestamp":   time.strftime('%Y-%m-%dT%H:%M:%S'),
            "event":       "GHOSTNET_HIT",
            "ip":          attacker_ip,
            "port":        port,
            "fake_host":   host["name"],
            "fake_os":     host["os"],
            "fake_role":   host["role"],
        }
        log_to_file(GHOST_NETWORK_LOG, gn_entry)
        log_event(
            f"Ghost Network: {attacker_ip} → {host['name']} ({host['role']})",
            event_type="GHOSTNET", ip=attacker_ip, port=port
        )

        # Lanjutkan fake interactive session
        while True:
            try:
                conn.settimeout(60)
                data = conn.recv(1024)
                if not data:
                    break
                cmd = data.decode('utf-8', errors='ignore').strip()
                if not cmd:
                    conn.send(host["prompt"])
                    continue

                # Fake responses sesuai role host
                temporal_deception_delay()
                if host["role"] == "Production Database":
                    resp = f"ERROR 1045 (28000): Access denied for user 'root'@'{attacker_ip}'\n".encode()
                elif host["role"] == "Redis Cache":
                    resp = b"-ERR unknown command\r\n"
                elif "Windows" in host["os"]:
                    resp = f"Access is denied.\r\n\r\n{host['prompt'].decode()}".encode()
                else:
                    resp = f"{cmd}: Permission denied\n{host['prompt'].decode()}".encode()

                conn.send(resp)

            except socket.timeout:
                break

    except Exception:
        pass
    finally:
        conn.close()

def start_ghost_network(port=4444):
    """NOVEL #8: GHOST NETWORK — satu host fisik mensimulasikan 10 fake enterprise hosts."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', port))
        s.listen(10)
        print(f"  [+] Ghost Network active on port {port} — simulating {len(_GHOST_HOSTS)} fake enterprise hosts")
        print(f"      Hosts: {', '.join(h['name'] for h in _GHOST_HOSTS[:5])} +{len(_GHOST_HOSTS)-5} more")
        while True:
            try:
                conn, addr = s.accept()
                threading.Thread(
                    target=_ghost_network_handler,
                    args=(conn, addr, port),
                    daemon=True
                ).start()
            except Exception as e:
                log_event(f"[GHOSTNET] Accept error: {e}", event_type="ERROR")
    except Exception as e:
        print(f"[-] Ghost Network failed: {e}")

def cmd_ghostnet():
    print("[*] Launching Ghost Network in background (Port 4444)...")
    print(f"[*] Simulating {len(_GHOST_HOSTS)} fake enterprise hosts via round-robin distribution.")
    threading.Thread(target=start_ghost_network, daemon=True).start()

def show_ghost_network_stats():
    """Tampilkan statistik Ghost Network dari log terpisah."""
    if not os.path.exists(GHOST_NETWORK_LOG):
        print("[-] No Ghost Network data yet. Start IPS and wait for scans.")
        return
    sessions = []
    try:
        with open(GHOST_NETWORK_LOG) as f:
            for line in f:
                try:
                    sessions.append(json.loads(line.strip()))
                except Exception:
                    pass
    except Exception:
        pass

    if not sessions:
        print("[-] No Ghost Network sessions recorded yet.")
        return

    host_freq = defaultdict(int)
    for s in sessions:
        host_freq[s.get('fake_host', 'unknown')] += 1

    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║         RCDIDN — GHOST NETWORK TOPOLOGY STATS            ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print(f"  Total Pivot Attempts : {len(sessions)}")
    print("  Hits per Fake Host:")
    for host_name, cnt in sorted(host_freq.items(), key=lambda x: -x[1]):
        role = next((h['role'] for h in _GHOST_HOSTS if h['name'] == host_name), '?')
        print(f"    {host_name:<15} ({role:<25}) : {cnt}")
    print("╚══════════════════════════════════════════════════════════╝\n")

# ================= NOVEL #9: REGULATORY TRAP =================
def collect_evidence(target_name: str):
    """NOVEL #9: REGULATORY TRAP — generate forensic-grade evidence bundle."""
    ensure_dirs()
    stamp       = time.strftime('%Y%m%d_%H%M%S')
    report_name = os.path.join(EVIDENCE_DIR, f"Evidence_Report_{target_name}_{stamp}.txt")
    zip_name    = os.path.join(EVIDENCE_DIR, f"Evidence_Bundle_{target_name}_{stamp}.zip")

    # Hitung SHA-256 dari semua log file untuk chain of custody
    chain = {}
    log_files = [HIDDEN_LOG, DWELL_LOG, CANARY_LOG, DARK_MIRROR_LOG, PHEROMONE_LOG, GHOST_NETWORK_LOG]
    for lf in log_files:
        if os.path.exists(lf):
            with open(lf, 'rb') as f:
                chain[os.path.basename(lf)] = hashlib.sha256(f.read()).hexdigest()

    with open(report_name, "w") as f:
        f.write("=== RCDIDN REGULATORY EVIDENCE REPORT ===\n")
        f.write(f"Target/Authority : {target_name}\n")
        f.write(f"Generated        : {stamp}\n")
        f.write(f"Host             : {socket.gethostname()}\n")
        f.write(f"Creator          : RCDIDN V1.0 — Muhamad Fadhil Faturohman\n\n")
        f.write("=== SHA-256 CHAIN OF CUSTODY ===\n")
        for fname, sha in chain.items():
            f.write(f"  {sha}  {fname}\n")
        f.write("\n=== CONTENTS ===\n")
        f.write("This bundle contains raw JSON logs, phantom clock metrics,\n")
        f.write("canary hit records, dark mirror sessions, pheromone hits,\n")
        f.write("and ghost network pivot attempts with cryptographic integrity proofs.\n")

    zip_password      = secrets.token_hex(16)
    zip_password_file = zip_name + ".password.txt"
    with open(zip_password_file, 'w') as pf:
        pf.write(f"Evidence Bundle Password: {zip_password}\n")
        pf.write(f"Bundle: {os.path.basename(zip_name)}\n")
        pf.write(f"Generated: {stamp}\n")
        pf.write("IMPORTANT: Store this file securely. Required to open the bundle.\n")
    os.chmod(zip_password_file, 0o600)

    with zipfile.ZipFile(zip_name, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for z in log_files + [report_name]:
            if os.path.exists(z):
                zf.write(z, os.path.basename(z))
    os.chmod(zip_name, 0o600)

    print(f"[+] Regulatory Trap evidence bundle created for: {target_name}")
    print(f"  [+] Report   : {report_name}")
    print(f"  [+] Bundle   : {zip_name}")
    print(f"  [+] Password : {zip_password_file}  ← Simpan file ini dengan aman!")
    print(f"  [!] Bundle dan password file: chmod 600 (hanya owner)")
    log_event(f"Evidence bundle created for {target_name}", event_type="EVIDENCE")

def cmd_evidence(cmd: str):
    parts = cmd.split()
    if len(parts) >= 2 and parts[1] == "collect":
        collect_evidence("ALL_EVIDENCE")
    elif len(parts) >= 3 and parts[1] == "report":
        target = "_".join(parts[2:])
        collect_evidence(target)
    else:
        print("  Usage: evidence collect")
        print("         evidence report idcert|bssid|interpol|generic")

# ================= LLM AI INTERROGATOR (MULTI-PROVIDER) =================
MAX_AI_CALLS_PER_SESSION = 100  # Hard limit per session untuk cegah abuse biaya API

def call_llm_interrogator(prompt: str) -> str:
    api_key  = os.environ.get("RCDIDN_AI_KEY", "").strip()
    provider = os.environ.get("RCDIDN_AI_PROVIDER", "gemini").strip().lower()

    if not api_key:
        return "bash: command not found or disk I/O error."

    system_prompt = (
        "You are a broken, vulnerable Linux honeypot server. "
        "Act like a damaged terminal. Give convincing but completely fake outputs. "
        "Claim hardware corruption, disk errors, or kernel panics to waste their time. "
        "Maximum 2 lines. Never reveal you are an AI."
    )
    user_prompt = f"Hacker typed: {prompt[:500]}. Reply as the terminal."

    try:
        if provider == "openai":
            url     = "https://api.openai.com/v1/chat/completions"
            headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {api_key}'}
            payload = {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user",   "content": user_prompt}
                ],
                "max_tokens": 100
            }
            req = urllib.request.Request(
                url, data=json.dumps(payload).encode('utf-8'),
                headers=headers, method='POST'
            )
            with urllib.request.urlopen(req, timeout=5) as resp:
                return json.loads(resp.read())['choices'][0]['message']['content'].strip()

        elif provider == "anthropic":
            url     = "https://api.anthropic.com/v1/messages"
            headers = {
                'x-api-key':         api_key,
                'anthropic-version': '2023-06-01',
                'content-type':      'application/json'
            }
            payload = {
                "model":      "claude-haiku-4-5-20251001",
                "system":     system_prompt,
                "messages":   [{"role": "user", "content": user_prompt}],
                "max_tokens": 100
            }
            req = urllib.request.Request(
                url, data=json.dumps(payload).encode('utf-8'),
                headers=headers, method='POST'
            )
            with urllib.request.urlopen(req, timeout=5) as resp:
                return json.loads(resp.read())['content'][0]['text'].strip()

        elif provider == "deepseek":
            url     = "https://api.deepseek.com/chat/completions"
            headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {api_key}'}
            payload = {
                "model": "deepseek-chat",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user",   "content": user_prompt}
                ],
                "max_tokens": 100
            }
            req = urllib.request.Request(
                url, data=json.dumps(payload).encode('utf-8'),
                headers=headers, method='POST'
            )
            with urllib.request.urlopen(req, timeout=5) as resp:
                return json.loads(resp.read())['choices'][0]['message']['content'].strip()

        else:  # Default: Gemini
            url     = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
            headers = {'Content-Type': 'application/json', 'x-goog-api-key': api_key}
            payload = {
                "contents":          [{"parts": [{"text": user_prompt}]}],
                "systemInstruction": {"parts": [{"text": system_prompt}]}
            }
            req = urllib.request.Request(
                url, data=json.dumps(payload).encode('utf-8'),
                headers=headers, method='POST'
            )
            with urllib.request.urlopen(req, timeout=5) as resp:
                return json.loads(resp.read())['candidates'][0]['content']['parts'][0]['text'].strip()

    except Exception:
        return "Segmentation fault (core dumped)"

# ================= NOVEL #1: PHANTOM CLOCK — LLM DWELL TIME MEASUREMENT =================
def log_dwell_session(ip: str, port: int, duration_sec: float, commands: list, honeypot_type: str):
    ensure_dirs()
    engagement_score = min(100, int((duration_sec / 60) * 20 + len(commands) * 5))
    entry = {
        "timestamp":                time.strftime('%Y-%m-%dT%H:%M:%S'),
        "event":                    "DWELL_SESSION",
        "ip":                       ip,
        "port":                     port,
        "honeypot_type":            honeypot_type,
        "session_duration_seconds": round(duration_sec, 2),
        "total_commands_sent":      len(commands),
        "commands":                 commands[:20],
        "engagement_score":         engagement_score
    }
    try:
        if not os.path.exists(DWELL_LOG):
            open(DWELL_LOG, 'w').close()
        with open(DWELL_LOG, 'a') as f:
            f.write(json.dumps(entry) + "\n")
    except Exception as e:
        log_event(f"[PHANTOM CLOCK] Log error: {e}", event_type="ERROR")

def show_dwell_stats():
    if not os.path.exists(DWELL_LOG):
        print("[-] No PHANTOM CLOCK data yet. Start IPS and wait for attackers.")
        return
    sessions = []
    try:
        with open(DWELL_LOG) as f:
            for line in f:
                try:
                    sessions.append(json.loads(line.strip()))
                except Exception:
                    pass
    except Exception as e:
        print(f"[-] Error reading PHANTOM CLOCK log: {e}")
        return

    if not sessions:
        print("[-] No sessions recorded yet.")
        return

    ai_sessions     = [s for s in sessions if s.get('honeypot_type') == 'AI_LLM']
    tarpit_sessions = [s for s in sessions if s.get('honeypot_type') == 'TARPIT']

    def avg(lst):
        return sum(lst) / len(lst) if lst else 0
    def fmt(sec):
        return f"{int(sec // 60)}m {int(sec % 60)}s"

    ai_dur = [s.get('session_duration_seconds', 0) for s in ai_sessions]
    tp_dur = [s.get('session_duration_seconds', 0) for s in tarpit_sessions]

    all_cmd = [cmd for s in ai_sessions for cmd in s.get('commands', [])]
    cmd_freq = defaultdict(int)
    for cmd in all_cmd:
        cmd_freq[cmd.strip()] += 1
    top_cmd = sorted(cmd_freq.items(), key=lambda x: -x[1])[:3]

    ai_avg  = avg(ai_dur)
    tp_avg  = avg(tp_dur)
    effect  = (ai_avg / tp_avg) if tp_avg > 0 else 0

    long_s    = sum(1 for d in ai_dur if d > 60)
    eng_rate  = (long_s / len(ai_sessions) * 100) if ai_sessions else 0

    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║          RCDIDN — PHANTOM CLOCK DWELL TIME ANALYSIS      ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print(f"  Total AI Sessions        : {len(ai_sessions)}")
    print(f"  Total Tarpit Sessions    : {len(tarpit_sessions)}")
    print(f"  AI Avg Dwell Time        : {fmt(ai_avg)}")
    if ai_dur:
        print(f"  Longest AI Session       : {fmt(max(ai_dur))}")
    print(f"  Avg Commands / Session   : {avg([s.get('total_commands_sent',0) for s in ai_sessions]):.1f}")
    if top_cmd:
        print(f"  Most Typed Command       : '{top_cmd[0][0]}' ({top_cmd[0][1]}x total)")
    print(f"  Engagement Rate (> 1 min): {eng_rate:.1f}%")
    print("╠══════════════════════════════════════════════════════════╣")
    print("  COMPARISON: AI HONEYPOT vs STATIC TARPIT")
    print(f"  AI Honeypot Avg          : {fmt(ai_avg)}")
    print(f"  Static Tarpit Avg        : {fmt(tp_avg)}")
    if effect > 0:
        print(f"  LLM Effectiveness        : {effect:.1f}x longer than tarpit")
    else:
        print(f"  LLM Effectiveness        : No tarpit data yet for comparison")
    print("╚══════════════════════════════════════════════════════════╝\n")

# ================= HONEYPOT HANDLERS =================
def ai_honeypot_handler(conn: socket.socket, addr):
    attacker_ip   = addr[0]
    session_start = time.time()
    commands      = []
    ai_call_count = 0
    try:
        conn.settimeout(30)
        conn.send(b"Ubuntu 22.04.1 LTS server tty1\nLogin: ")
        conn.recv(1024)
        conn.send(b"Password: ")
        conn.recv(1024)
        conn.send(b"\nWelcome to root. Warning: Filesystem integrity degraded.\nroot@server:~# ")
        while True:
            try:
                conn.settimeout(120)
                data = conn.recv(1024)
                if not data:
                    break
                temporal_deception_delay()
                cmd = data.decode('utf-8', errors='ignore').strip()
                if cmd:
                    commands.append(cmd)
                    if ai_call_count < MAX_AI_CALLS_PER_SESSION:
                        reply = call_llm_interrogator(cmd)
                        ai_call_count += 1
                    else:
                        reply = "kernel: I/O error on device sda: lost connection"
                    conn.send(f"{reply}\nroot@server:~# ".encode('utf-8'))
                else:
                    conn.send(b"root@server:~# ")
            except socket.timeout:
                break
    except Exception as e:
        log_event(f"[AI_HONEYPOT] Session error {attacker_ip}: {e}", event_type="ERROR")
    finally:
        duration = time.time() - session_start
        conn.close()
        log_dwell_session(attacker_ip, 2323, duration, commands, "AI_LLM")
        log_event(
            f"AI session ended: {attacker_ip} | {duration:.0f}s | {len(commands)} cmds",
            event_type="DWELL", ip=attacker_ip, port=2323
        )

def tarpit_handler(conn: socket.socket, addr, port: int):
    attacker_ip   = addr[0]
    session_start = time.time()
    try:
        while True:
            if time.time() - session_start > MAX_TARPIT_SECONDS:
                break
            temporal_deception_delay()
            conn.send(b"\x00" + secrets.token_bytes(4))
            time.sleep(10)
    except Exception:
        pass
    finally:
        duration = time.time() - session_start
        conn.close()
        log_dwell_session(attacker_ip, port, duration, [], "TARPIT")
        log_event(
            f"Tarpit session ended: {attacker_ip} | {duration:.0f}s",
            event_type="DWELL", ip=attacker_ip, port=port
        )

def honeypot_server(port: int, name: str, mode: str = "tarpit"):
    global _honeypot_semaphore
    if port not in _honeypot_semaphore:
        _honeypot_semaphore[port] = threading.Semaphore(MAX_HONEYPOT_THREADS)
    sem = _honeypot_semaphore[port]

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind(('0.0.0.0', port))
        except OSError as e:
            print(f"  [-] HoneyPort '{name}' ({port}) unavailable: {e}")
            log_event(f"[HONEYPOT] Port {port} bind failed: {e}", event_type="ERROR")
            return

        s.listen(10)
        print(f"  [+] HoneyPort '{name}' active on port {port} [{mode.upper()}] (max {MAX_HONEYPOT_THREADS} threads)")
        while True:
            try:
                conn, addr = s.accept()
                attacker_ip = addr[0]
                if attacker_ip not in ('127.0.0.1', '::1'):
                    if not sem.acquire(blocking=False):
                        conn.close()
                        log_event(
                            f"[HONEYPOT] Thread limit reached on port {port} — connection dropped",
                            event_type="WARNING", ip=attacker_ip
                        )
                        continue
                    geo = get_ip_geo(attacker_ip)
                    log_event(
                        f"ATTACK | HoneyPort {name} ({port})",
                        event_type="ATTACK", ip=attacker_ip, port=port,
                        country=geo.get('country')
                    )

                    def _run_and_release(target, args, s=sem):
                        try:
                            target(*args)
                        finally:
                            s.release()

                    if mode == "ai":
                        threading.Thread(
                            target=_run_and_release,
                            args=(ai_honeypot_handler, (conn, addr)),
                            daemon=True
                        ).start()
                    else:
                        threading.Thread(
                            target=_run_and_release,
                            args=(tarpit_handler, (conn, addr, port)),
                            daemon=True
                        ).start()
            except Exception as e:
                log_event(f"[HONEYPOT] Accept error on port {port}: {e}", event_type="ERROR")
    except Exception as e:
        log_event(f"[HONEYPOT] Server error '{name}': {e}", event_type="ERROR")

# ================= OMNIVERSAL AUTO-BLACKLIST IPS =================
def is_valid_ip(ip: str) -> bool:
    """Validasi format IP sebelum masuk ke iptables/netsh — IP injection prevention."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def ban_ip(ip: str, loc: str = "Unknown", isp: str = "Unknown"):
    if not is_valid_ip(ip):
        log_event(f"[BAN] Invalid IP rejected (possible injection): {ip!r}", event_type="ERROR")
        return
    sys_os = platform.system()
    try:
        if sys_os == "Linux":
            check = subprocess.run(
                ["sudo", "iptables", "-L", "INPUT", "-v", "-n"],
                capture_output=True, text=True, timeout=5
            )
            if ip not in check.stdout:
                subprocess.run(
                    ["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"],
                    timeout=5
                )
        elif sys_os == "Windows":
            subprocess.run(
                ["netsh", "advfirewall", "firewall", "add", "rule",
                 f"name=RCDIDN_BLOCK_{ip}", "dir=in", "action=block", f"remoteip={ip}"],
                timeout=5
            )
        elif sys_os == "Darwin":
            subprocess.run(
                ["sudo", "route", "-q", "add", "-host", ip, "127.0.0.1", "-blackhole"],
                timeout=5
            )

        log_event(f"[IPS] Banned: {ip} | {loc} | {isp}", event_type="BAN", ip=ip, country=loc)
        sync_hive_mind(ip, loc, isp)
        print(f"  [BANNED] {ip} [{loc}]")
    except Exception as e:
        log_event(f"[BAN] Error banning {ip}: {e}", event_type="ERROR")

def ips_log_watcher():
    ensure_dirs()
    if not os.path.exists(HIDDEN_LOG):
        open(HIDDEN_LOG, 'w').close()

    banned = set()
    MAX_BANNED_SET = 10000
    try:
        with open(HIDDEN_LOG, 'r') as f:
            f.seek(0, 2)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(1)
                    continue
                try:
                    entry       = json.loads(line.strip())
                    attacker_ip = entry.get('ip')
                    if (attacker_ip and attacker_ip not in ('127.0.0.1', '::1') and
                            attacker_ip not in banned and
                            entry.get('event') in ('ATTACK', 'DWELL', 'GHOSTNET', 'PHEROMONE')):
                        if len(banned) >= MAX_BANNED_SET:
                            banned = set(list(banned)[MAX_BANNED_SET // 2:])
                        banned.add(attacker_ip)
                        geo = get_ip_geo(attacker_ip)
                        ban_ip(attacker_ip, loc=geo.get('country', 'Unknown'), isp=geo.get('isp', 'Unknown'))
                except (json.JSONDecodeError, Exception):
                    pass
    except Exception as e:
        log_event(f"[IPS_WATCHER] Fatal error: {e}", event_type="ERROR")

def start_ips_guard():
    threading.Thread(target=honeypot_server, args=(2323, "AI-Interrogator", "ai"),   daemon=True).start()
    threading.Thread(target=honeypot_server, args=(2222, "Fake-SSH",        "tarpit"), daemon=True).start()
    threading.Thread(target=honeypot_server, args=(3306, "Fake-MySQL",      "tarpit"), daemon=True).start()
    threading.Thread(target=start_ghost_network,                                       daemon=True).start()
    threading.Thread(target=ips_log_watcher,                                           daemon=True).start()

def start_background_ips():
    ensure_dirs()
    script_path = os.path.abspath(__file__)
    sys_os      = platform.system()

    try:
        if sys_os == "Windows":
            proc = subprocess.Popen(
                [sys.executable, script_path, "--ips_daemon"],
                creationflags=0x00000008
            )
        else:
            proc = subprocess.Popen(
                [sys.executable, script_path, "--ips_daemon"],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                preexec_fn=os.setpgrp
            )

        with open(IPS_PID_FILE, "w") as f:
            f.write(str(proc.pid))

        print(f"[+] IPS & AI Honeypot running in background (PID: {proc.pid})")
        log_event(f"[IPS] Daemon started PID {proc.pid}", event_type="IPS_START")
    except Exception as e:
        print(f"[-] Failed to start IPS daemon: {e}")
        log_event(f"[IPS] Start failed: {e}", event_type="ERROR")

def stop_ips():
    if not os.path.exists(IPS_PID_FILE):
        print("[-] IPS daemon is not running.")
        return
    try:
        with open(IPS_PID_FILE, 'r') as f:
            pid_str = f.read().strip()

        if not re.match(r'^\d+$', pid_str) or int(pid_str) < 2:
            print(f"[-] Invalid PID in file: {pid_str!r} — aborting.")
            log_event(f"[IPS] Invalid PID rejected: {pid_str!r}", event_type="ERROR")
            return
        pid = int(pid_str)

        if platform.system() == "Windows":
            subprocess.run(["taskkill", "/PID", str(pid), "/F"], capture_output=True)
        else:
            if not os.path.exists(f"/proc/{pid}"):
                print(f"[-] Process {pid} is not running.")
                log_event(f"[IPS] PID {pid} not found in /proc", event_type="ERROR")
                return
            subprocess.run(["sudo", "kill", "-9", str(pid)], capture_output=True)

        print(f"[+] IPS daemon (PID {pid}) stopped.")
        log_event(f"[IPS] Daemon PID {pid} stopped", event_type="IPS_STOP")
    except Exception as e:
        print(f"[-] Error stopping IPS: {e}")
    finally:
        if os.path.exists(IPS_PID_FILE):
            os.remove(IPS_PID_FILE)

# ================= SENTINEL UI — PSYCHOLOGICAL COUNTERATTACK =================
def build_sentinel_html() -> str:
    rand_hash_admin = hashlib.sha256(secrets.token_bytes(16)).hexdigest()[:32]
    rand_hash_root  = hashlib.sha256(secrets.token_bytes(16)).hexdigest()[:32]
    return f"""<!DOCTYPE html>
<html><head><title>System Compromised</title><style>
body{{background:#000;color:#0f0;font-family:'Courier New',monospace;margin:0;overflow:hidden}}
#terminal{{padding:20px;height:50vh;overflow-y:auto;border-bottom:2px solid #0f0;background:rgba(0,20,0,.9)}}
#map-container{{height:50vh;position:relative}}
.error{{color:#f00;font-weight:700}}.cmd{{color:#fff}}
.fake-sql{{color:#ffea00;margin-top:10px;padding:10px;border:1px dashed #ffea00}}
.alert-rce{{color:#0ff;margin-top:10px;padding:5px;border:1px solid #0ff}}
#map-iframe{{width:100%;height:100%;border:none;filter:invert(90%) hue-rotate(180deg)}}
.overlay{{position:absolute;top:10px;right:10px;background:rgba(0,0,0,.8);padding:10px;
          border:1px solid #0f0;z-index:100;font-size:12px}}
.typing::after{{content:'|';animation:blink 1s infinite}}
@keyframes blink{{50%{{opacity:0}}}}
</style></head><body>
<div id='terminal'>
  <div>[SYSTEM] Reverse connection established...</div>
  <div>[SYSTEM] Accessing /dev/sda1... <span class='cmd'>SUCCESS</span></div>
  <div>[SYSTEM] Hardware ID: <span class='cmd' id='r_gpu'>Scanning...</span></div>
  <div id='rce-alert-container'></div>
  <div class='cmd' style='margin-top:10px'>&gt;&gt; Extracting database credentials...
    <span class='error'>SUCCESS</span></div>
  <div class='fake-sql'>
    [+] TABLE: users_db_dump<br>
    id | username | password_hash<br>
    ---+----------+----------------------------------<br>
    1  | admin    | {rand_hash_admin}<br>
    2  | root     | {rand_hash_root}<br>
    [!] 2 rows extracted.
  </div>
  <div class='error' style='margin-top:10px'>[!] TRACE COMPLETE: TARGET IDENTIFIED [!]</div>
  <div class='cmd'>&gt;&gt; Public IP       : <span id='public_ip'>Detecting...</span></div>
  <div class='cmd'>&gt;&gt; VPN Bypass IP   : <span class='error' id='webrtc_ip'>Piercing tunnel...</span></div>
  <div class='cmd'>&gt;&gt; ISP / Provider  : <span id='isp_data'>Detecting...</span></div>
  <div class='cmd'>&gt;&gt; CPU Threads     : <span id='r_cpu'>...</span></div>
  <div class='error' style='background:#330000;padding:10px;border:1px solid red;margin-top:10px'>
    <div style='color:#fff'>[!] TRANSMITTING ABUSE REPORT TO <b id='isp_target'>ISP</b>...</div>
    <div id='auto-draft' class='typing'
         style='color:#ffea00;margin-top:5px;font-style:italic'></div>
  </div>
</div>
<div id='map-container'>
  <div class='overlay'>
    <b>LIVE GPS TRACKING</b><br>STATUS: <span style='color:#f00'>LOCKED</span>
  </div>
  <iframe id='map-iframe'
    src='https://www.openstreetmap.org/export/embed.html?bbox=106.8227,-6.1751,106.8327,-6.1651&layer=mapnik'>
  </iframe>
</div>
<script>
const urlParams = new URLSearchParams(window.location.search);
const cmdParam  = urlParams.get('cmd');
if (cmdParam) {{
  const wrapper = document.createElement('div');
  wrapper.className = 'alert-rce';
  const label   = document.createTextNode('[!] RCE PAYLOAD INTERCEPTED: ');
  const payload  = document.createElement('span');
  payload.className = 'error';
  payload.textContent = cmdParam;
  const suffix  = document.createTextNode(' | [!] REVERSING SHELL TO SENDER...');
  wrapper.appendChild(label);
  wrapper.appendChild(payload);
  wrapper.appendChild(suffix);
  document.getElementById('rce-alert-container').appendChild(wrapper);
}}
document.addEventListener('copy', e => {{
  e.clipboardData.setData('text/plain', 'YOU ARE TRACKED BY RCDIDN. ALL ACTIONS ARE RECORDED.');
  e.preventDefault();
}});
let global_ip = 'Unknown', global_isp = 'ISP';
async function getRealIP() {{
  try {{
    const pc = new RTCPeerConnection({{iceServers:[{{urls:'stun:stun.l.google.com:19302'}}]}});
    pc.createDataChannel('');
    pc.createOffer().then(o => pc.setLocalDescription(o));
    pc.onicecandidate = ice => {{
      if (ice && ice.candidate && ice.candidate.candidate) {{
        const m = /([0-9]{{1,3}}(\\.[0-9]{{1,3}}){{3}})/.exec(ice.candidate.candidate);
        if (m) document.getElementById('webrtc_ip').innerText = m[1] + ' (TUNNEL COMPROMISED)';
      }}
    }};
  }} catch(e) {{}}
}}
function typeWriter(txt, i) {{
  if (i < txt.length) {{
    document.getElementById('auto-draft').innerHTML +=
      txt[i] === '\\n' ? '<br>' : txt[i];
    setTimeout(() => typeWriter(txt, i + 1), 30);
  }}
}}
function voiceOfGod() {{
  const msg = new SpeechSynthesisUtterance(
    'Target Locked. Tunnel compromised. Law enforcement report generated. Disconnect now.'
  );
  msg.pitch = 0.1; msg.rate = 0.9;
  window.speechSynthesis.speak(msg);
}}
async function capture() {{
  getRealIP();
  const gl  = document.createElement('canvas').getContext('webgl');
  const dbg = gl && gl.getExtension('WEBGL_debug_renderer_info');
  document.getElementById('r_gpu').innerText =
    dbg ? gl.getParameter(dbg.UNMASKED_RENDERER_WEBGL) : 'Generic GPU';
  document.getElementById('r_cpu').innerText = navigator.hardwareConcurrency + ' Threads';
  fetch('https://ip-api.com/json/').then(r => r.json()).then(data => {{
    if (data.status === 'success') {{
      global_ip  = data.query; global_isp = data.isp;
      document.getElementById('public_ip').innerText  = global_ip;
      document.getElementById('isp_data').innerText   = global_isp;
      document.getElementById('isp_target').innerText = 'abuse@' + global_isp;
      document.getElementById('map-iframe').src =
        `https://www.openstreetmap.org/export/embed.html?` +
        `bbox=${{data.lon-.01}},${{data.lat-.01}},${{data.lon+.01}},${{data.lat+.01}}` +
        `&layer=mapnik&marker=${{data.lat}},${{data.lon}}`;
    }}
    const txt =
      `Subject: URGENT — Cyber Attack Report\\n` +
      `Dear ${{global_isp}},\\n` +
      `IP ${{global_ip}} is actively attempting unauthorized server access.\\n` +
      `Hardware signatures and geolocation data have been logged.\\n` +
      `Please suspend this account immediately.\\n` +
      `CC: Cyber Crime Division, Law Enforcement`;
    setTimeout(() => typeWriter(txt, 0), 1000);
  }}).catch(() => {{
    setTimeout(() =>
      typeWriter('Subject: URGENT — Cyber Attack\\nTarget logged.\\nCC: Law Enforcement...', 0),
      1000
    );
  }});
  voiceOfGod();
  setTimeout(() => {{
    window.location.href = 'https://google.com/search?q=cyber+crime+penalties';
  }}, 25000);
}}
window.onload  = capture;
document.body.onclick = voiceOfGod;
</script></body></html>"""

def build_ransom_html() -> str:
    _btc_chars = string.ascii_lowercase + string.digits
    btc_wallet = "bc1q" + ''.join(secrets.choice(_btc_chars) for _ in range(38))
    return f"""<!DOCTYPE html>
<html><head><title>SERVER LOCKED</title><style>
body{{background:#500;color:#fff;font-family:Arial,sans-serif;text-align:center;padding:50px;margin:0}}
.box{{border:3px solid #f00;padding:30px;background:#111;display:inline-block;box-shadow:0 0 20px red}}
h1{{color:#f00;font-size:3em;margin:0 0 10px 0}}
.btc{{background:#333;padding:15px;font-family:monospace;color:#ffea00;font-size:1.2em;border:1px dashed #fff;margin:20px 0}}
</style></head><body>
<div class='box'>
  <h1>YOUR NETWORK HAS BEEN ENCRYPTED</h1>
  <p>All databases and sensitive files are locked with military-grade encryption.</p>
  <p>Send <b>0.5 BTC</b> to the address below to restore your data:</p>
  <div class='btc'>{btc_wallet}</div>
  <p>Time remaining before decryption keys are permanently destroyed:</p>
  <h2 id='timer' style='color:red'>71:59:59</h2>
</div>
<script>
let time = 72 * 3600;
setInterval(() => {{
  time--;
  const h = Math.floor(time / 3600);
  const m = Math.floor((time % 3600) / 60);
  const s = time % 60;
  document.getElementById('timer').innerText = `${{h}}:${{m < 10 ? '0' : ''}}${{m}}:${{s < 10 ? '0' : ''}}${{s}}`;
}}, 1000);
</script></body></html>"""

def inject_sentinel(target: str):
    if not os.path.exists(target) or not target.endswith('.php'):
        return
    try:
        with open(target, 'r') as f:
            content = f.read()
        if "RCDIDN_STRIKE_V15" in content:
            return

        target_dir    = os.path.dirname(os.path.abspath(target))
        web_log_path  = os.path.join(target_dir, "rcdidn_web.log")
        safe_log_path = web_log_path.replace("'", "\\'").replace("\\", "\\\\")

        php_guard = f"""<?php /* RCDIDN_STRIKE_V15 */
error_reporting(0);
$ip  = $_SERVER['REMOTE_ADDR'] ?? 'Unknown';
$ua  = $_SERVER['HTTP_USER_AGENT'] ?? 'None';
$uri = $_SERVER['REQUEST_URI'] ?? '/';
$cmd = htmlspecialchars($_GET['cmd'] ?? $_POST['cmd'] ?? 'None');

if ($cmd === 'None' && preg_match('/(whoami|ls|cat|pwd|wget|curl|bash)/i', $uri, $m)) {{
    $cmd = $m[0];
}}

if (preg_match('/\\.zip|\\.bak|\\.tar|\\.gz/i', $uri)) {{
    @file_put_contents('{safe_log_path}', json_encode(['ts'=>date('c'),'event'=>'ZIP_BOMB','ip'=>$ip]).PHP_EOL, FILE_APPEND);
    header("Content-Encoding: gzip");
    header("Content-Length: 10737418240");
    echo "\\x1f\\x8b\\x08\\x00\\x00\\x00\\x00\\x00";
    while (true) {{
        echo str_repeat("\\0", 1024 * 1024);
        ob_flush();
        flush();
    }}
    die();
}}

if (preg_match('/(shodan|censys|masscan|zgrab|nmap|binaryedge|project sonar)/i', $ua)) {{
    @file_put_contents('{safe_log_path}', json_encode(['ts'=>date('c'),'event'=>'SCANNER','ip'=>$ip,'ua'=>$ua]).PHP_EOL, FILE_APPEND);
    echo file_get_contents(__DIR__ . '/rc_ransom.html');
    die();
}}

$is_attack = (preg_match('/(sqlmap|gobuster|ffuf|dirb|nikto|\\' or|\\" or|union select|<script)/i', $ua . $uri)
    || strpos($uri, '.env') !== false
    || strpos($uri, 'wp-admin') !== false
    || strpos($uri, 'phpmyadmin') !== false
    || $cmd !== 'None');

if ($is_attack) {{
    @file_put_contents('{safe_log_path}', json_encode(['ts'=>date('c'),'event'=>'ATTACK','ip'=>$ip,'uri'=>$uri]).PHP_EOL, FILE_APPEND);
    echo file_get_contents(__DIR__ . '/rc_sentinel.html');
    die();
}}
?>\n"""
        with open(target, 'w') as f:
            f.write(php_guard + content)

        sentinel_path = os.path.join(target_dir, "rc_sentinel.html")
        ransom_path   = os.path.join(target_dir, "rc_ransom.html")

        with open(sentinel_path, 'w') as f:
            f.write(build_sentinel_html())
        with open(ransom_path, 'w') as f:
            f.write(build_ransom_html())

        set_immutable(sentinel_path, True)
        set_immutable(ransom_path,   True)
        print(f"[+] PHP Sentinel injected into {target}")
        print(f"[+] rc_sentinel.html and rc_ransom.html deployed.")
    except Exception as e:
        log_event(f"[SENTINEL] Injection error on {target}: {e}", event_type="ERROR")

# ================= NOVEL #2: MINDPRINT — ATTACKER BEHAVIORAL PROFILING =================
def generate_attacker_profile():
    logs = read_logs()
    if not logs:
        print("[-] No log data available. Start IPS and wait for attacks.")
        return

    ip_data = defaultdict(lambda: {'hits': 0, 'timestamps': [], 'tools': set(), 'events': []})
    for entry in logs:
        ip = entry.get('ip')
        if not ip or ip in ('127.0.0.1', '::1'):
            continue
        d = ip_data[ip]
        d['hits'] += 1
        d['timestamps'].append(entry.get('timestamp', ''))
        if entry.get('tool_detected'):
            d['tools'].add(entry['tool_detected'])
        d['events'].append(entry.get('event', ''))

    AUTO_TOOLS = {'sqlmap', 'gobuster', 'ffuf', 'dirb', 'nikto', 'masscan', 'nmap'}
    SCANNERS   = {'shodan', 'censys', 'zgrab', 'binaryedge'}
    profiles   = []

    for ip, d in ip_data.items():
        hits, tools = d['hits'], d['tools']

        if tools & SCANNERS:
            persona, score = "RESEARCHER", 20
        elif hits >= 10:
            persona, score = "APT_CANDIDATE", 90
        elif hits >= 3:
            persona, score = "PERSISTENT", 70
        elif tools & AUTO_TOOLS:
            persona, score = "SCRIPTKIDDIE", 50
        else:
            persona, score = "UNKNOWN", 30

        if len(d['timestamps']) >= 3:
            try:
                ts_list   = sorted([datetime.strptime(t, '%Y-%m-%dT%H:%M:%S') for t in d['timestamps'] if t])
                intervals = [(ts_list[i+1] - ts_list[i]).total_seconds() for i in range(len(ts_list) - 1)]
                if intervals:
                    avg_i    = sum(intervals) / len(intervals)
                    variance = sum((x - avg_i) ** 2 for x in intervals) / len(intervals)
                    if variance < 5 and avg_i < 60:
                        persona, score = "BOTNET_NODE", 85
            except Exception:
                pass

        geo        = _geo_cache.get(ip, {'country': 'Unknown', 'isp': 'Unknown'})
        first_seen = min(d['timestamps']) if d['timestamps'] else 'Unknown'
        last_seen  = max(d['timestamps']) if d['timestamps'] else 'Unknown'

        profiles.append({
            'ip': ip, 'persona': persona, 'threat_score': score, 'hits': hits,
            'tools': list(tools), 'first_seen': first_seen, 'last_seen': last_seen,
            'country': geo.get('country', 'Unknown'), 'isp': geo.get('isp', 'Unknown')
        })

    profiles.sort(key=lambda x: -x['threat_score'])
    ICONS = {
        'APT_CANDIDATE': '[RED]', 'PERSISTENT': '[ORA]', 'BOTNET_NODE': '[YEL]',
        'SCRIPTKIDDIE': '[GRN]', 'RESEARCHER': '[BLU]', 'UNKNOWN': '[---]'
    }

    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║        RCDIDN — MINDPRINT BEHAVIORAL PROFILING ENGINE    ║")
    print(f"║  Total Unique IPs Profiled : {len(profiles):<28}║")
    print("╠══════════════════════════════════════════════════════════╣")
    for p in profiles[:10]:
        icon = ICONS.get(p['persona'], '[---]')
        print(f"\n  {icon} IP            : {p['ip']} [{p['country']}]")
        print(f"       Persona      : {p['persona']}")
        print(f"       Threat Score : {p['threat_score']}/100")
        print(f"       Total Hits   : {p['hits']}")
        print(f"       First Seen   : {p['first_seen']}")
        print(f"       Last Seen    : {p['last_seen']}")
        if p['tools']:
            print(f"       Tools Used   : {', '.join(p['tools'])}")
        print(f"       ISP          : {p['isp']}")

    if len(profiles) > 10:
        print(f"\n  ... and {len(profiles) - 10} more IP(s)")
    print("\n╚══════════════════════════════════════════════════════════╝\n")

# ================= THREAT INTELLIGENCE DASHBOARD =================
def show_stats():
    logs = read_logs()
    if not logs:
        print("[-] No data yet. Start IPS and wait for attacks to be logged.")
        return

    cutoff = datetime.now() - timedelta(days=30)
    recent = []
    for e in logs:
        try:
            ts = datetime.strptime(e.get('timestamp', ''), '%Y-%m-%dT%H:%M:%S')
            if ts >= cutoff:
                recent.append(e)
        except Exception:
            recent.append(e)

    unique_ips   = set(e.get('ip') for e in recent if e.get('ip'))
    banned_count = sum(1 for e in recent if e.get('event') == 'BAN')
    attack_count = sum(1 for e in recent if e.get('event') == 'ATTACK')
    tool_freq    = defaultdict(int)
    country_freq = defaultdict(int)

    for e in recent:
        if e.get('tool_detected'):
            tool_freq[e['tool_detected']] += 1
        if e.get('country') and e['country'] != 'Unknown':
            country_freq[e['country']] += 1

    total_tools     = sum(tool_freq.values()) or 1
    total_countries = sum(country_freq.values()) or 1

    def bar(pct, width=20):
        filled = int(pct / 100 * width)
        return '█' * filled + '░' * (width - filled)

    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║        RCDIDN — THREAT INTELLIGENCE DASHBOARD            ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print(f"  Period              : Last 30 days")
    print(f"  Total Events        : {len(recent):,}")
    print(f"  Unique Attacker IPs : {len(unique_ips):,}")
    print(f"  IPs Banned          : {banned_count:,}")
    print(f"  Attack Events       : {attack_count:,}")

    if tool_freq:
        print("╠══════════════════════════════════════════════════════════╣")
        print("  TOP ATTACKER TOOLS")
        for tool, count in sorted(tool_freq.items(), key=lambda x: -x[1])[:5]:
            pct = count / total_tools * 100
            print(f"  {tool:<14} {bar(pct)} {pct:.0f}%")

    if country_freq:
        print("╠══════════════════════════════════════════════════════════╣")
        print("  TOP ATTACKING COUNTRIES")
        for country, count in sorted(country_freq.items(), key=lambda x: -x[1])[:5]:
            pct = count / total_countries * 100
            print(f"  {country:<14} {bar(pct)} {pct:.0f}%")

    if os.path.exists(DWELL_LOG):
        dwell_sessions = []
        try:
            with open(DWELL_LOG) as f:
                for line in f:
                    try:
                        dwell_sessions.append(json.loads(line.strip()))
                    except Exception:
                        pass
        except Exception:
            pass
        if dwell_sessions:
            ai_sess     = [s.get('session_duration_seconds', 0) for s in dwell_sessions if s.get('honeypot_type') == 'AI_LLM']
            canary_hits = sum(1 for e in recent if e.get('event') == 'CANARY_HIT')
            print("╠══════════════════════════════════════════════════════════╣")
            print("  PHANTOM CLOCK — HONEYPOT EFFECTIVENESS")
            if ai_sess:
                ai_avg = sum(ai_sess) / len(ai_sess)
                print(f"  AI Honeypot Avg Dwell : {int(ai_avg//60)}m {int(ai_avg%60)}s")
            print(f"  Canary Hits           : {canary_hits}")
            print(f"  Total Dwell Sessions  : {len(dwell_sessions)}")

    print("╚══════════════════════════════════════════════════════════╝\n")

# ================= HTML THREAT INTELLIGENCE REPORT =================
def generate_threat_report():
    logs           = read_logs()
    dwell_sessions = []
    if os.path.exists(DWELL_LOG):
        try:
            with open(DWELL_LOG) as f:
                for line in f:
                    try:
                        dwell_sessions.append(json.loads(line.strip()))
                    except Exception:
                        pass
        except Exception:
            pass

    unique_ips   = set(e.get('ip') for e in logs if e.get('ip'))
    banned_count = sum(1 for e in logs if e.get('event') == 'BAN')
    attack_count = sum(1 for e in logs if e.get('event') == 'ATTACK')

    tool_freq    = defaultdict(int)
    country_freq = defaultdict(int)
    for e in logs:
        if e.get('tool_detected'):
            tool_freq[e['tool_detected']] += 1
        if e.get('country') and e['country'] != 'Unknown':
            country_freq[e['country']] += 1

    tool_labels    = json.dumps(list(tool_freq.keys())[:8])
    tool_values    = json.dumps(list(tool_freq.values())[:8])
    country_labels = json.dumps(list(country_freq.keys())[:8])
    country_values = json.dumps(list(country_freq.values())[:8])

    ai_dur = [s.get('session_duration_seconds', 0) for s in dwell_sessions if s.get('honeypot_type') == 'AI_LLM']
    tp_dur = [s.get('session_duration_seconds', 0) for s in dwell_sessions if s.get('honeypot_type') == 'TARPIT']
    ai_avg = sum(ai_dur) / len(ai_dur) if ai_dur else 0
    tp_avg = sum(tp_dur) / len(tp_dur) if tp_dur else 0
    effect = (ai_avg / tp_avg) if tp_avg > 0 else 0

    report_date = time.strftime('%Y-%m-%d %H:%M:%S')
    filename    = f"rcdidn_report_{time.strftime('%Y%m%d_%H%M%S')}.html"

    html = f"""<!DOCTYPE html>
<html lang='en'><head><meta charset='UTF-8'>
<title>RCDIDN Threat Intelligence Report — {report_date}</title>
<script src='https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js'></script>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#0a0a0a;color:#e0e0e0;font-family:'Courier New',monospace;padding:20px}}
.header{{border:2px solid #0f0;padding:20px;margin-bottom:20px;background:#0d150d}}
.header h1{{color:#0f0;font-size:2em;letter-spacing:3px}}
.header p{{color:#888;margin-top:5px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:15px;margin-bottom:20px}}
.card{{background:#111;border:1px solid #333;padding:20px;border-radius:4px}}
.card .num{{font-size:2.5em;color:#0f0;font-weight:bold}}
.card .label{{color:#888;font-size:.85em;margin-top:5px}}
.chart-row{{display:grid;grid-template-columns:1fr 1fr;gap:15px;margin-bottom:20px}}
.chart-box{{background:#111;border:1px solid #333;padding:20px;border-radius:4px}}
.chart-box h3{{color:#0f0;margin-bottom:15px;font-size:.9em;letter-spacing:1px}}
.dwell-box{{background:#111;border:2px solid #0f0;padding:20px;margin-bottom:20px;border-radius:4px}}
.dwell-box h3{{color:#0f0;margin-bottom:10px;letter-spacing:1px}}
.dwell-stat{{display:inline-block;margin:10px 20px;text-align:center}}
.dwell-stat .val{{font-size:1.8em;color:#0ff;font-weight:bold}}
.dwell-stat .lbl{{color:#888;font-size:.8em}}
.footer{{color:#444;font-size:.75em;margin-top:20px;border-top:1px solid #222;padding-top:10px}}
canvas{{max-height:250px}}
</style></head><body>
<div class='header'>
  <h1>⚡ RCDIDN THREAT INTELLIGENCE REPORT</h1>
  <p>Generated  : {report_date}</p>
  <p>Creator    : Muhamad Fadhil Faturohman | RCDIDN V1.0 HACKER KILLER</p>
  <p>Log entries analyzed : {len(logs):,}</p>
</div>
<div class='grid'>
  <div class='card'><div class='num'>{len(unique_ips):,}</div>
    <div class='label'>UNIQUE ATTACKER IPs</div></div>
  <div class='card'><div class='num'>{len(logs):,}</div>
    <div class='label'>TOTAL EVENTS</div></div>
  <div class='card'><div class='num'>{banned_count:,}</div>
    <div class='label'>IPs BANNED</div></div>
  <div class='card'><div class='num'>{attack_count:,}</div>
    <div class='label'>ATTACK EVENTS</div></div>
  <div class='card'><div class='num'>{len(dwell_sessions):,}</div>
    <div class='label'>DWELL SESSIONS</div></div>
</div>
<div class='dwell-box'>
  <h3>⏱ PHANTOM CLOCK — LLM DWELL TIME ANALYSIS (Novel Research)</h3>
  <div class='dwell-stat'>
    <div class='val'>{int(ai_avg//60)}m {int(ai_avg%60)}s</div>
    <div class='lbl'>AI HONEYPOT AVG</div></div>
  <div class='dwell-stat'>
    <div class='val'>{int(tp_avg//60)}m {int(tp_avg%60)}s</div>
    <div class='lbl'>STATIC TARPIT AVG</div></div>
  <div class='dwell-stat'>
    <div class='val'>{len(ai_dur)}</div>
    <div class='lbl'>AI SESSIONS</div></div>
  <div class='dwell-stat'>
    <div class='val'>{effect:.1f}x</div>
    <div class='lbl'>LLM EFFECTIVENESS</div></div>
</div>
<div class='chart-row'>
  <div class='chart-box'>
    <h3>ATTACK TOOLS DETECTED</h3>
    <canvas id='toolChart'></canvas>
  </div>
  <div class='chart-box'>
    <h3>TOP ATTACKING COUNTRIES</h3>
    <canvas id='countryChart'></canvas>
  </div>
</div>
<div class='footer'>
  RCDIDN V1.0 — HACKER KILLER | Radioactive Cognitive Data Indonesia |
  Creator: Muhamad Fadhil Faturohman<br>
  Report generated from real deployment data.
  All attacker intelligence is logged for research and defensive purposes only.
</div>
<script>
const C = ['#0f0','#0ff','#ff0','#f80','#f0f','#08f','#f00','#8f0'];
new Chart(document.getElementById('toolChart'), {{
  type: 'bar',
  data: {{
    labels: {tool_labels},
    datasets: [{{ data: {tool_values}, backgroundColor: C, borderWidth: 0 }}]
  }},
  options: {{
    plugins: {{ legend: {{ display: false }} }},
    scales: {{
      x: {{ ticks: {{ color: '#888' }}, grid: {{ color: '#222' }} }},
      y: {{ ticks: {{ color: '#888' }}, grid: {{ color: '#222' }} }}
    }}
  }}
}});
new Chart(document.getElementById('countryChart'), {{
  type: 'doughnut',
  data: {{
    labels: {country_labels},
    datasets: [{{ data: {country_values}, backgroundColor: C, borderWidth: 0 }}]
  }},
  options: {{ plugins: {{ legend: {{ labels: {{ color: '#888' }} }} }} }}
}});
</script></body></html>"""

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"\n[+] Generating threat intelligence report...")
    print(f"[+] Analyzed {len(logs):,} log entries")
    print(f"[+] Report saved : {filename}")
    print(f"[+] Open in any browser to view the visualizations.\n")

# ================= SELF-TEST SUITE =================
def run_self_test():
    import tempfile
    passed, failed = 0, 0
    print("\n[=== RCDIDN SELF-TEST SUITE — V1.0 HACKER KILLER ===]")

    # Test 1: AES-256-GCM encrypt/decrypt round-trip
    try:
        test_key = os.urandom(32)
        with tempfile.NamedTemporaryFile(suffix='.env', delete=False, mode='w') as tf:
            tf.write("SECRET=production_value_xyz\nDB_PASS=real_db_password_123")
            tp = tf.name
        original = open(tp).read()
        vp       = encrypt_file(tp, test_key)
        with open(tp, 'w') as f:
            f.write("FAKE=canary_placeholder")
        decrypt_file(vp, tp, test_key)
        restored = open(tp).read()
        assert restored == original, f"Content mismatch"
        set_immutable(vp, False)
        os.remove(vp)
        os.remove(tp)
        print("  [PASS] Test 1 : AES-256-GCM encrypt → decrypt round-trip")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 1 : {e}")
        failed += 1

    # Test 2: MIRAGE DROP canary generation
    try:
        canary = generate_canary("/project/.env")
        assert "production_value_xyz" not in canary, "Canary contains real data"
        assert "AKIA" in canary or "sk_live_" in canary, "Canary not realistic"
        assert len(canary) > 50, "Canary too short"
        print("  [PASS] Test 2 : MIRAGE DROP canary generation")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 2 : {e}")
        failed += 1

    # Test 3: PBKDF2HMAC key derivation
    try:
        salt = os.urandom(32)
        k1   = derive_true_aes256_key("same_master_key", salt)
        k2   = derive_true_aes256_key("same_master_key", salt)
        k3   = derive_true_aes256_key("different_master_key", salt)
        assert k1 == k2, "Key is not deterministic"
        assert k1 != k3, "Different keys produce same output"
        assert len(k1) == 32, f"Invalid key length: {len(k1)}"
        AESGCM(k1)
        print("  [PASS] Test 3 : PBKDF2HMAC Key derivation (deterministic, unique, AES-256-GCM compatible)")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 3 : {e}")
        failed += 1

    # Test 4: Structured JSON logging
    try:
        ensure_dirs()
        log_event("rcdidn_self_test_marker", event_type="TEST", ip="10.0.0.1")
        with open(HIDDEN_LOG) as f:
            last_line = f.readlines()[-1].strip()
        entry = json.loads(last_line)
        assert entry.get('event') == "TEST", "Wrong event type"
        assert entry.get('ip')    == "10.0.0.1", "IP not stored"
        assert 'timestamp' in entry, "Missing timestamp"
        print("  [PASS] Test 4 : Structured JSON logging")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 4 : {e}")
        failed += 1

    # Test 5: Encrypted Shadow Manifest
    try:
        import tempfile as tf2
        test_manifest = {"file_a.env": "vault_a.enc", "file_b.json": "vault_b.enc"}
        with tf2.TemporaryDirectory() as tmpdir:
            test_key_mani = os.urandom(32)
            save_manifest(tmpdir, test_manifest, test_key_mani)
            loaded = load_manifest(tmpdir, test_key_mani)
            assert loaded == test_manifest, f"Manifest mismatch: {loaded}"
            manifest_path = os.path.join(tmpdir, MANIFEST_NAME)
            set_immutable(manifest_path, False)
        print("  [PASS] Test 5 : Encrypted Shadow manifest save → load")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 5 : {e}")
        failed += 1

    # Test 6: Wrong password raises InvalidTag
    try:
        key_a = os.urandom(32)
        key_b = os.urandom(32)
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False, mode='w') as tf:
            tf.write('{"test": "production_data"}')
            tp = tf.name
        vp = encrypt_file(tp, key_a)
        try:
            decrypt_file(vp, tp + ".out", key_b)
            print("  [FAIL] Test 6 : Wrong key was NOT detected")
            failed += 1
        except InvalidTag:
            print("  [PASS] Test 6 : Wrong password correctly raises InvalidTag (AES-GCM Authenticated)")
            passed += 1
        finally:
            set_immutable(vp, False)
            for p in [vp, tp, tp + ".out"]:
                if os.path.exists(p):
                    os.remove(p)
    except Exception as e:
        print(f"  [FAIL] Test 6 : {e}")
        failed += 1

    total = passed + failed
    print(f"\n  Result : {passed}/{total} tests passed")
    if failed == 0:
        print("  [OK] ALL TESTS PASSED — RCDIDN IS MILITARY-GRADE READY\n")
        return True
    else:
        print("  [!!] SOME TESTS FAILED — Do not deploy until all tests pass\n")
        return False

# ================= SYSTEM STATUS =================
def cmd_status():
    print("\n[=== RCDIDN V1.0 HACKER KILLER — SYSTEM STATUS ===]")
    manifest_path = os.path.join(".", MANIFEST_NAME)
    if os.path.exists(manifest_path):
        print(f"  [+] Shadow Manifest   : Found (Encrypted Blob)")
    else:
        print("  [-] Shadow Manifest   : not found in current directory")

    if os.path.exists(VAULT_DIR):
        vault_files = list(Path(VAULT_DIR).glob("*.enc"))
        print(f"  [+] Vault Files       : {len(vault_files)}")

    # FIX: Verifikasi proses masih hidup via os.kill(pid, 0)
    if os.path.exists(IPS_PID_FILE):
        try:
            with open(IPS_PID_FILE) as f:
                pid_str = f.read().strip()
            if re.match(r'^\d+$', pid_str) and int(pid_str) >= 2:
                pid = int(pid_str)
                try:
                    os.kill(pid, 0)  # Cek proses masih hidup tanpa kill
                    print(f"  [+] IPS Daemon PID    : {pid} (verified running)")
                except (ProcessLookupError, OSError):
                    print(f"  [!] IPS Daemon PID    : {pid} (DEAD — process not found, stale PID file)")
            else:
                print("  [!] IPS Daemon        : invalid PID in file")
        except Exception:
            print("  [-] IPS Daemon        : could not read PID file")
    else:
        print("  [-] IPS Daemon        : not running")

    if os.path.exists(HIDDEN_LOG):
        try:
            count = sum(1 for _ in open(HIDDEN_LOG))
            size  = os.path.getsize(HIDDEN_LOG)
            print(f"  [+] Log Entries       : {count:,} ({size/1024:.1f} KB)")
        except Exception:
            print("  [?] Log Entries       : (file sedang dirotasi)")

    if os.path.exists(DWELL_LOG):
        try:
            dc = sum(1 for _ in open(DWELL_LOG))
            print(f"  [+] PHANTOM CLOCK     : {dc} session(s) recorded")
        except Exception:
            print("  [?] PHANTOM CLOCK     : (file sedang dirotasi)")

    if os.path.exists(CANARY_LOG):
        try:
            cc = sum(1 for _ in open(CANARY_LOG))
            print(f"  [+] MIRAGE DROP Hits  : {cc}")
        except Exception:
            print("  [?] MIRAGE DROP Hits  : (file sedang dirotasi)")

    if os.path.exists(DARK_MIRROR_LOG):
        try:
            dm = sum(1 for _ in open(DARK_MIRROR_LOG))
            print(f"  [+] DARK MIRROR       : {dm} session(s)")
        except Exception:
            pass

    if os.path.exists(GHOST_NETWORK_LOG):
        try:
            gn = sum(1 for _ in open(GHOST_NETWORK_LOG))
            print(f"  [+] GHOST NETWORK     : {gn} pivot attempt(s)")
        except Exception:
            pass

    hive_url = os.environ.get("RCDIDN_HIVE_URL", "")
    if hive_url:
        print(f"  [+] HIVE-MIND Webhook : {hive_url[:50]}...")
    else:
        print("  [-] HIVE-MIND Webhook : not configured (set RCDIDN_HIVE_URL)")
    print()

# ================= INTERACTIVE COMMANDER SHELL =================
COMMANDER_ART = """
  ╔══════════════════════════════════════════════════════════════════╗
  ║          RCDIDN V1.0 — HACKER KILLER COMMANDER                   ║
  ║          Radioactive Cognitive Data Indonesia                    ║
  ╠══════════════════════════════════════════════════════════════════╣
  ║  CORE DEFENSE                                                    ║
  ║  run          → Vault files + deploy MIRAGE DROP canaries        ║
  ║  restart      → Re-lock files with current key                   ║
  ║  restore      → Decrypt all files back to original               ║
  ║  gk           → Rotate Master Password                           ║
  ╠══════════════════════════════════════════════════════════════════╣
  ║  IPS & HONEYPOT                                                  ║
  ║  ips start    → Start IPS + AI Honeypot + Ghost Network          ║
  ║  ips stop     → Stop all honeypot daemons                        ║
  ╠══════════════════════════════════════════════════════════════════╣
  ║  THREAT INTELLIGENCE                                             ║
  ║  stats        → Live threat intelligence dashboard               ║
  ║  profile      → MINDPRINT attacker behavioral profiling          ║
  ║  dwelltime    → PHANTOM CLOCK LLM dwell time analysis            ║
  ║  canary       → MIRAGE DROP canary hit tracker                   ║
  ║  report       → Generate HTML threat intelligence report         ║
  ╠══════════════════════════════════════════════════════════════════╣
  ║  NOVEL RESEARCH FEATURES                                         ║
  ║  temporal     → TEMPORAL DECEPTION GRID — timing manipulation    ║
  ║    profiles: off|random_chaos|busy_server|flapping|              ║
  ║              degrading|recovering|tarpit_extreme                 ║
  ║  mirror       → DARK MIRROR — attacker OS/tool detection         ║
  ║  mirror stats → Show Dark Mirror session statistics              ║
  ║  economics    → HONEYPOT ECONOMICS — cost imposed on attackers   ║
  ║  pheromone    → DIGITAL PHEROMONE — active attacker attraction   ║
  ║  ghostnet     → GHOST NETWORK — 10 fake enterprise hosts         ║
  ║  ghostnet stats → Ghost Network topology hit statistics          ║
  ║  evidence     → REGULATORY TRAP — forensic evidence collection   ║
  ╠══════════════════════════════════════════════════════════════════╣
  ║  SYSTEM                                                          ║
  ║  test         → Run self-test suite (6 unit tests)               ║
  ║  status       → Show vault and daemon status                     ║
  ║  help         → Show this menu                                   ║
  ║  exit         → Exit commander                                   ║
  ╠══════════════════════════════════════════════════════════════════╣
  ║  AI HONEYPOT CONFIG                                              ║
  ║  setkey       → Set AI provider + key (Gemini/OpenAI/Claude/     ║
  ║                 DeepSeek)                                        ║
  ║  aikey        → Show active AI provider and key status           ║
  ║  hiveset      → Set HIVE-MIND webhook URL                        ║
  ╚══════════════════════════════════════════════════════════════════╝
"""

def _show_ai_status():
    key      = os.environ.get("RCDIDN_AI_KEY", "").strip()
    provider = os.environ.get("RCDIDN_AI_PROVIDER", "gemini").strip().upper()
    if key:
        masked = key[:8] + "*" * max(0, len(key) - 12) + key[-4:] if len(key) > 12 else key[:4] + "****"
        print(f"  [AI HONEYPOT]  Status : ACTIVE  |  Provider : {provider}")
        print(f"  [AI HONEYPOT]  Key    : {masked}  |  Port 2323 ready")
    else:
        print("  [AI HONEYPOT]  Status : INACTIVE  (no RCDIDN_AI_KEY set)")
        print("  [AI HONEYPOT]  Tip    : type 'setkey' to configure your preferred AI provider")

def interactive_shell():
    print_banner()
    print(COMMANDER_ART)
    _show_ai_status()
    print()

    project_root = "."
    while True:
        try:
            cmd_input = input("RCDIDN > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n[*] Session terminated.")
            break

        if not cmd_input:
            continue

        if cmd_input == "run":
            master_key = get_or_create_key()
            secure_massal(project_root, master_key)
        elif cmd_input == "restart":
            master_key = get_or_create_key()
            restart_lock(project_root, master_key)
        elif cmd_input == "restore":
            c = input("  [!] Restore ALL files? Canaries will be removed. (y/N): ").strip().lower()
            if c == 'y':
                master_key = get_or_create_key()
                restore_files(project_root, master_key)
            else:
                print("  [*] Restore cancelled.")
        elif cmd_input == "gk":
            cmd_generate_key()
        elif cmd_input == "ips start":
            start_background_ips()
        elif cmd_input == "ips stop":
            stop_ips()

        # --- ADVANCED WARFARE COMMANDS ---
        elif cmd_input.startswith("temporal"):
            cmd_temporal(cmd_input)
        elif cmd_input == "mirror stats":
            show_dark_mirror_stats()
        elif cmd_input == "mirror":
            cmd_mirror()
        elif cmd_input == "economics":
            show_economics()
        elif cmd_input.startswith("pheromone"):
            cmd_pheromone(cmd_input)
        elif cmd_input == "ghostnet stats":
            show_ghost_network_stats()
        elif cmd_input == "ghostnet":
            cmd_ghostnet()
        elif cmd_input.startswith("evidence"):
            cmd_evidence(cmd_input)

        # --- THREAT INTEL COMMANDS ---
        elif cmd_input == "stats":
            show_stats()
        elif cmd_input == "profile":
            generate_attacker_profile()
        elif cmd_input == "dwelltime":
            show_dwell_stats()
        elif cmd_input == "canary":
            show_canary_stats()
        elif cmd_input == "report":
            generate_threat_report()

        # --- SYSTEM COMMANDS ---
        elif cmd_input == "test":
            run_self_test()
        elif cmd_input == "status":
            cmd_status()
        elif cmd_input in ("help", "?"):
            print(COMMANDER_ART)

        # --- AI CONFIG COMMANDS ---
        elif cmd_input == "setkey":
            print("\n  [AI HONEYPOT CONFIGURATION]")
            print("  Select your preferred AI Provider:")
            print("  1) Gemini (Google) - Default (free tier available)")
            print("  2) OpenAI (ChatGPT)")
            print("  3) Anthropic (Claude)")
            print("  4) DeepSeek")
            try:
                choice       = input("  Choice (1-4) [default: 1]: ").strip()
                provider_map = {"1": "gemini", "2": "openai", "3": "anthropic", "4": "deepseek"}
                provider     = provider_map.get(choice, "gemini")
                print(f"\n  [AI HONEYPOT] Enter your {provider.upper()} API key.")
                new_key = input("  API Key: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n  [*] Cancelled.")
                continue

            if not new_key:
                print("  [*] No key entered. Cancelled.")
                continue

            os.environ["RCDIDN_AI_PROVIDER"] = provider
            os.environ["RCDIDN_AI_KEY"]      = new_key
            bashrc = os.path.join(str(pathlib.Path.home()), ".bashrc")
            try:
                if os.path.exists(bashrc):
                    with open(bashrc, "r") as f:
                        existing = f.read()
                    lines_rc = [l for l in existing.splitlines()
                                if "RCDIDN_AI_KEY" not in l and "RCDIDN_AI_PROVIDER" not in l]
                    with open(bashrc, "w") as f:
                        f.write("\n".join(lines_rc) + "\n")
                with open(bashrc, "a") as f:
                    safe_key = new_key.replace("\\", "\\\\").replace('"', '\\"')
                    f.write(f'\nexport RCDIDN_AI_PROVIDER="{provider}"  # Added by RCDIDN\n')
                    f.write(f'export RCDIDN_AI_KEY="{safe_key}"  # Added by RCDIDN\n')
                print(f"  [+] API key and provider saved to {bashrc}")
            except Exception as e:
                print(f"  [!] Could not write to {bashrc}: {e}")
                print(f"  [!] Key is active for this session only.")

            masked = new_key[:8] + "*" * max(0, len(new_key) - 12) + new_key[-4:] if len(new_key) > 12 else new_key[:4] + "****"
            print(f"  [+] AI Honeypot ACTIVATED via {provider.upper()}  |  Key: {masked}")
            print(f"  [+] Run 'ips start' to launch AI Interrogator on port 2323")
            log_event(f"[CONFIG] API provider set to {provider} via commander", event_type="SYSTEM")

        elif cmd_input == "aikey":
            _show_ai_status()

        elif cmd_input == "hiveset":
            print("\n  [HIVE-MIND WEBHOOK CONFIGURATION]")
            print("  Set the URL of your central threat intelligence aggregator.")
            print("  The server should accept HTTP POST with JSON body.")
            try:
                hive_url    = input("  Webhook URL: ").strip()
                hive_secret = input("  Secret key (optional, sent as X-RCDIDN-Key header): ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n  [*] Cancelled.")
                continue
            if not hive_url:
                print("  [*] No URL entered. Cancelled.")
                continue
            os.environ["RCDIDN_HIVE_URL"]    = hive_url
            os.environ["RCDIDN_HIVE_SECRET"] = hive_secret
            bashrc = os.path.join(str(pathlib.Path.home()), ".bashrc")
            try:
                with open(bashrc, "a") as f:
                    f.write(f'\nexport RCDIDN_HIVE_URL="{hive_url}"  # Added by RCDIDN\n')
                    if hive_secret:
                        f.write(f'export RCDIDN_HIVE_SECRET="{hive_secret}"  # Added by RCDIDN\n')
                print(f"  [+] Hive webhook saved to {bashrc}")
            except Exception as e:
                print(f"  [!] Could not write to .bashrc: {e}")
            print(f"  [+] HIVE-MIND active → {hive_url}")
            log_event(f"[CONFIG] Hive webhook set to {hive_url}", event_type="SYSTEM")

        elif cmd_input in ("exit", "quit", "q"):
            print("[*] RCDIDN Commander terminated.")
            break
        else:
            print(f"  [-] Unknown command: '{cmd_input}'. Type 'help' for the menu.")

# ================= SYSTEMD SERVICE INSTALLER =================
def install_systemd_service():
    if platform.system() != "Linux":
        print("[-] Systemd installer is only available on Linux.")
        print("[*] Windows : use Task Scheduler")
        print("[*] macOS   : use launchd (launchctl)")
        return

    script_path     = os.path.abspath(__file__)
    python_path     = sys.executable
    service_file    = "/etc/systemd/system/rcdidn.service"
    service_content = f"""[Unit]
Description=RCDIDN V1.0 HACKER KILLER — IPS & Honeypot Daemon
Documentation=https://github.com/rcdidn
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=root
WorkingDirectory=/root
ExecStart={python_path} {script_path} --ips_daemon
Restart=always
RestartSec=10
StandardOutput=append:/var/log/rcdidn.log
StandardError=append:/var/log/rcdidn_error.log

[Install]
WantedBy=multi-user.target
"""
    try:
        with open(service_file, 'w') as f:
            f.write(service_content)

        for cmd in [
            ["systemctl", "daemon-reload"],
            ["systemctl", "enable", "rcdidn"],
            ["systemctl", "start",  "rcdidn"]
        ]:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"[-] Command failed: {' '.join(cmd)}: {result.stderr.strip()}")
                return

        print("""
╔══════════════════════════════════════════════════════════╗
║       RCDIDN SUCCESSFULLY INSTALLED AS A SERVICE         ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  [OK] Service active and running 24/7                    ║
║  [OK] Auto-starts on server reboot                       ║
║  [OK] Auto-restarts on crash (10s delay)                 ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║  MONITORING COMMANDS:                                    ║
║                                                          ║
║  systemctl status rcdidn          check status           ║
║  systemctl stop rcdidn            stop temporarily       ║
║  systemctl restart rcdidn         restart service        ║
║  journalctl -u rcdidn -f          live log stream        ║
║  tail -f /var/log/rcdidn.log      output log             ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║  ACTIVE HONEYPOT PORTS:                                  ║
║  2323  AI Interrogator  (PHANTOM CLOCK)                  ║
║  2222  Fake SSH         (Tarpit)                         ║
║  3306  Fake MySQL       (Tarpit)                         ║
║  4444  Ghost Network    (10 Fake Enterprise Hosts)       ║
║  8080  Dark Mirror      (OS/Tool Fingerprinting)         ║
╚══════════════════════════════════════════════════════════╝
""")
        log_event("[INSTALL] Systemd service installed and started", event_type="SYSTEM")
    except PermissionError:
        print("[-] Permission denied. Run with sudo:")
        print(f"    sudo python3 {script_path} --install")
    except Exception as e:
        print(f"[-] Installation failed: {e}")
        log_event(f"[INSTALL] Failed: {e}", event_type="ERROR")

def uninstall_systemd_service():
    if platform.system() != "Linux":
        print("[-] Only available on Linux.")
        return

    service_file = "/etc/systemd/system/rcdidn.service"
    try:
        for cmd in [
            ["systemctl", "stop",    "rcdidn"],
            ["systemctl", "disable", "rcdidn"],
            ["systemctl", "daemon-reload"]
        ]:
            subprocess.run(cmd, capture_output=True)

        if os.path.exists(service_file):
            os.remove(service_file)

        print("[+] RCDIDN service successfully removed from systemd.")
        log_event("[UNINSTALL] Systemd service removed", event_type="SYSTEM")
    except PermissionError:
        print("[-] Permission denied. Run with sudo:")
        print(f"    sudo python3 {os.path.abspath(__file__)} --uninstall")
    except Exception as e:
        print(f"[-] Uninstall failed: {e}")

# ================= ENTRY POINT =================
def main():
    parser = argparse.ArgumentParser(
        prog="rcdidn",
        description="""
╔══════════════════════════════════════════════════════════╗
║         RCDIDN V1.0 — HACKER KILLER                      ║
║  Radioactive Cognitive Data Indonesia                    ║
║  Creator: Muhamad Fadhil Faturohman                      ║
╚══════════════════════════════════════════════════════════╝

Defensive security system — 38 active features:
  AES-256 file vault        PHANTOM CLOCK LLM dwell time
  MIRAGE DROP canary drops  MINDPRINT behavioral profiling
  AI honeypot (Multi-LLM)   Auto-ban IPS firewall
  PHP sentinel injection    HTML threat report generator
  TEMPORAL DECEPTION GRID   DARK MIRROR OS fingerprinting
  HONEYPOT ECONOMICS        DIGITAL PHEROMONE bait files
  GHOST NETWORK topology    REGULATORY TRAP evidence zip
  HIVE-MIND webhook sync
""",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
USAGE EXAMPLES:
  python rcdidn.py                   open interactive commander shell
  python rcdidn.py --run             vault all sensitive files immediately
  python rcdidn.py --restore         restore all files from vault
  python rcdidn.py --status          show system status
  python rcdidn.py --test            run self-test suite (6 unit tests)
  python rcdidn.py --stats           show threat intelligence dashboard
  python rcdidn.py --report          generate HTML threat report
  sudo python rcdidn.py --install    install as systemd service (24/7)
  sudo python rcdidn.py --uninstall  remove systemd service

COMMANDER SHELL COMMANDS:
  CORE DEFENSE   : run  restart  restore  gk
  IPS & HONEYPOT : ips start  ips stop
  INTELLIGENCE   : stats  profile  dwelltime  canary  report
  SYSTEM         : test  status  help  exit
  AI CONFIG      : setkey  aikey  hiveset

  ── NOVEL RESEARCH FEATURES (9 world-first contributions) ──
  temporal                    TEMPORAL DECEPTION GRID status & stats
  temporal profile <n>        Switch timing profile:
                              off | random_chaos | busy_server |
                              flapping | degrading | recovering |
                              tarpit_extreme
  mirror                      DARK MIRROR — OS/tool fingerprinting
  mirror stats                Dark Mirror session statistics
  economics                   HONEYPOT ECONOMICS — cost imposed on attackers
  pheromone deploy [target]   Deploy bait files (all or specific target)
  pheromone stats             Pheromone hit statistics
  ghostnet                    GHOST NETWORK — 10 fake enterprise hosts
  ghostnet stats              Ghost Network topology hit statistics
  evidence collect            Collect all forensic evidence (cryptographic)
  evidence report idcert      Generate report for ID-CERT Indonesia
  evidence report bssid       Generate report for BSSN Indonesia
  evidence report interpol    Generate report for INTERPOL Cybercrime
  evidence report generic     Generate generic international format

ENVIRONMENT VARIABLES:
  RCDIDN_AI_KEY        Your LLM API key. Powers AI Interrogator on port 2323.
  RCDIDN_AI_PROVIDER   AI provider: gemini (default) | openai | anthropic | deepseek
  RCDIDN_HIVE_URL      Webhook URL for HIVE-MIND threat intel sync (optional)
  RCDIDN_HIVE_SECRET   Auth token sent as X-RCDIDN-Key header (optional)
  RCDIDN_NO_DESTRUCT   Set to 1 to disable self-destruct (use for coverage/profiling)

FILE LOCATIONS:
  Vault         : ~/.rcdidn_vault/
  Logs          : ~/.sys_meta_rcdidn/sys_kern_meta.log
  Salt          : ~/.sys_meta_rcdidn/sys_crypto_salt.bin
  PHANTOM CLOCK : ~/.sys_meta_rcdidn/phantom_clock.log
  Canary        : ~/.sys_meta_rcdidn/canary_hits.log
  Dark Mirror   : ~/.sys_meta_rcdidn/dark_mirror.log
  Economics     : ~/.sys_meta_rcdidn/economics.log
  Pheromone     : ~/.sys_meta_rcdidn/pheromone.log
  Ghost Network : ~/.sys_meta_rcdidn/ghost_network.log
  Evidence      : ~/.sys_meta_rcdidn/legal_evidence/
"""
    )
    parser.add_argument("--ips_daemon", action="store_true", help="[INTERNAL] Run as background IPS/Honeypot daemon")
    parser.add_argument("--run",        action="store_true", help="Vault all sensitive files in the current directory")
    parser.add_argument("--restore",    action="store_true", help="Restore all encrypted files from vault")
    parser.add_argument("--status",     action="store_true", help="Show system status (vault, daemon, logs)")
    parser.add_argument("--test",       action="store_true", help="Run the self-test suite (6 unit tests)")
    parser.add_argument("--stats",      action="store_true", help="Show ASCII threat intelligence dashboard")
    parser.add_argument("--report",     action="store_true", help="Generate an HTML threat intelligence report")
    parser.add_argument("--install",    action="store_true", help="Install RCDIDN as a systemd service for 24/7 auto-run (requires sudo)")
    parser.add_argument("--uninstall",  action="store_true", help="Remove RCDIDN from systemd (requires sudo)")
    args = parser.parse_args()

    if args.ips_daemon:
        ensure_dirs()
        log_event("[IPS] Daemon started", event_type="IPS_START")
        start_ips_guard()
        while True:
            time.sleep(60)

    elif args.install:
        install_systemd_service()

    elif args.uninstall:
        uninstall_systemd_service()

    elif any([args.run, args.restore, args.status, args.test, args.stats, args.report]):
        if args.run:
            master_key = get_or_create_key()
            secure_massal(".", master_key)

        if args.restore:
            c = input("[!] Restore ALL files? (y/N): ").strip().lower()
            if c == 'y':
                master_key = get_or_create_key()
                restore_files(".", master_key)

        if args.status:
            cmd_status()

        if args.test:
            run_self_test()

        if args.stats:
            show_stats()

        if args.report:
            generate_threat_report()
    else:
        interactive_shell()

if __name__ == "__main__":
    main()
