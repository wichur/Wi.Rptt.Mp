# boot.py - - runs on boot-up
import ota
import secrets
from ota.ota_updater import OTAUpdater

def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/wichur/Wi.Rptt.Mp', main_dir='app', secrets_file="secrets.py")
    o.install_update_if_available_after_boot(
        secrets.WIFI_SSID, secrets.WIFI_PASSWORD)

def start():
    print('start')

def boot():
    download_and_install_update_if_available()
    start()

boot()