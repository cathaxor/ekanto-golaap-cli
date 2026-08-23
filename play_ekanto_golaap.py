import sys, os, time, subprocess

sys.stdout.reconfigure(encoding='utf-8')

VIDEO_FILE = "YTDown.com_YouTube_Indalo-Ekanto-Golaap-OFFICIAL-LYRIC-VIDE_Media_pdxbOpEfr-U_001_1080p.mp4"
VIDEO_PATH = os.path.abspath(VIDEO_FILE)

MAGENTA = "\033[1;35m"
CYAN    = "\033[1;36m"
GREEN   = "\033[1;32m"
YELLOW  = "\033[1;33m"
RED     = "\033[1;31m"
PINK    = "\033[1;95m"
BLUE    = "\033[1;34m"
WHITE   = "\033[1;37m"
RESET   = "\033[0m"

LYRICS = [
    (0.0,    YELLOW, "~~ Music ~~"),
    (2.19,   GREEN,  "Tomar din kete jak chena kobitay"),
    (5.57,   CYAN,   "Kothao keu nei, tate ki ashe jay?"),
    (8.39,   PINK,   "Tumi tomar"),
    (11.24,  MAGENTA,"Ekanto priyo golaap"),
    (14.10,  BLUE,   "Tomar raat dube thak chena shunnotay"),
    (17.41,  CYAN,   "Chole jay jak, tate ki ashe jay?"),
    (20.29,  RED,    "Keu nei"),
    (23.21,  MAGENTA,"Pore thake eka golaap"),
    (39.32,  GREEN,  "Tomar golpera"),
    (42.30,  CYAN,   "Shesh hoy na jene"),
    (51.13,  PINK,   "Atke thake din"),
    (53.35,  BLUE,   "Cellphone ar shada ceiling-e"),
    (62.11,  GREEN,  "Tomar din kete jak chena kobitay"),
    (65.52,  CYAN,   "Kothao keu nei, tate ki ashe jay?"),
    (68.32,  PINK,   "Tumi tomar"),
    (71.05,  MAGENTA,"Ekanto priyo golaap"),
    (74.02,  BLUE,   "Tomar raat dube thak chena shunnotay"),
    (77.46,  CYAN,   "Chere jay jak, tate ki ashe jay?"),
    (80.20,  RED,    "Keu nei"),
    (83.09,  MAGENTA,"Pore thake eka golaap"),
    (87.0,   YELLOW, "~~ Guitar Solo ~~"),
    (107.75, GREEN,  "Tomar din kete jak kobitay"),
    (111.28, BLUE,   "Chirochena bishonnotay"),
    (114.39, PINK,   "Tumi tomar"),
    (116.95, PINK,   "Tumi tomar"),
    (119.84, BLUE,   "Tomar raat dube thak shunnotay"),
    (123.14, CYAN,   "Tomar golpe tumi"),
    (125.74, MAGENTA,"Shudhu tomar"),
    (131.94, GREEN,  "Amar din kete jak chena kobitay"),
    (135.38, CYAN,   "Kothao keu nei, tate ki ashe jay?"),
    (138.24, PINK,   "Ami amar"),
    (140.81, MAGENTA,"Ekanto priyo golaap"),
    (150.0,  YELLOW, "~~ Ekanto Golaap - Shesh ~~")
]

def play_audio():
    ps_code = f"""
    Add-Type -AssemblyName PresentationCore
    $player = New-Object System.Windows.Media.MediaPlayer
    $player.Open([System.Uri]"{VIDEO_PATH}")
    Start-Sleep -Milliseconds 500
    $player.Position = [System.TimeSpan]::FromSeconds(70)
    $player.Play()
    while ($player.Position.TotalSeconds -lt 280) {{
        Start-Sleep -Milliseconds 200
    }}
    """
    ps_file = os.path.join(os.path.dirname(VIDEO_PATH), "play_bg.ps1")
    with open(ps_file, "w", encoding="utf-8") as f:
        f.write(ps_code)

    proc = subprocess.Popen(
        ["powershell", "-ExecutionPolicy", "Bypass", "-NoProfile", "-File", ps_file],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    return proc, ps_file

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n  {MAGENTA}Indalo - Ekanto Golaap{RESET}\n  ----------------------\n")

    audio_proc, ps_file = play_audio()
    time.sleep(1.5)
    start = time.time()

    try:
        for offset, color, line in LYRICS:
            wait = (start + offset) - time.time()
            if wait > 0:
                time.sleep(wait)
            if "~~" in line:
                print(f"    {color}  {line}{RESET}", flush=True)
            else:
                print(f"    {color}> {line}{RESET}", flush=True)

    except KeyboardInterrupt:
        pass
    finally:
        try: audio_proc.terminate()
        except: pass
        try: os.remove(ps_file)
        except: pass
        print(f"\n  ----------------------\n  {MAGENTA}Gaan shesh! Dhonnobad!{RESET}\n")

if __name__ == "__main__":
    main()
