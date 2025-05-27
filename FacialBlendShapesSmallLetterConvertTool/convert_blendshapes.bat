@echo off
set BLEND_FILE=%~1
if "%BLEND_FILE%"=="" (
    echo 사용법: convert_blendshapes.bat [블렌더파일경로]
    exit /b 1
)
echo Blender 실행 중...
"C:\Program Files\Blender Foundation\Blender 4.2\blender.exe" --background --python convert_blendshapes.py -- "%BLEND_FILE%" 2>&1
if errorlevel 1 (
    echo 오류가 발생했습니다.
    pause
) 