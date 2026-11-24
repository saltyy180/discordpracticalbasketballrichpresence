import os
import sys
import time
import random
import warnings
from pypresence import Presence

os.system("")
warnings.filterwarnings("ignore")

CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

CLIENT_ID = "YOUR_CLIENT_ID_HERE"
IMAGE_KEY = "pbthumbnail"

print(f"PRACTICAL BASKETBALL DEMON RPC{RESET}")

try:
    fake_offset = random.randint(172800, 345600)
    rpc = Presence(CLIENT_ID)
    rpc.connect()
    rpc.update(
        details="LOOKING FOR VICTIMS",
        state="1V1 IF U WANT TO SUFFER",
        large_image=IMAGE_KEY,
        large_text="PRACTICAL BASKETBALL DEMON",
        start=int(time.time()) - fake_offset,
        party_id="pbd_lobby_1",
        party_size=[1, 2],
        join="pbd_join_secret_123"
    )
    print(f"{GREEN}[LIVE]{RESET}")

    while True:
        time.sleep(15)

except KeyboardInterrupt:
    try:
        rpc.clear()
        rpc.close()
    except Exception:
        pass
    print(f"\n{RED}Stopped{RESET}")
    sys.stdout.flush()
    os._exit(0)
