#!/usr/bin/python3
from brownie import PriceExercise, MockV3Aggregator, LinkToken, MockOracle, config, network
from scripts.helpful_scripts import (
    get_account,
    get_verify_status,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_price_exercise():
    jobId = config["networks"][network.show_active()]["jobId"]
    fee = config["networks"][network.show_active()]["fee"]
    account = get_account()
    oracle = get_contract("oracle").address
    link_token = get_contract("link_token").address
    api_consumer = APIConsumer.deploy(
        oracle,
        jobId,
        fee,
        link_token,
        {"from": account},
        publish_source=get_verify_status(),
    )
    print(f"API Consumer deployed to {api_consumer.address}")
    return api_consumer



def main():
    deploy_api_consumer()