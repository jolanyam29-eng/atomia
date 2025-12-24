# Atomia (Streamlit)

## تشغيل محليًا
1) ثبتي Python 3.10+
2) ثبتي المتطلبات:
```bash
pip install -r requirements.txt
```
3) ضعي المفتاح كـ Environment Variable باسم `OPENAI_API_KEY`

Windows (PowerShell):
```powershell
setx OPENAI_API_KEY "sk-xxxx"
```
ثم افتحي تيرمنال جديد.

4) شغّلي:
```bash
streamlit run app.py
```

## نشر كرابط (Streamlit Community Cloud)
- ارفعي الملفات إلى GitHub (بدون أي API key)
- في Streamlit Cloud:
  - New app → اختاري الريبو → Main file: app.py
  - App settings → Secrets:
```toml
OPENAI_API_KEY = "sk-xxxx"
```
