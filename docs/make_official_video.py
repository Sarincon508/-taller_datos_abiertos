import os
import subprocess
import time

ADB = r"F:\Android\Sdk\platform-tools\adb.exe"
OUTPUT_DIR = r"F:\Users\Max\Desktop\moviles\taller 4\docs"
SCREENSHOTS_DIR = os.path.join(OUTPUT_DIR, "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

def adb(cmd):
    return subprocess.run(f'"{ADB}" {cmd}', shell=True, capture_output=True, text=True).stdout.strip()

def tap(x, y, wait=1.5):
    adb(f"shell input tap {x} {y}")
    time.sleep(wait)

def swipe(x1, y1, x2, y2, duration=500, wait=1.5):
    adb(f"shell input swipe {x1} {y1} {x2} {y2} {duration}")
    time.sleep(wait)

def type_text(text, wait=1.5):
    adb(f'shell input text "{text}"')
    time.sleep(wait)

def back_appbar(wait=1.5):
    adb("shell input tap 70 85")
    time.sleep(wait)

def screenshot(name):
    remote = f"/sdcard/{name}.png"
    local = os.path.join(SCREENSHOTS_DIR, f"{name}.png")
    adb(f"shell screencap -p {remote}")
    adb(f'pull {remote} "{local}"')
    print(f"Captured: {name}")

def ensure_dashboard():
    # Bring to foreground and ensure at top of dashboard
    adb("shell am start -n com.example.taller_datos_abiertos.taller_datos_abiertos/.MainActivity")
    time.sleep(1)
    # If on a child page, tap back arrow a few times
    back_appbar(0.5)
    back_appbar(0.5)
    # Scroll all the way to top of dashboard
    swipe(540, 600, 540, 2000, 400, 1)

def record():
    ensure_dashboard()

    print("[*] Iniciando grabación de video oficial...")
    # Start screenrecord: 720x1600, 4Mbps, max 180s
    rec = subprocess.Popen(
        f'"{ADB}" shell screenrecord --size 720x1600 --bit-rate 4500000 --time-limit 180 /sdcard/video_taller_colombia.mp4',
        shell=True
    )
    time.sleep(2)

    # ================= 1. DASHBOARD =================
    print("[1] Grabando Dashboard...")
    screenshot("01_dashboard_principal")
    time.sleep(2)
    # Scroll down to show all 4 cards
    swipe(540, 1800, 540, 700, 700, 2)
    screenshot("01_dashboard_inferior")
    time.sleep(1.5)
    # Scroll back to top
    swipe(540, 700, 540, 1800, 700, 2)

    # ================= 2. DEPARTAMENTOS =================
    print("[2] Grabando Departamentos...")
    tap(540, 1150, 2.5) # Clic en card Departamentos
    screenshot("02_departamentos_listado")
    time.sleep(1.5)
    # Scroll list
    swipe(540, 1700, 540, 900, 600, 2)
    swipe(540, 900, 540, 1700, 600, 1.5)
    # Tap first department
    tap(540, 650, 2.5) # Abre Detalle de Departamento
    screenshot("03_departamento_detalle")
    time.sleep(1.5)
    swipe(540, 1700, 540, 1000, 600, 2) # Scroll en detalle
    back_appbar(1.5) # Regresar a listado
    back_appbar(1.5) # Regresar a dashboard

    # ================= 3. ATRACCIONES TURÍSTICAS =================
    print("[3] Grabando Atracciones Turísticas...")
    # Scroll slightly down so card 2 is centered
    swipe(540, 1400, 540, 800, 500, 1.5)
    tap(540, 650, 2.5) # Clic en Atracciones Turísticas
    screenshot("04_atracciones_listado")
    time.sleep(1.5)
    swipe(540, 1700, 540, 900, 600, 2) # Scroll list
    # Tap second attraction with image
    tap(540, 1200, 2.5) # Abre Detalle de Atracción
    screenshot("05_atraccion_detalle")
    time.sleep(1.5)
    swipe(540, 1700, 540, 1000, 600, 2) # Scroll en detalle
    back_appbar(1.5) # Regresa a listado
    back_appbar(1.5) # Regresa a dashboard

    # ================= 4. PRESIDENTES =================
    print("[4] Grabando Presidentes...")
    # Scroll down to reveal Presidentes and Platos Típicos
    swipe(540, 1800, 540, 800, 600, 1.5)
    tap(540, 1100, 2.5) # Clic en Presidentes
    screenshot("06_presidentes_listado")
    time.sleep(1.5)
    swipe(540, 1700, 540, 900, 600, 2) # Scroll list
    tap(540, 650, 2.5) # Clic en un presidente
    screenshot("07_presidente_detalle")
    time.sleep(1.5)
    swipe(540, 1700, 540, 1000, 600, 2) # Scroll en biografía
    back_appbar(1.5) # Regresa a listado
    back_appbar(1.5) # Regresa a dashboard

    # ================= 5. PLATOS TÍPICOS =================
    print("[5] Grabando Platos Típicos...")
    swipe(540, 1800, 540, 800, 600, 1.5)
    tap(540, 1800, 2.5) # Clic en Platos Típicos
    screenshot("08_platos_tipicos_listado")
    time.sleep(1.5)
    swipe(540, 1700, 540, 1000, 600, 2) # Scroll list
    tap(540, 650, 2.5) # Clic en Bandeja Paisa
    screenshot("09_plato_tipico_detalle")
    time.sleep(1.5)
    swipe(540, 1700, 540, 1000, 600, 2) # Scroll en ingredientes y origen
    back_appbar(1.5) # Regresa a listado
    back_appbar(1.5) # Regresa a dashboard

    # ================= 6. ACERCA DE Y CIERRE =================
    print("[6] Mostrando Acerca de...")
    swipe(540, 800, 540, 1800, 600, 1.5) # Scroll back to top
    tap(990, 85, 2) # Clic icono Info
    screenshot("10_modal_acerca_de")
    time.sleep(2)
    tap(540, 1400, 2) # Clic en 'Entendido'
    time.sleep(2)

    print("[*] Deteniendo grabación...")
    adb("shell pkill -2 screenrecord")
    time.sleep(3)
    rec.terminate()

    # Descargar video
    video_remote = "/sdcard/video_taller_colombia.mp4"
    video_local = os.path.join(OUTPUT_DIR, "video_demostracion.mp4")
    print(f"[*] Transfiriendo video a {video_local}...")
    adb(f'pull {video_remote} "{video_local}"')

    if os.path.exists(video_local):
        size = os.path.getsize(video_local) / (1024 * 1024)
        print(f"[SUCCESS] Video oficial grabado: {video_local} ({size:.2f} MB)")
    else:
        print("[ERROR] No se pudo transferir el video.")

if __name__ == "__main__":
    record()
