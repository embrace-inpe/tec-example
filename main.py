import logging
import os
import sys
import time

from tec_embrace import tec
#import db.persistence as persistence
import settings as settings

from logging import handlers


def process_tec_by_station(files):
    """
    Main workflow of TECMAP by station. This routine can sequentially calculate the TEC relative, the slant factor,
    absolute, and vertical. Besides, it can generate an accurate estimate of bias receptor along the day

    :param rinex_folder: Absolute path to the rinex folder
    :param files: Rinex's files respecting to N-stations
    :return: tec_processed
    """
    rinex_folder = settings.RINEX_FOLDER
    path_dcb = settings.PATH_DCB
    path_orbit = settings.PATH_ORBIT
    path_glonass_channel = settings.PATH_GLONASS_CHANNEL

    min_requeried_version = settings.MIN_REQUIRED_VERSION
    constelations = settings.CONSTELATIONS
    tec_resolution = settings.TEC_RESOLUTION
    tec_resolution_value = settings.TEC_RESOLUTION_VALUE
    keys_save = settings.KEYS_SAVE

    pipeline = tec.TEC(rinex_folder, path_dcb, path_orbit, path_glonass_channel, min_requeried_version, constelations, tec_resolution, tec_resolution_value, keys_save)

    tec_processed = []

    for file in files:
        try:
            tec_result = pipeline.process_tec_file(file)
            tec_processed.append(tec_result)
        except:
            continue

        logging.info("{} file(s) stacked to be persisted!".format(len(tec_processed)))

    return tec_processed


if __name__=='__main__':
    log = logging.getLogger('')
    log.setLevel(logging.INFO)
    format = logging.Formatter("[%(asctime)s] {%(filename)-15s:%(lineno)-4s} %(levelname)-5s: %(message)s ",
                               datefmt='%Y.%m.%d %H:%M:%S')

    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(format)

    fh = logging.handlers.RotatingFileHandler(filename='tecmap.log', maxBytes=(1048576 * 5), backupCount=7)
    fh.setFormatter(format)

    log.addHandler(ch)
    log.addHandler(fh)

    #persist = persistence.Persistence()
    files = sorted(os.listdir(settings.RINEX_FOLDER))
    before = dict([(f, None) for f in files])

    tec_processed = process_tec_by_station(files)
    #persist.save_tec_dict(tec_processed)

    logging.info("-----------------------------------------------------------------------------------")
    logging.info(">> Watching folder {} for more files...".format(settings.RINEX_FOLDER))
    while 1:
        time.sleep(20)
        if os.path.isdir(settings.RINEX_FOLDER):
            after = dict([(file, None) for file in os.listdir(settings.RINEX_FOLDER)])
            added = [file for file in after if not file in before]

            if added:
                tec_processed = process_tec_by_station(added)
                #persist.save_tec_dict(tec_processed)

                logging.info("-----------------------------------------------------------------------------------")
                logging.info(">> Watching folder {} for more files...".format(settings.RINEX_FOLDER))

            before = after
        else:
            logging.info(">>>> Folder " + settings.RINEX_FOLDER + " deleted or does not exist anymore!")

