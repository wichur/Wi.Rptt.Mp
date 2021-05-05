# boot.py - - runs on boot-upxxx
import app
import app.secrets as secrets
from app.ota_updater import OTAUpdater

def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/wichur/Wi.Rptt.Mp', github_src_dir='src', main_dir='app', secrets_file="secrets.py")
    o.install_update_if_available_after_boot(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)

def start():
    print('start')

def boot():
    download_and_install_update_if_available()
    start()

boot()