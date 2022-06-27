from json import loads
import argparse

from urllib.request import urlopen
from pprint import pprint


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("timezone", help="Your timezone e.g. -7", type=int)
    parser.add_argument("sunset", help="Desired sunset time in format hh:mm", 
                        type=str)
    args = parser.parse_args()
    timezone = args.timezone
    sunset_string = args.sunset
    sunset = int(sunset_string.split(":")[0])*60 + int((sunset_string.split(":")[1]))
    lng = get_longitude_for_sunset((sunset-timezone*60))
    direction="E"
    if(lng < 0):
        lng=lng*-1
        direction="W"
    print(f"Coordinates with desired sunset time: 0.0 N,",lng,direction)

def get_longitude_for_sunset(sunset): # sunset is time in minutes from midnight
    tmp = -90-15/60*sunset
    if(tmp<-180):
        tmp+=360
    return(tmp)

if __name__ == '__main__':
    main()
