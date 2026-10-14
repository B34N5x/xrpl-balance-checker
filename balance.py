# XRPL Balance Checker - read-only. Testnet by default, Mainnet with --mainnet.
# Only ever asks for a PUBLIC address. Never enter a seed or secret key.
# It only reads public balances: it never signs, submits or moves anything.
import sys

from xrpl.clients import JsonRpcClient
from xrpl.core.addresscodec import is_valid_classic_address
from xrpl.models.requests import AccountInfo
from xrpl.utils import drops_to_xrp

NETWORKS = {
    "testnet": ("Testnet", ["https://s.altnet.rippletest.net:51234/", "https://testnet.xrpl-labs.com/"]),
    "mainnet": ("Mainnet", ["https://xrplcluster.com/", "https://s1.ripple.com:51234/"]),
}

network = "mainnet" if "--mainnet" in sys.argv[1:] else "testnet"
name, urls = NETWORKS[network]
if network == "mainnet":
    print("MAINNET: real XRP. Read-only balance lookup only.")

address = input(f"Enter a {name} XRP address (starts with r): ").strip()

if not is_valid_classic_address(address):
    if address.startswith("s"):
        print("That looks like a secret seed. Never share it with anyone or paste it into any tool.")
    print("That doesn't look like a valid XRP address. It should start with 'r'.")
    raise SystemExit(1)

resp = None
for url in urls:  # try each public server in turn
    try:
        resp = JsonRpcClient(url).request(AccountInfo(account=address, ledger_index="validated"))
        break
    except Exception:
        continue
if resp is None:
    print(f"Couldn't reach the XRPL {name} right now. Check your internet connection and try again.")
    raise SystemExit(1)

if resp.is_successful():
    drops = resp.result["account_data"]["Balance"]
    print("Balance:", drops_to_xrp(drops), "XRP")
else:
    print("Error:", resp.result.get("error_message", resp.result.get("error")))
