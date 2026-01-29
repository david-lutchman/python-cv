#!/bin/bash

echo "============================================"
echo "Python Resume Generator - macOS Setup"
echo "============================================"

# Check for Homebrew
if ! command -v brew >/dev/null 2>&1; then
  echo "Homebrew not found. Installing Homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

  if [ $? -ne 0 ]; then
    echo "Homebrew installation failed."
    exit 1
  fi
else
  echo "Homebrew already installed."
fi

# Check for Python
if ! command -v python3 >/dev/null 2>&1; then
  echo "Installing Python..."
  brew install python
else
  echo "Python already installed."
fi

echo "Installing Python dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install reportlab

if [ $? -ne 0 ]; then
  echo "Failed to install Python dependencies."
  exit 1
fi

echo "============================================"
echo "Setup complete."
echo "You can now run: python3 generate_resume.py"
echo "============================================"
