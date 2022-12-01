from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from mainwindow import Ui_MainWindow
import time
from random import randint
# IMPORT FUNCTIONS
from Samplingnetwork import SamplingNetworkClass

#from cobain import *
from Setconfig import settingconfiguration 

import mscl
import csv

config = mscl.WirelessNodeConfig()

ui = Ui_MainWindow()
bb = SamplingNetworkClass()
aa = settingconfiguration()

def starting():
    global ip_address, Connection, baseStation, node, node_address, baseStation, network
    ip_address = "COM4"
    Connection = mscl.Connection.Serial(ip_address)
    baseStation = mscl.BaseStation(Connection)
    node_address = 56532
    node = mscl.WirelessNode(node_address, baseStation)


    network = mscl.SyncSamplingNetwork(baseStation)
    network.addNode(node)
    network.applyConfiguration()
    network.startSampling()
    global setConfig
    def setConfig():
        config.defaultMode(mscl.WirelessTypes.defaultMode_idle)
        config.inactivityTimeout(7200)
        config.unlimitedDuration(True)
        config.samplingMode(mscl.WirelessTypes.samplingMode_sync)
        config.dataFormat(mscl.WirelessTypes.dataFormat_cal_float)

def openWindow1(node):
    window = QtWidgets.QWidget()
    bb.setupUi(window)
    window.show()
    bb.pushButton.clicked.connect(lambda: buttonwindow1(node))
    def buttonwindow1(node):
        a = 0
        while a == 0:
            inputcombo1(node)
            a+=1
        inputcombo2(node)

##open window for setting configuration
def openWindow2(node):
    window = QtWidgets.QWidget()
    aa.setupUi(window)
    window.show()  
    aa.pushButton.clicked.connect(lambda: buttonset(node))
    def buttonset(node):
        inputbox(node)
        lowPassFilter(node)
        highPassFilter(node)
        calCoef(node)





def inputcombo1(node):
    sRInputUser = int(bb.comboBox.currentIndex())
    if sRInputUser == 0 :
        config.sampleRate(mscl.WirelessTypes.sampleRate_1Hz)
        node.applyConfig(config)
    elif sRInputUser == 1 :
        config.sampleRate(mscl.WirelessTypes.sampleRate_2Hz)
        node.applyConfig(config) 
    elif sRInputUser == 2 :
        config.sampleRate(mscl.WirelessTypes.sampleRate_4Hz)
        node.applyConfig(config)
        
    elif sRInputUser == 3 :
        config.sampleRate(mscl.WirelessTypes.sampleRate_8Hz)
        node.applyConfig(config) 
    elif sRInputUser == 4 :
        config.sampleRate(mscl.WirelessTypes.sampleRate_16Hz)
        node.applyConfig(config)
            
    elif sRInputUser == 5 :
        config.sampleRate(mscl.WirelessTypes.sampleRate_32Hz)
        node.applyConfig(config)
            
    elif sRInputUser == 6 :
        config.sampleRate(mscl.WirelessTypes.sampleRate_64Hz)
        node.applyConfig(config) 
    elif sRInputUser == 7 :
        config.sampleRate(mscl.WirelessTypes.sampleRate_128Hz)
        node.applyConfig(config)
    elif sRInputUser == 8 :
        config.sampleRate(mscl.WirelessTypes.sampleRate_256Hz)
        node.applyConfig(config) 
    elif sRInputUser == 9 :
        config.sampleRate(mscl.WirelessTypes.sampleRate_512Hz)
        node.applyConfig(config)
def inputcombo2(node):
    DCInputUser = bb.comboBox_2.currentIndex()
    if DCInputUser == 0:
        config.dataCollectionMethod(mscl.WirelessTypes.collectionMethod_logAndTransmit)
        node.applyConfig(config)
    elif DCInputUser == 1:
        config.dataCollectionMethod(mscl.WirelessTypes.collectionMethod_logOnly)
        node.applyConfig(config)
    elif DCInputUser == 2:
        config.dataCollectionMethod(mscl.WirelessTypes.collectionMethod_transmitOnly)
        node.applyConfig(config)

