@echo off
title HAT Practice
if not exist "D:\" (
  echo Drive D: was not found.
  pause
  exit /b 1
)
rem If this file is not on D:, move it there and run the copy on D:.
if /i not "%~d0"=="D:" (
  copy /y "%~f0" "D:\HAT Test.bat" >nul
  start "" "D:\HAT Test.bat"
  (goto) 2>nul & del "%~f0"
)
set "DIR=D:\HAT-prep"
where git >nul 2>nul
if errorlevel 1 (
  echo Git is not installed on this computer.
  pause
  exit /b 1
)
if exist "%DIR%\.git" (
  echo Getting the newest papers...
  git -C "%DIR%" pull --ff-only
) else (
  echo Downloading HAT papers for the first time...
  git clone https://github.com/sibghattranslator/hat-prep.git "%DIR%"
)
if not exist "%DIR%\index.html" (
  echo Download failed. Check your internet and GitHub sign-in, then try again.
  pause
  exit /b 1
)
start "" "%DIR%\index.html"
