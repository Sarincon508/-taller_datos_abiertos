import os
import subprocess
import time

ADB = r"F:\Android\Sdk\platform-tools\adb.exe"
OUTPUT_DIR = r"F:\Users\Max\Desktop\moviles\taller 4\docs"
SCREENSHOTS_DIR = os.path.join(OUTPUT_DIR, "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

def run_adb(cmd):
    full_cmd = f'"{ADB}" {cmd}'
    res = subprocess.run(full_cmd, shell=True, capture_output=True, text=True)
    return res.stdout.strip()

def tap(x, y):
    run_adb(f"shell input tap {x} {y}")
    time.sleep(1.2)

def swipe(x1, y1, x2, y2, duration=400):
    run_adb(f"shell input swipe {x1} {y1} {x2} {y2} {duration}")
    time.sleep(1.2)

def back():
    run_adb("shell input keyevent 4")
    time.sleep(1.2)

def take_screenshot(name):
    remote = f"/sdcard/{name}.png"
    local = os.path.join(SCREENSHOTS_DIR, f"{name}.png")
    run_adb(f"shell screencap -p {remote}")
    run_adb(f'pull {remote} "{local}"')
    print(f"[+] Screenshot guardado: {local}")

def main():
    print("[*] Iniciando grabación de video con screenrecord...")
    # Iniciar grabación en background (720x1600 para alta calidad y tamaño ligero)
    rec_proc = subprocess.Popen(
        f'"{ADB}" shell screenrecord --size 720x1600 --bit-rate 4000000 --time-limit 180 /sdcard/demo_colombia.mp4',
        shell=True
    )
    time.sleep(2)

    # 1. Dashboard Inicial
    print("[1/5] Mostrando Dashboard...")
    take_screenshot("01_dashboard")
    time.sleep(2)

    # Scroll hacia abajo en Dashboard para mostrar los 4 módulos
    swipe(540, 1800, 540, 800, 600)
    time.sleep(1.5)
    take_screenshot("01_dashboard_scrolled")
    time.sleep(1)

    # Scroll de vuelta arriba
    swipe(540, 800, 540, 1800, 600)
    time.sleep(1.5)

    # 2. Departamentos
    print("[2/5] Entrando a Departamentos...")
    tap(540, 1150) # Clic en card Departamentos
    time.sleep(2)
    take_screenshot("02_departamentos_list")

    # Scroll en lista de departamentos
    swipe(540, 1600, 540, 1000, 500)
    time.sleep(1.5)

    # Clic en un departamento (primer o segundo elemento visible)
    tap(540, 800)
    time.sleep(2)
    take_screenshot("03_departamento_detalle")

    # Scroll en detalle
    swipe(540, 1600, 540, 900, 500)
    time.sleep(2)
    back() # Regresar a lista
    time.sleep(1.5)
    back() # Regresar a dashboard
    time.sleep(1.5)

    # 3. Atracciones Turísticas
    print("[3/5] Entrando a Atracciones Turísticas...")
    tap(540, 1750) # Clic en card Atracciones Turísticas
    time.sleep(2.5)
    take_screenshot("04_atracciones_list")

    # Scroll en lista de atracciones
    swipe(540, 1600, 540, 900, 500)
    time.sleep(1.5)

    # Clic en detalle de atracción
    tap(540, 900)
    time.sleep(2)
    take_screenshot("05_atraccion_detalle")

    # Scroll en detalle
    swipe(540, 1600, 540, 900, 500)
    time.sleep(2)
    back()
    time.sleep(1.5)
    back()
    time.sleep(1.5)

    # 4. Presidentes
    print("[4/5] Entrando a Presidentes...")
    swipe(540, 1800, 540, 800, 500) # Scroll down on dashboard
    time.sleep(1.5)
    tap(540, 1000) # Clic en card Presidentes
    time.sleep(2.5)
    take_screenshot("06_presidentes_list")

    # Scroll en lista de presidentes
    swipe(540, 1600, 540, 900, 500)
    time.sleep(1.5)

    # Clic en un presidente
    tap(540, 850)
    time.sleep(2)
    take_screenshot("07_presidente_detalle")

    # Scroll en biografía
    swipe(540, 1600, 540, 900, 500)
    time.sleep(2)
    back()
    time.sleep(1.5)
    back()
    time.sleep(1.5)

    # 5. Platos Típicos
    print("[5/5] Entrando a Platos Típicos...")
    swipe(540, 1800, 540, 800, 500) # Scroll down on dashboard
    time.sleep(1.5)
    tap(540, 1700) # Clic en card Platos Típicos
    time.sleep(2.5)
    take_screenshot("08_platos_tipicos_list")

    # Scroll en lista de platos
    swipe(540, 1600, 540, 900, 500)
    time.sleep(1.5)

    # Clic en un plato típico
    tap(540, 750)
    time.sleep(2)
    take_screenshot("09_plato_tipico_detalle")

    # Scroll en detalle del plato
    swipe(540, 1600, 540, 900, 500)
    time.sleep(2)
    back()
    time.sleep(1.5)
    back()
    time.sleep(1.5)

    # Regresar arriba en dashboard y mostrar diálogo Acerca de
    swipe(540, 800, 540, 1800, 500)
    time.sleep(1)
    tap(990, 170) # Icono info del AppBar
    time.sleep(1.5)
    take_screenshot("10_acerca_de_dialog")
    tap(540, 1400) # Cerrar diálogo ("Entendido")
    time.sleep(2)

    print("[*] Finalizando grabación de video...")
    run_adb("shell pkill -2 screenrecord")
    time.sleep(3)
    rec_proc.terminate()

    video_remote = "/sdcard/demo_colombia.mp4"
    video_local = os.path.join(OUTPUT_DIR, "video_demostracion.mp4")
    print(f"[*] Descargando video a {video_local}...")
    run_adb(f'pull {video_remote} "{video_local}"')

    if os.path.exists(video_local):
        size_mb = os.path.getsize(video_local) / (1024 * 1024)
        print(f"[V] Video grabado exitosamente: {video_local} ({size_mb:.2f} MB)")
    else:
        print("[!] No se pudo descargar el video.")

if __name__ == "__main__":
    main()
