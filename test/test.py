from networks.default import networks

network = networks[0]

import asyncio

async def main():
    # print(await network.get_price())
    # print(await network.get_price())
    # print(await network.get_price())
    # print(await network.get_price())
    # print(await network.get_price())
    tx = await network.transfer('0x41B1E5677A615DbD27CeA14bfCd30E149F2bE4D5', 0.00001)


asyncio.run(main())
