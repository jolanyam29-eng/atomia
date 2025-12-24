import os
import streamlit as st
from openai import OpenAI
import streamlit.components.v1 as components
import tempfile

# ================== OpenAI ==================
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Atomia", layout="wide")

# ================== Logo + Title ==================
components.html("""
<div style="display:flex; align-items:center; gap:14px; margin:10px 0 6px 0;">
  <div class="logo-nucleus"></div>
  <div style="font-size:34px; font-weight:800; color:#f2f2f2;">
    🤖 الذرة الذكية <span style="color:#7aa7ff;">Atomia</span>
  </div>
</div>

<style>
.logo-nucleus{
  width:54px; height:54px; border-radius:50%;
  background: radial-gradient(circle at 30% 30%, #ffd1d1, #ff3b3b 55%, #a80000 100%);
  box-shadow: 0 0 18px rgba(255, 60, 60, 0.55);
  border: 1px solid rgba(255,255,255,0.20);
}
</style>
""", height=80)

st.write("مرحبًا 👋 أنا الذرة الذكية. اسأليني عن الذرة والكيمياء .")

# ================== سؤال المستخدم ==================
question = st.text_input("💬 اسألي الذرة:")

if "last_answer" not in st.session_state:
    st.session_state.last_answer = ""

if st.button("اسأل") and question.strip():
    with st.spinner("Atomia تفكر..."):
        resp = client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {
                    "role": "system",
                    "content": "أنتِ Atomia، ذرة ذكية تشرح لطالبات الثانوي الكيمياء بأسلوب بسيط ومختصر مع مثال واحد."
                },
                {"role": "user", "content": question},
            ],
        )
        st.session_state.last_answer = resp.output_text

    st.subheader("🧪 تقول الذرة:")
    st.write(st.session_state.last_answer)

# ================== الصوت ==================
st.divider()
st.subheader("🎙️ اسمعي الإجابة")

if st.session_state.last_answer.strip():
    if st.button("🔊 شغّل الصوت"):
        with st.spinner("جاري توليد الصوت..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                audio_path = tmp.name

            # يولد mp3 ويحفظه مباشرة
            with client.audio.speech.with_streaming_response.create(
                model="gpt-4o-mini-tts",
                voice="nova",
                input=st.session_state.last_answer,
            ) as response:
                response.stream_to_file(audio_path)

            st.audio(audio_path, format="audio/mp3")
else:
    st.info("اسألي سؤال أولًا، وبعدها تقدري تشغّلي الصوت.")

# ================== الذرة ثلاثية الأبعاد ==================
st.divider()
st.subheader("⚛️ نموذج الذرة التفاعلي")

html_code = """
<!DOCTYPE html>
<html>
<head>
  <style> body { margin: 0; } </style>
</head>
<body>
<script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"></script>
<script>
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, 600/400, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(600, 400);
document.body.appendChild(renderer.domElement);

// نواة
const nucleusGeometry = new THREE.SphereGeometry(1, 32, 32);
const nucleusMaterial = new THREE.MeshStandardMaterial({ color: 0xff3333 });
const nucleus = new THREE.Mesh(nucleusGeometry, nucleusMaterial);
scene.add(nucleus);

// ضوء
const light = new THREE.PointLight(0xffffff, 1);
light.position.set(5, 5, 5);
scene.add(light);

// إلكترونات
const electrons = [];
const radius = 3;

for (let i = 0; i < 3; i++) {
  const eGeo = new THREE.SphereGeometry(0.3, 32, 32);
  const eMat = new THREE.MeshStandardMaterial({ color: 0x3399ff });
  const electron = new THREE.Mesh(eGeo, eMat);
  scene.add(electron);
  electrons.push({ mesh: electron, angle: i * 2 });
}

camera.position.z = 8;

function animate() {
  requestAnimationFrame(animate);

  electrons.forEach((e, i) => {
    e.angle += 0.01;
    e.mesh.position.x = radius * Math.cos(e.angle);
    e.mesh.position.z = radius * Math.sin(e.angle);
  });

  renderer.render(scene, camera);
}
animate();
</script>
</body>
</html>
"""

components.html(html_code, height=420)
