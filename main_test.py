from datetime import datetime, timedelta
import logging
import settings
from app.downloads import DownloadDCB, DownloadOrbit

def main():
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

    rinex = 'SJSP0088.19O'
    year = datetime.strptime(rinex[-3:-1], '%y').strftime('%Y')
    day = rinex[4:7]
    month = datetime.strptime(day, '%j').strftime('%m')
    print(year, day, month)

    #orbit = DownloadOrbit(year, month, day)
    orbit = DownloadOrbit('2014', '01', '007')
    print(orbit.orbit_sufix)

    print(orbit)
    #print(orbit.day, orbit.year, orbit.month)
    orbit.download()


if __name__ == "__main__":
    main()
