docker compose down
docker rmi $(docker images -q "lan-chain-lanchain1")
docker rmi $(docker images -q "lan-chain-lanchain2")
docker rmi $(docker images -q "lan-chain-lanchain3")
docker compose up