#Position data in .txt format and output distant and/or x/y as a List.
import sys
import binascii
#Pixy position data.
#cam_data is a text file path. String.
def camera_pos_data(cam_data):
    pass
#GPS RTK distance between base station and rover.
#gps_data, text file, HEX. Argument type: String
#Returns a list of reletive distance measurements in meters.
def GPS_pos_data(gps_data):
    _data = []
    try:
        with open(gps_data, "rb") as gps_file:
            for line in gps_file:
                if line[0:4].hex() == 'b5620130': #check first 5 bytes to aquire UBX packet.
                    print(True)
        gps_file.closed
    except(OSError):
        print("Error in opening/reading file. " + str(OSError))
        return None
    return _data
#UWB distance data.
#umb_data, text file, ascii. Argument type: String.
#Returns a list of reletive distance measurements in meters. Otherwise returns None object    
def UWB_pos_data(uwb_data):
    _data = []
    try:
        with open(uwb_data, "rb") as uwb_file:
            for line in uwb_file:
                data_list = line.split(b',')
                if len(data_list) == 8 and (b'\n' in data_list[7]):
                    _data.append(float(data_list[7].strip(b'\n')))
            print(_data[1])
        uwb_file.closed
    except(OSError):
        print("Error in opening/reading file. " + str(OSError))
        return None
    return _data


#end of file
#If the files are passed in at compile/execution time.
if __name__ == "__main__":
    #test
    GPS_pos_data(sys.argv[1])