def inputbox(node):
    pilihIR = aa.comboBox.currentIndex()
    accelChannelMaskIR = mscl.ChannelMask(7)
    if pilihIR == 0:
        config.inputRange(accelChannelMaskIR, mscl.WirelessTypes.range_2G)
        node.applyConfig(config)
        setConfig(node)
    elif pilihIR == 1:
        config.inputRange(accelChannelMaskIR, mscl.WirelessTypes.range_4G)
        node.applyConfig(config)
        setConfig(node)
    elif pilihIR == 2:
        config.inputRange(accelChannelMaskIR, mscl.WirelessTypes.range_8G)
        node.applyConfig(config)
        setConfig(node)

def lowPassFilter(node):
    pilihLPF = int(aa.comboBox_2.curr)
    accelChannelMaskLPF = mscl.ChannelMask(7)
    if pilihLPF == 0:
        config.lowPassFilter(accelChannelMaskLPF, mscl.WirelessTypes.filter_26hz)
        node.applyConfig(config)
        setConfig(node)
    elif pilihLPF == 1:
        config.lowPassFilter(accelChannelMaskLPF, mscl.WirelessTypes.filter_52hz)
        node.applyConfig(config)
        setConfig(node)
    elif pilihLPF == 2:
        config.lowPassFilter(accelChannelMaskLPF, mscl.WirelessTypes.filter_104hz)       
        node.applyConfig(config)
        setConfig(node)
    elif pilihLPF == 3:
        config.lowPassFilter(accelChannelMaskLPF, mscl.WirelessTypes.filter_209hz)
        node.applyConfig(config)
        setConfig(node)              
    elif pilihLPF == 4:
        config.lowPassFilter(accelChannelMaskLPF, mscl.WirelessTypes.filter_418hz) 
        node.applyConfig(config)
        setConfig(node)           
    elif pilihLPF == 5:
        config.lowPassFilter(accelChannelMaskLPF, mscl.WirelessTypes.filter_800hz)
        node.applyConfig(config)
        setConfig(node)

def highPassFilter(node):
    accelChannelMaskHPF = mscl.ChannelMask(7)
    pilihHPF= int(aa.comboBox_3.currentIndex())
    if pilihHPF == 1:
        config.highPassFilter(accelChannelMaskHPF, mscl.WirelessTypes.highPass_auto)
        node.applyConfig(config)
        setConfig(node)
    if pilihHPF == 2:
        config.highPassFilter(accelChannelMaskHPF, mscl.WirelessTypes.highPass_off)
        node.applyConfig(config)
        setConfig(node)

