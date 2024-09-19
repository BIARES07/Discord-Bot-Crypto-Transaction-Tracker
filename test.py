import asyncio
from blockcypher import get_transaction_details

async def get_transaction_info(tx_hash, api_key):
    loop = asyncio.get_event_loop()
    tx_details = await loop.run_in_executor(None, get_transaction_details, tx_hash, 'ltc', api_key)

    # Get the date and time of the transaction
    date_time = tx_details.get('received', 'Date and time not available')

    # Get the number of confirmations
    confirmations = tx_details.get('confirmations', 0)

    # Check if the transaction is confirmed
    if confirmations > 3:
        status = 'Confirmed'
    else:
        status = 'Pending'

    return date_time, status, confirmations






