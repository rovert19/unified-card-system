from services.dispenser import DispenserPerson

import asyncio

# api


async def main():
    dispenser = DispenserPerson()
    card = await dispenser.get_card(init_charge=10.0)
    print(card)


asyncio.run(main())