def calCoef(node):
    accelChannelMaskCh1 = mscl.ChannelMask(1) 
    accelChannelMaskCh2 = mscl.ChannelMask(2)
    accelChannelMaskCh3 = mscl.ChannelMask(4)
    pilihCH = int(aa.comboBox_4.currentIndex)
    if pilihCH == 0:
        pilihUnitCH1 = int(aa.comboBox_5.currentIndex)
        if pilihUnitCH1 == 1:
            config.unit(accelChannelMaskCh1, mscl.WirelessTypes.unit_accel_g)
            node.applyConfig(config)
        elif pilihUnitCH1 == 2:
            config.unit(accelChannelMaskCh1, mscl.WirelessTypes.unit_accel_milliG)    
            node.applyConfig(config) 
        elif pilihUnitCH1 == 3:
            config.unit(accelChannelMaskCh1, mscl.WirelessTypes.unit_accel_ftPerSec2)          
            node.applyConfig(config)

        elif pilihUnitCH1 == 4:
            config.unit(accelChannelMaskCh1, mscl.WirelessTypes.unit_accel_mPerSec2)             
            node.applyConfig(config)

    if pilihCH == 1:
        pilihUnitCH2 = int(aa.comboBox_5.currentIndex)
        if pilihUnitCH2 == 1:
            config.unit(accelChannelMaskCh2, mscl.WirelessTypes.unit_accel_g)
            node.applyConfig(config)

        elif pilihUnitCH2 == 2:
            config.unit(accelChannelMaskCh2, mscl.WirelessTypes.unit_accel_milliG)
            node.applyConfig(config) 

        elif pilihUnitCH2 == 3:
            config.unit(accelChannelMaskCh2, mscl.WirelessTypes.unit_accel_ftPerSec2)
            node.applyConfig(config)  
    
        elif pilihUnitCH2 == 4:
            config.unit(accelChannelMaskCh2, mscl.WirelessTypes.unit_accel_mPerSec2)  
            node.applyConfig(config)
            node.calibrationConfig(node)
    if pilihCH == 2:
        pilihUnitCH3 = int(aa.comboBox_5.currentIndex)
        if pilihUnitCH3 == 1:
            config.unit(accelChannelMaskCh3, mscl.WirelessTypes.unit_accel_g)
            node.applyConfig(config)

        elif pilihUnitCH3 == 2:
            config.unit(accelChannelMaskCh3, mscl.WirelessTypes.unit_accel_milliG)
            node.applyConfig(config) 

        elif pilihUnitCH3 == 3:
            config.unit(accelChannelMaskCh3, mscl.WirelessTypes.unit_accel_ftPerSec2)
            node.applyConfig(config)  
    
        elif pilihUnitCH3 == 4:
                    config.unit(accelChannelMaskCh3, mscl.WirelessTypes.unit_accel_mPerSec2)
                    node.applyConfig(config)     
    

    # def enableBeacon(self):
    #     try:
    #         # make sure we can ping the base station
    #         if not baseStation.ping():
    #             print("Failed to ping the Base Station")

    #         if baseStation.features.supportsBeaconStatus():
    #             status = baseStation.beaconStatus()
    #             print("Beacon current status: Enabled?", status.enabled(), "Time:", status.timestamp())
    #             print("Attempting to enable the beacon...")

    #         # enable the beacon on the Base Station using the PC time
    #         startTime = baseStation.enableBeacon()

    #         # if we got here, no exception was thrown, so enableBeacon was successful
    #         print("Successfully enabled the beacon on the Base Station")
    #         print("Beacon's initial Timestamp:", startTime)
    #     except Exception:
    #         print("Error Beacon :", Exception._str_) 
def draw1():    
    x = list(range(1024))  # 100 time points
    y1 = [0 for _ in range(1024)]  # 100 data points
    y2 = [0 for _ in range(1024)]  # 100 data points
    y3 = [0 for _ in range(1024)]  # 100 data points

    ui.nodeGraph_1.showGrid(x=True, y=True)

    Connection = mscl.Connection.Serial(ip_address, 5000)
    baseStation = mscl.BaseStation(Connection)

    DataLine1 = ui.nodeGraph_1.plot(x, y1, pen='r') #CH1 
    DataLine2 = ui.nodeGraph_1.plot(x, y2, pen='g') #CH2
    DataLine3 = ui.nodeGraph_1.plot(x, y3, pen='b') #CH3
    
    timer = QtCore.QTimer()
    timer.setInterval(4)
    timer.timeout.connect(update_plot_data)
    timer.start()
    def update_plot_data():
        arrDataCH1 = []
        arrDataCH2 = []
        arrDataCH3 = []
        tempTimestamp = 0

        sweeps = baseStation.getData(1)
        print(len(sweeps))
        for sweep in sweeps:                    
            i=0 
            print("len sweep data ",len(sweep.data()))
            tempTimestamp = str(sweep.timestamp())
            for dataPoint in sweep.data():                  
                
                i+=1
                if i is 1:
                    arrDataCH1.append(dataPoint.as_float())
                elif i is 2:
                    arrDataCH2.append(dataPoint.as_float()) 
                elif i is 3:
                    arrDataCH3.append(dataPoint.as_float())
                            

            x = x[1:]  # Remove the first y element.
            x.append(x[-1] + 1)  # Add a new value 1 higher than the last.
            
            #DATA1
            y1 = y1[1:]  # Remove the first
            y1.append(arrDataCH1[-1])  # Add a new random value.
            DataLine1.setData(x, y1)  # Update the data.

            #DATA2
            y2 = y2[1:]  # Remove the first
            y2.append(arrDataCH2[-1])  # Add a new random value.
            DataLine2.setData(x, y2)  # Update the data.

            #DATA3
            y3 = y3[1:]  # Remove the first
            y3.append(arrDataCH3[-1])  # Add a new random value.
            DataLine3.setData(x, y3)  # Update the data.

            all_data = tempTimestamp+","+dataPoint.as_string()
            sensor_data_parsing = all_data.split(",")
            with open('sensor_output_glink.csv', 'a', newline='') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(sensor_data_parsing)
                csvFile.close()

