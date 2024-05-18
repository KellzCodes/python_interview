import asyncio

class BatchFetcher:
    def __init__(self, database):
        self.database = database

    async def fetch_records(self, record_ids):
        pending_records = []
        for record_id in record_ids:
            pending_records.append(self.database.async_fetch(record_id))
        return await asyncio.gather(*pending_records)
