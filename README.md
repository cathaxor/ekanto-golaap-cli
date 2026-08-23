# Ekanto Golaap — CLI Lyric Player

<p align="center">

<img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows">
<img src="https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="MIT License">

</p>

<p align="center">
  <strong>A colorful Python CLI lyric player for Indalo — Ekanto Golaap.</strong>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#requirements">Requirements</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#customization">Customization</a> •
  <a href="#license">License</a>
</p>

---

## About

**Ekanto Golaap CLI** is a lightweight Python-based terminal lyric player created for **Indalo — Ekanto Golaap**.

The program plays the local media file in the background while displaying synchronized lyrics directly inside the terminal using ANSI colors.

The project is designed to be simple, lightweight, and easy to customize.

> This is an independent fan/educational project.

---

## Features

| Feature             | Description                                            |
| ------------------- | ------------------------------------------------------ |
| Terminal Lyrics     | Displays synchronized lyrics directly in the terminal  |
| Color Output        | Different colors can be assigned to lyric lines        |
| Background Playback | Plays the local media file through Windows MediaPlayer |
| Lightweight         | Uses only Python standard libraries                    |
| No Dependencies     | No `pip install` required                              |
| Windows Support     | Designed for Windows 10/11                             |
| Custom Timestamps   | Easily adjust lyric synchronization                    |
| Custom Colors       | Modify terminal colors from the source                 |
| Simple Setup        | Clone, add media, and run                              |

---

## Requirements

Before running the project, make sure you have:

* Windows 10 or Windows 11
* Python 3.9 or newer
* PowerShell
* A legally obtained local copy of the required media file

No external Python packages are required.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/cathaxor/ekanto-golaap-cli.git
```

Enter the project directory:

```bash
cd ekanto-golaap-cli
```

### 2. Download the Project Manually

Alternatively, download the repository as a ZIP file from GitHub and extract it.

---

## Media File Setup

The Python script expects the media file to be available in the same directory.

The default filename is:

```text
YTDown.com_YouTube_Indalo-Ekanto-Golaap-OFFICIAL-LYRIC-VIDE_Media_pdxbOpEfr-U_001_1080p.mp4
```

Your project directory should look like:

```text
ekanto-golaap-cli/
│
├── play_ekanto_golaap.py
├── README.md
├── LICENSE
├── .gitignore
└── YTDown.com_YouTube_Indalo-Ekanto-Golaap-OFFICIAL-LYRIC-VIDE_Media_pdxbOpEfr-U_001_1080p.mp4
```

### Important

The original media file is **not included in this repository**.

Users should provide their own legally obtained copy.

Do not upload copyrighted audio/video to the repository unless you have permission to redistribute it.

---

## Usage

Open **Command Prompt**, **PowerShell**, or **Windows Terminal** inside the project directory.

Run:

```bash
python play_ekanto_golaap.py
```

If your system uses the Python launcher:

```bash
py play_ekanto_golaap.py
```

The program will:

1. Clear the terminal.
2. Start the background media player.
3. Start the lyric timer.
4. Display each lyric according to its timestamp.
5. Stop playback after the lyrics finish.

---

## Terminal Preview

```text
  Indalo - Ekanto Golaap
  ----------------------

    ~~ Music ~~

    > Tomar din kete jak chena kobitay

    > Kothao keu nei, tate ki ashe jay?

    > Tumi tomar

    > Ekanto priyo golaap

    > Tomar raat dube thak chena shunnotay

    > Chole jay jak, tate ki ashe jay?

    > Keu nei

    > Pore thake eka golaap
```

---

## How It Works

The project uses Python's built-in modules to control the terminal and launch the Windows media player.

Main components:

```text
Python Script
     │
     ├── Lyrics & Timestamps
     │
     ├── Terminal Colors
     │
     ├── Timer Synchronization
     │
     └── PowerShell
            │
            └── Windows MediaPlayer
```

The project does not require external Python packages.

---

## Project Structure

```text
ekanto-golaap-cli/
│
├── play_ekanto_golaap.py
│   └── Main lyric player
│
├── README.md
│   └── Project documentation
│
├── LICENSE
│   └── MIT License
│
└── .gitignore
    └── Git ignored files
