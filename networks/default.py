from core.evm.flexible import FlexibleEvm

networks = [
    FlexibleEvm("sepolia", "Sepolia", "ETH", "ETHUSDT", "https://ethereum-sepolia-rpc.publicnode.com", "https://sepolia.etherscan.io/tx/"),
    FlexibleEvm("holesky", "Holesky", "ETH", "ETHUSDT", "https://ethereum-holesky-rpc.publicnode.com", "https://holesky.etherscan.io/tx/")
]