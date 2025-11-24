import asyncio
from datetime import datetime, timedelta
from privat_api import PrivatApi


async def main():
    days = int(input("Введіть кількість днів (1–10): "))

    if not 1 <= days <= 10:
        print("Можна запросити лише останні 10 днів!")
        return

    api = PrivatApi()

    today = datetime.now()
    tasks = []

    for i in range(days):
        date = today - timedelta(days=i)
        tasks.append(api.get_rates(date))

    results = await asyncio.gather(*tasks)

    print(results)


if __name__ == "__main__":
    asyncio.run(main())
