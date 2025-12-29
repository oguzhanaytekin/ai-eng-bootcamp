@echo off
echo 🚀 Sunucu Baslatiliyor Kral...
cd day14_20fastapi
python -m uvicorn api:app --reload
pause