import aiohttp
from datetime import datetime


class PrivatApi:

    BASE_URL = "https://api.privatbank.ua/p24api/exchange_rates"

    async def get_rates(self, date: datetime):
        date_str = date.strftime("%d.%m.%Y")
        url = f"{self.BASE_URL}?json&date={date_str}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    raise RuntimeError(f"HTTP error {resp.status}")

                data = await resp.json()

        eur = next((c for c in data["exchangeRate"] if c.get("currency") == "EUR"), None)
        usd = next((c for c in data["exchangeRate"] if c.get("currency") == "USD"), None)

        return {
            date_str: {
                "EUR": {
                    "sale": eur.get("saleRate"),
                    "purchase": eur.get("purchaseRate"),
                },

                "USD": {
                    "sale": usd.get("saleRate"),
                    "purchase": usd.get("purchaseRate"),
                }
            }
        }
