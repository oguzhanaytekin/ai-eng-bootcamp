@echo off
echo 🚀 Sunucu Baslatiliyor Kral...
cd day14_17fastapi
python -m uvicorn api:app --reload
pause