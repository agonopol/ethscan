#!/usr/bin/env python

import click
from ethinjest import status
from ethinjest.model import session
from ethinjest.util import chunkify
from multiprocessing import Pool

ETHERSCAN_DB = 'sqlite:///ethscan.db'
CPUS = 5


@click.group()
def ethinjest():
    pass


@ethinjest.command()
@click.argument('address', type=click.STRING, default='0x742d35Cc6634C0532925a3b844Bc454e4438f44e')
def fetch(address):
    print(status(address).__repr__())


def update(addresses):
    sql = session(ETHERSCAN_DB)
    for address in addresses:
        try:
            update = status(address)
            sql.add(update)
        except Exception as e:
            print(e)
    sql.commit()


@ethinjest.command()
@click.argument('addresses', type=click.File('r'))
def injest(addresses):
    # Start session and create database
    session(ETHERSCAN_DB)
    pool = Pool(CPUS)

    # Spawn a multiprocessing pool to do 5 requests at a time
    # Chunk the addresses into 5 lists so as to minimize banging on the sql
    queue = chunkify([address.strip() for address in addresses], CPUS)
    pool.map(update, queue)


if __name__ == '__main__':
    ethinjest()
