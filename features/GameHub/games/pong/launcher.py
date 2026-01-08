import webview
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_dir, "index.html")

window = webview.create_window("Pong", html_path)
webview.start()
"""
© 2026 Lakshya.  
Licensed under CC BY-NC 4.0.  
https://creativecommons.org/licenses/by-nc/4.0/
"""
