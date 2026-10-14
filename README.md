# XRPL Balance Checker

A read-only Python script that looks up an XRP balance on the XRP Ledger, built with [xrpl-py](https://github.com/XRPLF/xrpl-py). **Testnet** is the default; **Mainnet** is opt-in.

Prefer the browser? The live web checker has separate Testnet and Mainnet pages: [b34n5x.github.io/checker](https://b34n5x.github.io/checker/).

## Run it

```
pip install xrpl-py
python balance.py            # Testnet (default)
python balance.py --mainnet  # Mainnet (real XRP, read-only)
```

Enter an address (starts with `r`) and it prints the balance in XRP. It only reads public data: no keys or seeds are used, and it never signs, submits or moves anything.

## Terms and disclaimer

Not legal, financial or tax advice. Provided as-is with no warranty, and the author accepts no liability for any losses, damages or disputes. Read-only: never asks for seeds or keys. See [TERMS.md](TERMS.md).

## Notes
Note: an internal Xaman support planning section appeared briefly in earlier commit history. It was a simple mistake made while learning project management, and it has been corrected and removed from the current version.
