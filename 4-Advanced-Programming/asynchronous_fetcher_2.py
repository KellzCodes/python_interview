import asyncio


class BatchFetcher:
    def __init__(self, database):
        self.database = database

    async def fetch_records(self, record_ids):
        pending_records = []
        for record_id in record_ids:
            task = asyncio.create_task(self.database.async_fetch(record_id))
            pending_records.append(task)

        records = []
        for pending_record in pending_records:
            records.append(await pending_record)

        return records