class MainWindow(QMainWindow):
    ##open window for sampling network
    def __init__(self):
        QMainWindow.__init__(self)
        ui.setupUi(self)
        ## FUNCTIONS
        ## PAGES
        ########################################################################
        #home page
        #self.ui.checkButton.pressed.connect(lambda: self.settingbuttonss())

        # PAGE 1
        ui.activityButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.Activity))

        # PAGE 2
        ui.homeButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.Home))
        ui.checkButton.clicked.connect(lambda: starting())

        # PAGE 3
        ui.devicesButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.Devices))

        #devices page
        ui.baseButton.clicked.connect(lambda: ui.devicePage.setCurrentWidget(ui.base_Page))
        ui.node1Button.clicked.connect(lambda: ui.devicePage.setCurrentWidget(ui.node_1))
        ui.node2Button.clicked.connect(lambda: ui.devicePage.setCurrentWidget(ui.node_2))
        ui.node3Button.clicked.connect(lambda: ui.devicePage.setCurrentWidget(ui.node_3))
        
        #Node windows
        ui.node1Button_1.clicked.connect(lambda: openWindow1(node))
        ui.node1Button_2.clicked
        ui.node1Button_3.clicked.connect(lambda: openWindow2(node))
        ui.node1Button_4.clicked.connect(lambda: draw1)


        ui.node2Button_1.clicked.connect(lambda: openWindow1(node))
        ui.node2Button_3.clicked.connect(lambda: openWindow2(node))

        ui.node3Button_1.clicked.connect(lambda: openWindow1(node))
        ui.node3Button_3.clicked.connect(lambda: openWindow2(node))

        #graph functions
        ui.nodeGraph_1.hide()
        ui.graphLabel_1.hide()
        ui.graphButton_1.pressed.connect(lambda: ui.graphLabel_1.show())
        ui.graphButton_1.pressed.connect(lambda: ui.nodeGraph_1.show())
        ui.graphButton_1.clicked.connect(lambda: ui.nodeGraph_1.hide())
        ui.graphLabel_2.hide()
        ui.graphButton_2.pressed.connect(lambda: ui.graphLabel_2.show())
        ui.nodeGraph_2.hide()
        ui.graphButton_2.pressed.connect(lambda: ui.nodeGraph_2.show())
        ui.graphLabel_3.hide()
        ui.graphButton_3.pressed.connect(lambda: ui.graphLabel_3.show())
        ui.nodeGraph_3.hide()
        ui.graphButton_3.pressed.connect(lambda: ui.nodeGraph_3.show())
        ui.graphLabel_4.hide()
        ui.graphButton_4.pressed.connect(lambda: ui.graphLabel_4.show())
        ui.nodeGraph_4.hide()
        ui.graphButton_4.pressed.connect(lambda: ui.nodeGraph_4.show())   

        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())