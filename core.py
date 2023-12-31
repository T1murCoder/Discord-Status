from pypresence import Presence
import time
import sys


def create_rpc(client_id: str):
    rpc = Presence(client_id)
    return rpc


def start_rpc(rpc: Presence):
    rpc.connect()


def update_rpc(rpc: Presence, state=None, details=None, large_image=None, large_text=None, small_image=None, small_text=None):
    rpc.update(state=state, details=details, large_image=large_image, large_text=large_text, small_image=small_image, small_text=small_text)


def close_rpc(rpc: Presence):
    rpc.close()


if __name__ == "__main__":
    client_id = "1131635406417449041"
    state = "test"
    details = "123"
    large_image = "https://media.tenor.com/Pl4WC5dd83UAAAAC/meme-memes.gif"
    small_image = "https://sun1-99.userapi.com/impf/c852128/v852128365/1d3bf6/Y9_SLDM9Vgk.jpg?size=2560x1714&quality=96&sign=05b468177bb38e2bd1efb5fde034835a&type=album"
    rpc = create_rpc(client_id)
    start_rpc(rpc)
    update_rpc(rpc, state=state, details=details, large_image=large_image, small_image=small_image)
    while True:
        time.sleep(1)
        t = input()
        if t == "stop":
            close_rpc(rpc)
            sys.exit(0)