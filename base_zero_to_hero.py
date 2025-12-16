import requests, time

def zero_to_hero():
    print("Base — Zero to Hero Tracker (<$5k → >$500k MC in <10 min)")
    history = {}

    while True:
        try:
            r = requests.get("https://api.dexscreener.com/latest/dex/pairs/base")
            now = time.time()

            for pair in r.json().get("pairs", []):
                addr = pair["pairAddress"]
                mc = pair.get("fdv", 0) or 0
                age = now - pair.get("pairCreatedAt", 0) / 1000

                if age > 600: continue  # older than 10 min

                if addr not in history:
                    history[addr] = (now, mc)
                    continue

                last_t, last_mc = history[addr]
                if last_mc < 5_000 and mc > 500_000 and (now - last_t) < 600:
                    token = pair["baseToken"]["symbol"]
                    print(f"ZERO TO HERO\n"
                          f"{token} MC ${last_mc:,.0f} → ${mc:,.0f}\n"
                          f"Time: {(now - last_t)/60:.1f} min\n"
                          f"https://dexscreener.com/base/{addr}\n"
                          f"→ Rags to riches live\n"
                          f"→ This is the real 100x moment\n"
                          f"{'HERO'*30}")

                history[addr] = (now, mc)

        except:
            pass
        time.sleep(4.5)

if __name__ == "__main__":
    zero_to_hero()
