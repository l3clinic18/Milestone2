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
    ubx_data = []
    try:
        with open(gps_data, "rb") as gps_file:
            _data = gps_file.read()
            #                                           UBX packet structure                                            #
            # SyncChar1 | SyncChar2 |  Class   |   ID     |   Length   |             Payload              |  CHK_SUM |  #
            #  1 Byte   |  1 Byte   |  1 Byte  |  1 Byte  |   2 Byte   |     Variable 4 Byte increment    |  2 Byte  |  #
            for index in range(len(_data)-1): #reading the file two bytes at a time.
                if _data[index:(index + 2)].hex() == 'b562': #check two bytes to verify UBX packet
                    payload_length = int.from_bytes(_data[(index+4):(index+6)], byteorder='little', signed=False)
                    if _data[(index+2):(index+4)].hex() == '013c': #Check the Class & ID
                        #check the packet for validity
                        if verify_packet(_data[(index+2):(index+payload_length+4)],_data[(payload_length):(payload_length+2)]):
                            UBX_packet_data(_data[(index+6):(index+46)])
                        else:
                            pass
                    #It is not a NAV_RELPOSNED packet. find the length and skip that + 2 bytes.
                    else:
                        index += payload_length + 2
                        continue
                elif (len(_data) - index) < 8:
                    pass
                index += 1
        gps_file.closed
    except(OSError):
        print("Error in opening/reading file. " + str(OSError))
        return None
    return ubx_data
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
    except(OSError):
        print("Error in opening/reading file. " + str(OSError))
        return None
    return _data

#The payload of the UBX packet to be decoded and useful information returned.
def UBX_packet_data(payload):
    #print(payload)
    pass

def verify_packet(_data, chksum):
    pass

#end of file
#If the files are passed in at compile/execution time.
if __name__ == "__main__":
    #test
    GPS_pos_data(sys.argv[1])