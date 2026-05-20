import json
import re

with open('templates/base.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the JSON object inside tailwind.config = {...}
match = re.search(r'tailwind\.config\s*=\s*(\{.*?\})', html, re.DOTALL)
if match:
    config_str = match.group(1)
    
    # It's a JS object, not strict JSON, but it looks like it uses double quotes for keys.
    # Let's just output it as a JS module
    js_content = "/** @type {import('tailwindcss').Config} */\n"
    js_content += "module.exports = " + config_str + ";\n"
    js_content = js_content.replace('module.exports = {', 'module.exports = {\n  content: ["./templates/**/*.html"],')
    
    # Add plugins
    js_content = js_content.replace('}', '},\n  plugins: [\n    require("@tailwindcss/forms"),\n    require("@tailwindcss/container-queries")\n  ]\n}')
    
    with open('tailwind.config.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("tailwind.config.js generated.")
else:
    print("Could not find tailwind config.")
