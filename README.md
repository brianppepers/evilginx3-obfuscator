BETA TESTING



# Evil-Reverse-Proxy-
A non-forked fork of EvilGophish.

# Evilginx3 JS Obfuscator + Injector

A modular toolkit to inject randomized, obfuscated `js_inject` payloads into Evilginx3 phishlet YAMLs. Supports campaign-level polymorphism for advanced phishing simulations.

## 🔧 Features

- Generates obfuscated JavaScript that steals session cookies
- Outputs YAML-compliant `js_inject` blocks for Evilginx3
- Automatically inserts or replaces them in any `.yaml` phishlet
- Maintains YAML indentation and structure
- Fully scriptable, fast, and stealthy

## 📁 Files

| File                      | Purpose |
|---------------------------|---------|
| `js_obfuscator_yaml.py`   | Generates YAML-ready `js_inject` block |
| `inject_obfuscated_js.sh` | Modifies Evilginx3 phishlet YAML in-place |
| `LICENSE`                 | MIT License |
| `README.md`               | You're reading it |

## 🚀 Usage

### 1. Generate & Inject Obfuscation

```bash
chmod +x inject_obfuscated_js.sh
./inject_obfuscated_js.sh /path/to/your/phishlet.yaml
```

### 2. Output Only YAML-Ready JS Block

```bash
python3 js_obfuscator_yaml.py > block.yaml
```

### 3. Restore Original

```bash
cp /path/to/your/phishlet.yaml.bak /path/to/your/phishlet.yaml
```

## 🧠 Requirements

- Python 3.x
- Bash-compatible shell

## 🔐 Ethical Use Only

This tool is provided for educational and authorized security testing use only. Do not use it for malicious purposes.

---

© 2025 KaliGPT | MIT License


---

## 📡 Optional: Run Cookie Receiver

To receive session tokens sent by the obfuscated JavaScript:

```bash
python3 evilfeed.py
```

The script listens on `/session_notify` and logs any received tokens.

### Example Output

```
[2025-06-16 20:20:00] Captured session tokens: SID=abc; HSID=xyz; ...
```

---