```

---

# Customization

## Edit Lyrics

Lyrics are stored inside the `LYRICS` list:

```python
LYRICS = [
    (2.19, GREEN, "Tomar din kete jak chena kobitay"),
    (5.57, CYAN, "Kothao keu nei, tate ki ashe jay?"),
]
```

Each entry follows this format:

```text
(timestamp, color, "lyric")
```

Example:

```python
(30.00, CYAN, "Your lyric here"),
(35.50, MAGENTA, "Another line"),
(40.20, GREEN, "Another lyric"),
```

The timestamp is measured in seconds.

---

## Adjust Lyric Timing

If a lyric appears too early or too late, modify its timestamp.

For example:

```python
(20.29, RED, "Keu nei")
```

To make it appear 0.5 seconds later:

```python
(20.79, RED, "Keu nei")
```

You can fine-tune each timestamp to match your media file.

---

## Terminal Colors

The script contains several predefined ANSI colors:

```python
MAGENTA = "\033[1;35m"
CYAN    = "\033[1;36m"
GREEN   = "\033[1;32m"
YELLOW  = "\033[1;33m"
RED     = "\033[1;31m"
PINK    = "\033[1;95m"
BLUE    = "\033[1;34m"
WHITE   = "\033[1;37m"
RESET   = "\033[0m"
```

Example:

```python
(20.29, RED, "Keu nei")
```

You can change `RED` to:

```text
GREEN
CYAN
YELLOW
MAGENTA
PINK
BLUE
WHITE
```

---

## Audio Start Position

The PowerShell player can start the media from a specific position.

Current configuration:

```powershell
$player.Position = [System.TimeSpan]::FromSeconds(70)
```

If your lyric timestamps are measured from the beginning of the song, use:

```powershell
$player.Position = [System.TimeSpan]::FromSeconds(0)
```

### Synchronization Rule

The audio start position and lyric timestamps must use the same reference point.

For example, if audio starts at `70` seconds but lyrics start at `0`, the displayed lyrics may not match the audio.

---

# Troubleshooting

## Python Is Not Recognized

If you see:

```text
'python' is not recognized as an internal or external command
```

Install Python and enable:

```text
Add Python to PATH
```

during installation.

Restart your terminal after installing Python.

Check the installation:

```bash
python --version
```

---

## Audio Does Not Play

Check the following:

* The MP4 exists in the project directory.
* The filename exactly matches `VIDEO_FILE`.
* PowerShell is available.
* Windows MediaPlayer components are available.
* You are running Windows.

---

## File Not Found

If you receive a file-related error, check:

```python
VIDEO_FILE = "your-file-name.mp4"
```

The filename must exactly match the media file.

For example:

```python
VIDEO_FILE = "song.mp4"
```

Then place:

```text
song.mp4
```

in the same directory as the Python script.

---

## Lyrics Are Out of Sync

First check the audio start position:

```powershell
$player.Position = [System.TimeSpan]::FromSeconds(0)
```

Then adjust the timestamps inside:

```python
LYRICS = [...]
```

Small timestamp changes can significantly improve synchronization.

---

## Terminal Colors Are Not Working

For the best experience, use:

* Windows Terminal
* PowerShell
* Windows 10/11 Command Prompt

Windows Terminal is recommended.

---

# Development

Clone the repository:

```bash
git clone https://github.com/cathaxor/ekanto-golaap-cli.git
cd ekanto-golaap-cli
```

Create a development branch:

```bash
git checkout -b feature/improvement
```

Make your changes and test:

```bash
python play_ekanto_golaap.py
```

Commit:

```bash
git add .
git commit -m "Improve lyric synchronization"
```

Push:

```bash
git push origin feature/improvement
```

Then open a Pull Request on GitHub.

---

# Contributing

Contributions are welcome.

You can contribute by:

* Improving synchronization
* Improving terminal UI
* Adding additional customization
* Fixing bugs
* Improving Windows compatibility
* Improving documentation

Please open an Issue before making major changes.

---

# License

This project is released under the **MIT License**.

The source code is open source and may be reused according to the terms of the license.

The song, lyrics, artwork, video, and other copyrighted materials remain the property of their respective copyright holders.

This repository does **not** distribute the original copyrighted media.

See the `LICENSE` file for the complete license text.

---

# Disclaimer

This project is an independent fan/educational project.

It is not affiliated with, sponsored by, or endorsed by **Indalo**, its members, record label, or any copyright holder.

Users are responsible for obtaining and using media legally.

---

# Author

<p align="center">

<strong>Abdur Rahaman Abdulla</strong>

<br>

<a href="https://www.instagram.com/abdulla_trzz/">
  <img src="https://img.shields.io/badge/Instagram-abdulla__trzz-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram">
</a>

</p>

---

# Support

If you find this project useful:

* Star the repository
* Fork the project
* Report bugs through GitHub Issues
* Submit improvements through Pull Requests

---

<p align="center">
  <sub>Created by Abdur Rahaman Abdulla</sub>
</p>

<p align="center">
  <sub>Built with Python and Windows PowerShell.</sub>
</p>
