# XRPL Balance Checker - read-only, Testnet
from xrpl.clients import JsonRpcClient
from xrpl.models.requests import AccountInfo
from xrpl.utils import drops_to_xrp

client = JsonRpcClient("https://s.altnet.rippletest.net:51234/")
address = input("Enter a Testnet XRP address (starts with r): ").strip()

resp = client.request(AccountInfo(account=address, ledger_index="validated"))
if resp.is_successful():
    drops = resp.result["account_data"]["Balance"]
    print("Balance:", drops_to_xrp(drops), "XRP")
else:
    print("Error:", resp.result.get("error_message", resp.result.get("error")))
