from pymongo import MongoClient, ReturnDocument

from src.util.logger import log
from src.variables import db_host, db_port
from src.exception.base import DataBaseError, RpaException, RecordNotFoundException


def create_connection(data_base, collection):
    try:
        client = MongoClient(db_host, db_port)
        connection = client[data_base]
        return connection[collection]
    except Exception as ex:
        log(ex)
        raise DataBaseError(
            f'Something went wrong on creating database connection in {db_host}:{db_port}/{data_base}/{collection}')


def update_record(collection, record, new_status):
    rec_id = record['_id']

    collection.update_one(
        {'_id': rec_id},
        {'$set': {
            "status": new_status,
            'message': record['message'],
            'info': record['info'],
            'usd': record['usd'],
            'eur': record['eur']}}
    )


def update_error_status(ex, db_connection, record, message, status):
    log(ex)
    record['message'] = message
    record['info'] = f'{ex}'
    update_record(db_connection, record, status)


def create_record(connection, key):
    try:
        result = connection.find_one_and_update({'key': key}, {'$set': {
            "status": 'pending_usd',
            'message': None,
            'info': None,
            'usd': None,
            'eur': None
        }},
                                                upsert=True,
                                                return_document=ReturnDocument.AFTER)

        if result is not None:
            return result

        raise Exception('No record found')
    except Exception as ex:
        log(ex)
        raise RpaException(f'Can\'t select record from {key}. Error: {ex}')


def select_record(connection, key):
    try:

        result = connection.find_one(
            {'key': key}
        )

        if result is not None:
            return result

        raise RecordNotFoundException(f'No record with key [{key}] not found')
    except RecordNotFoundException as ex:
        raise ex
    except Exception as ex:
        log(ex)
        raise RpaException(f'Can\'t select record from {key}. Error: {ex}')


def list_records(connection, key):
    try:
        return list(connection.find({'key': key}))
    except Exception as ex:
        log(ex)
        raise RpaException(f'Can\'t list records from {key}. Error: {ex}')
