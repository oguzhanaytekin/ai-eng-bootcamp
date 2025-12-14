@echo off
echo 🚀 Sunucu Baslatiliyor Kral...
cd day14fastapi
python -m uvicorn api:app --reload
pause