@echo off
title HAT Practice
set "DIR=%USERPROFILE%\HAT-prep"
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
  git clone https://github.com/sibghattranslator/HAT-prep.git "%DIR%"
)
if not exist "%DIR%\index.html" (
  echo Download failed. Check your internet and GitHub sign-in, then try again.
  pause
  exit /b 1
)
start "" "%DIR%\index.html"
