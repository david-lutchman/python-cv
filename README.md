# ATS-Friendly Resume Generator (Python)

This repository contains a Python-based resume generator that produces an **ATS-friendly PDF** using ReportLab.

The resume content is maintained directly in code, making it version-controlled, portable, and easy to tailor for different roles or markets without relying on Word or GUI-based editors.

The output PDF uses:
- Standard fonts
- Plain text (no tables or graphics)
- Simple layout optimized for applicant tracking systems

---

## Features

- Generates a clean, searchable PDF resume
- ATS-safe formatting (no columns, tables, icons, or images)
- Easily customizable resume content via Python variables
- Cross-platform support (Windows and macOS)
- One-command setup scripts for dependency installation
- Suitable for enterprise, hospitality, MSP, and security roles

---

## Requirements

- Python 3.10 or later
- ReportLab

If Python is not installed, the setup scripts will install it automatically.

---

## Setup

### Windows

1. Open a Command Prompt as a standard user
2. Run:
setup_windows.bat

This will:
- Install Python (if not already present)
- Add Python to PATH
- Install required Python packages

---

### macOS

1. Open Terminal
2. Make the setup script executable:
chmod +x setup_mac.sh
3. Run:
./setup_mac.sh

This will:
- Install Homebrew (if missing)
- Install Python
- Install required Python packages

---

## Usage

After setup, generate the resume PDF by running:

### Windows
python generate_resume.py

### macOS
python3 generate_resume.py

The output file will be created in the project directory:
david-lutchman-2026.pdf

---

## Customization

All resume content is defined inside `generate_resume.py`.

You can easily modify:
- Professional summary
- Skills
- Job experience
- Projects
- Certifications

This approach allows:
- Easy tailoring for specific job applications
- Clean version control via Git
- Repeatable builds with no formatting drift

---

## Design Principles

- ATS compatibility over visual design
- Plain text over layout tricks
- Automation over manual editing
- Portability across systems

This is intentional.

---

## License

This project is provided for personal and professional use.  
No warranty is expressed or implied.

---

## Notes

This repository is meant to demonstrate:
- Practical Python usage
- Automation mindset
- Attention to real-world constraints (ATS systems)

Resume content is provided as sample data and can be replaced with user-specific content.
It is not intended to be a resume template for non-technical users.
