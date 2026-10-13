# XRPL Balance Checker - read-only, Testnet
# Only ever asks for a PUBLIC address. Never enter a seed or secret key.
from xrpl.clients import JsonRpcClient
from xrpl.core.addresscodec import is_valid_classic_address
from xrpl.models.requests import AccountInfo
from xrpl.utils import drops_to_xrp

client = JsonRpcClient("https://s.altnet.rippletest.net:51234/")
address = input("Enter a Testnet XRP address (starts with r): ").strip()

if not is_valid_classic_address(address):
    if address.startswith("s"):
        print("That looks like a secret seed. Never share it with anyone or paste it into any tool.")
    print("That doesn't look like a valid XRP address. It should start with 'r'.")
    raise SystemExit(1)

try:
    resp = client.request(AccountInfo(account=address, ledger_index="validated"))
except Exception:
    print("Couldn't reach the XRPL Testnet right now. Check your internet connection and try again.")
    raise SystemExit(1)

if resp.is_successful():
    drops = resp.result["account_data"]["Balance"]
    print("Balance:", drops_to_xrp(drops), "XRP")
else:
    print("Error:", resp.result.get("error_message", resp.result.get("error")))
