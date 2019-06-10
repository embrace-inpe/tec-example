
import pymongo
import logging

import db.settings as settings

from pymongo import MongoClient


class Persistence:
    """

    """

    def _connect(self, address):
        """Set up a connection to the MongoDB server.

        :param address: MongoDB server address
        :return: the client connection
        """
        client = MongoClient(address)

        if settings.DATABASE not in client.list_database_names():
            logging.warning(">> The database {} does not exists.".format(settings.DATABASE))
            return

        try:
            client.server_info()
        except pymongo.errors.ServerSelectionTimeoutError as e:
            logging.error(">> Unable to connect in {}: {}".format(address, e))
            client = None

        return client

    def save_tec_dict(self, tec_processed_list):
        """

        :param tec_processed_list:
        :return:
        """
        if not tec_processed_list:
            logging.info(">> No records to save!")
            return
        else:
            try:
                client = self._connect(settings.DB_HOST)

                db = client[settings.DATABASE]
                collection = db["estimated"]
                collection.insert_many(tec_processed_list)

                # with client.start_session() as s:
                #     s.start_transaction()
                #     collection.insert_many(tec_processed_list, session=s)
                #     s.commit_transaction()

                client.close()

                logging.info(">> {} record(s) successful saved!".format(len(tec_processed_list)))

            except pymongo.errors.InvalidDocument:
                logging.warning(">>>> Invalid document or connection was not possible!")