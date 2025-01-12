import subprocess
import os

def obfuscate_js(js_code: str) -> str:
    try:
        # Menulis kode JavaScript ke dalam file sementara
        with open("temp.js", "w") as f:
            f.write(js_code)

        # Menentukan path ke skrip obfuscate.js
        obfuscate_script_path = os.path.join(os.getcwd(), "obfuscate.js")

        # Menjalankan skrip obfuscate.js dengan node
        output_file = "obfuscated_temp.js"
        result = subprocess.run(
            ["node", obfuscate_script_path, "temp.js", output_file],
            capture_output=True, text=True
        )

        # Membaca hasil obfuscate dari file output
        if result.returncode == 0:
            with open(output_file, "r") as f:
                return f.read()
        else:
            return f"Error: {result.stderr}"

    except Exception as e:
        return f"Error: {str(e)}"

# UI Streamlit
import streamlit as st

st.title('JavaScript Obfuscator')

input_code = st.text_area("Masukkan Kode JavaScript", height=300)

if st.button("Obfuscate"):
    if input_code:
        obfuscated_result = obfuscate_js(input_code)
        st.subheader("Hasil Obfuscate:")
        st.code(obfuscated_result, language="javascript")
    else:
        st.error("Masukkan kode JavaScript yang ingin diobfuscate.")
