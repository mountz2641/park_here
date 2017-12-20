from practicum import McuBoard

####################################
class McuWithPeriBoard(McuBoard):

    ################################
    def getSwitch(self):
        '''
        Return a boolean value indicating whether the switch on the peripheral
        board is currently pressed
        '''
        result =  self.usb_read(request = 2, length = 1)
        return result[0] == 0

    ################################
    def getLight(self, channel):
        '''
        Return the current reading of light sensor on peripheral board
        '''
        result =  self.usb_read(request = 3, length = 2, value = channel)
        return result[1] * 256 + result[0]
