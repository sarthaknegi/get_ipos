# get_ipos

Get the ipos listed on top exchanges with easy to use pacakge.

Exchanges Covered :-

- NYSE
- NASDAQ
- BSE
- NSEI
- Euronext
- LSE
- SEHK
- TSX
- TYO

## Prerequisites

Use the requirements.txt file to install the prerequisites

### Installing

Use pip to install the package

- pip install get_ipos

### Usage

```
from ipos import get_ipos

get = get_ipos(path to the chrome driver)

# Getting latest ipo listing from NYSE
nyse_listings = get.nyse()

```

## Contributing

PR to cover more exchanges and making the process faster.
