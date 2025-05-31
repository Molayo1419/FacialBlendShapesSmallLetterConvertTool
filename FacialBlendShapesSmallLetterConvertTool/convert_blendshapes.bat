@echo off
set BLEND_FILE=%~1
if "%BLEND_FILE%"=="" (
    echo Usage: convert_blendshapes.bat [blender_file_path]
    echo Example: convert_blendshapes.bat "C:\path\to\your\file.blend"
    pause
    exit /b 1
)
echo Running Blender...
"C:\Program Files\Blender Foundation\Blender 4.2\blender.exe" --background --python convert_blendshapes.py -- "%BLEND_FILE%" 2>&1
if errorlevel 1 (
    echo Error occurred during execution.
    pause
    exit /b %errorlevel%
)
echo Process completed successfully.
pause 