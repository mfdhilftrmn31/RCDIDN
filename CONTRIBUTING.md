# Contributing to RCDIDN

**Radioactive Cognitive Data Indonesia — Hacker Killer**
Created by Muhamad Fadhil Faturohman

Thank you for your interest in contributing! RCDIDN is a research-grade active defense system with 9 novel contributions to honeypot science. Every contribution helps push this research further.

---

## How You Can Help

### 🔬 Research Contributions (highest impact)
The most valuable thing you can do: **deploy RCDIDN on a real server and share your data**.

- Run RCDIDN for 30+ days and share anonymized PHANTOM CLOCK logs
- Contribute attacker session data for the MINDPRINT behavioral study
- Help build the first public LLM dwell-time dataset

### 🛠 Code Contributions
- Bug fixes and security hardening
- New LLM provider support (currently: Gemini, OpenAI, Claude, DeepSeek)
- Windows / macOS compatibility improvements
- Performance optimizations for high-traffic servers
- New honeypot port types

### 📖 Documentation
- Translations (English → Bahasa Indonesia and vice versa)
- Tutorial videos or blog posts
- Use case writeups

### 🧪 Testing
- Run `python3 rcdidn.py --test` and report failures
- Test on different OS versions (Ubuntu, Debian, CentOS, Windows, macOS)
- Stress test the honeypot with controlled scanner tools in lab environments

---

## Getting Started

```bash
git clone https://github.com/[username]/rcdidn
cd rcdidn
pip install cryptography
python3 rcdidn.py --test   # run self-test suite first
```

---

## Ground Rules

1. **Attribution stays.** The name *Muhamad Fadhil Faturohman* and *RCDIDN V1.0* must remain visible per MIT License terms.
2. **No offensive features.** RCDIDN is strictly defensive. PRs that add active attack capabilities will not be merged.
3. **Security first.** If you find a vulnerability, email muhamadfadhilfaturohman@gmail.com privately before opening a public issue.
4. **One PR, one change.** Keep pull requests focused — easier to review and merge.

---

## Reporting Bugs

Open a GitHub Issue with:
- OS and Python version
- The command you ran
- Full error output (censor any API keys)

---

## Contact

**Muhamad Fadhil Faturohman**
muhamadfadhilfaturohman@gmail.com

*"Every server touched by RCDIDN becomes a research laboratory."*
