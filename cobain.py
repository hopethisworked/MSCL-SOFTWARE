import sys
import mscl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import numpy as np
import csv
import time
import matplotlib.pyplot as plt #import matplotlib library
import os
from Samplingnetwork import SamplingNetworkClass
from Setconfig import settingconfiguration
from mainwindow import Ui_MainWindow

# NODE_ADDRESS = []
# nodes = []
bb = SamplingNetworkClass()
aa=settingconfiguration()
ui = Ui_MainWindow()
# IP_ADDRESS = input("Masukkan IP Address: ")
def starting():
    global tcpConnection,baseStation,node,NODE_ADDRESS
    tcpConnection = mscl.Connection.Serial("COM4")
    baseStation = mscl.BaseStation(tcpConnection)

    NODE_ADDRESS = int(input("Masukkan Node Address: "))
    node = mscl.WirelessNode(NODE_ADDRESS, baseStation)


# node = mscl.WirelessNode(NODE_ADDRESS, baseStation)
config = mscl.WirelessNodeConfig()

class MainWindow(QMainWindow): #Showing Graph Class Window
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
        ui.node1Button_1.clicked.connect(lambda: openWindow1())
        ui.node1Button_2.clicked
        ui.node1Button_3.clicked.connect(lambda: openWindow2())
        ui.node1Button_4.clicked.connect(lambda: self.draw())


        ui.node2Button_1.clicked.connect(lambda: openWindow1())
        ui.node2Button_3.clicked.connect(lambda: openWindow2())

        ui.node3Button_1.clicked.connect(lambda: openWindow1())
        ui.node3Button_3.clicked.connect(lambda: openWindow2())

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



    def draw(self):
        self.x = list(range(1024))  # 100 time points
        self.y1 = [0 for _ in range(1024)]  # 100 data points
        self.y2 = [0 for _ in range(1024)]  # 100 data points
        self.y3 = [0 for _ in range(1024)]  # 100 data points

        ui.nodeGraph_1.showGrid(x=True, y=True)

        self.tcpConnection = tcpConnection
        self.baseStation = mscl.BaseStation(self.tcpConnection)

        self.DataLine1 = ui.nodeGraph_1.plot(self.x, self.y1, pen='r') #CH1 
        self.DataLine2 = ui.nodeGraph_1.plot(self.x, self.y2, pen='g') #CH2
        self.DataLine3 = ui.nodeGraph_1.plot(self.x, self.y3, pen='b') #CH3
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(4)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def enableBeacon(self):
        try:
            # make sure we can ping the base station
            if not self.baseStation.ping():
                print("Failed to ping the Base Station")

            if self.baseStation.features().supportsBeaconStatus():
                status = self.baseStation.beaconStatus()
                print("Beacon current status: Enabled?", status.enabled(), "Time:", status.timestamp())
                print("Attempting to enable the beacon...")

            # enable the beacon on the Base Station using the PC time
            startTime = self.baseStation.enableBeacon()

            # if we got here, no exception was thrown, so enableBeacon was successful
            print("Successfully enabled the beacon on the Base Station")
            print("Beacon's initial Timestamp:", startTime)
        except Exception:
            print("Error Beacon :", Exception._str_) 
        
    def update_plot_data(self):
        arrDataCH1 = []
        arrDataCH2 = []
        arrDataCH3 = []
        tempTimestamp = 0

        sweeps = self.baseStation.getData(1)
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
                            

            self.x = self.x[1:]  # Remove the first y element.
            self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
            
            #DATA1
            self.y1 = self.y1[1:]  # Remove the first
            self.y1.append(arrDataCH1[-1])  # Add a new random value.
            self.DataLine1.setData(self.x, self.y1)  # Update the data.

            #DATA2
            self.y2 = self.y2[1:]  # Remove the first
            self.y2.append(arrDataCH2[-1])  # Add a new random value.
            self.DataLine2.setData(self.x, self.y2)  # Update the data.

            #DATA3
            self.y3 = self.y3[1:]  # Remove the first
            self.y3.append(arrDataCH3[-1])  # Add a new random value.
            self.DataLine3.setData(self.x, self.y3)  # Update the data.

            all_data = tempTimestamp+","+dataPoint.as_string()
            sensor_data_parsing = all_data.split(",")
            with open('sensor_output_glink.csv', 'a', newline='') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(sensor_data_parsing)
                csvFile.close()

    def clear(self):
        self.graphicsView.clear()

def setBaseStation():
    def RFTraffic():
        sweeps = baseStation.getData(1)
        for sweep in sweeps:     
            baseStation.startRfSweepMode               
            print("len sweep data ",len(sweep.data()))
            for RfSweep in sweep.data(): 
                print (RfSweep.as_uint32())  

        setBaseStation()

def openWindow1():
    window = QtWidgets.QWidget()
    bb.setupUi(window)
    window.show()
    bb.pushButton.clicked.connect(lambda: buttonwindow1())
    def buttonwindow1(node):
            a = 0
            while a == 0:
                samplingNetwork(node)
                a+=1
            inputcombo2(node)

##open window for setting configuration
def openWindow2():
    window = QtWidgets.QWidget()
    aa.setupUi(window)
    window.show()  
    aa.pushButton.clicked.connect(lambda: buttonset())


def samplingNetwork(node):
    def samplingRate(node):
        sRInputUser = int(input(bb.comboBox.currentIndex()))
        if sRInputUser == 1 :
            config.sampleRate(mscl.WirelessTypes.sampleRate_1Hz)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif sRInputUser == 2 :
            config.sampleRate(mscl.WirelessTypes.sampleRate_2Hz)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif sRInputUser == 3 :
            config.sampleRate(mscl.WirelessTypes.sampleRate_4Hz)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif sRInputUser == 4 :
            config.sampleRate(mscl.WirelessTypes.sampleRate_8Hz)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif sRInputUser == 5 :
            config.sampleRate(mscl.WirelessTypes.sampleRate_16Hz)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif sRInputUser == 6 :
            config.sampleRate(mscl.WirelessTypes.sampleRate_32Hz)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif sRInputUser == 7 :
            config.sampleRate(mscl.WirelessTypes.sampleRate_64Hz)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif sRInputUser == 8 :
            mscl.WirelessNodeConfig().sampleRate(mscl.WirelessTypes.sampleRate_128Hz)
            node.applyConfig(mscl.WirelessNodeConfig())
            samplingNetwork(node) 
        elif sRInputUser == 9 :
            config.sampleRate(mscl.WirelessTypes.sampleRate_256Hz)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif sRInputUser == 10 :
            config.sampleRate(mscl.WirelessTypes.sampleRate_512Hz)
            node.applyConfig(config)
            samplingNetwork(node) 
    def dataCollect(node):
        print("1. Log and Transmit \n2. Log Only \n3. Transmit Only\n")
        DCInputUser = int(input("\nMasukkan Pilihan Menu: "))
        if DCInputUser == 1:
            config.dataCollectionMethod(mscl.WirelessTypes.collectionMethod_logAndTransmit)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif DCInputUser == 2:
            config.dataCollectionMethod(mscl.WirelessTypes.collectionMethod_logOnly)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif DCInputUser == 3:
            config.dataCollectionMethod(mscl.WirelessTypes.collectionMethod_transmitOnly)
            node.applyConfig(config)
            samplingNetwork(node) 
        def channelActivate(node):
            # mscl.ChannelMask
            # mscl.ChannelMask.enable(1)
            # config.activeChannels(channels);
            print("Belum")
            samplingNetwork(node) 
        def applySampling(node):
            network = mscl.SyncSamplingNetwork(baseStation)
            print("Menghubungkan Node ke jaringan . . .")
            network.addNode(node)
            print("Done.\n")
            print("Network info: ")
            print("\t Network OK: ", network.ok())
            print("\t Percent of Bandwidth: ", network.percentBandwidth())
            print("\t Lossless Enabled: ", network.lossless())
            print("\nApplying network configuration")
            network.applyConfiguration()
            print("Done.\n")
            print("Starting the network...")
            network.startSampling()
            print("Done.\n")
            samplingNetwork(node) 

        print("1. Sampling Rate \n2. Log/Transmit\n3. Channel\n4. Apply and Sampling Network\n5. Back")   
        setNodeInputUser = int(input("\nMasukkan Pilihan Menu: "))
        if setNodeInputUser == 1:
            samplingRate(node)
        elif setNodeInputUser == 2:
            dataCollect(node)
        elif setNodeInputUser == 3:
            channelActivate(node)
        elif setNodeInputUser == 4:
            applySampling(node)
        elif setNodeInputUser == 5:
            setNode()        
        else:
            print("Input Salah!")
            samplingNetwork(node)     
    def setToIdle(node):
        idleStatus = node.setToIdle()
        while not idleStatus.complete():
            print ("."),
        result = idleStatus.result()
        if result == mscl.SetToIdleStatus.setToIdleResult_success:
            print ("Node is now in idle mode.")
            setNode()
        elif result == mscl.SetToIdleStatus.setToIdleResult_canceled:
            print ("Set to Idle was canceled!")
            setNode()
        else:
            print ("Set to Idle has failed!")
            setNode()
    def getCurrentConfig(node):
        print ("Current Configuration Settings:\n")
        print ("User Inactivity Timeout:", node.getInactivityTimeout(), "seconds")
        print ("Total active channels:", node.getActiveChannels().count())
        chGroups = node.features().channelGroups()
        for group in chGroups:
            groupSettings = group.settings()
            for setting in groupSettings:
                if setting == mscl.WirelessTypes.chSetting_linearEquation:
                    le = node.getLinearEquation(group.channels())
                    print ("Linear Equation for: ", group.name())
                    print ("Slope: ", le.slope())
                    print ("Offset: ", le.offset())
        setNode()
    def showGraph():
        if __name__ == "__main__":
            import sys
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            app.exec_()
            setNode()

        
    def setConfig(node):
        config.defaultMode(mscl.WirelessTypes.defaultMode_idle)
        config.inactivityTimeout(7200)
        config.unlimitedDuration(True)
        config.samplingMode(mscl.WirelessTypes.samplingMode_sync)
        config.dataFormat(mscl.WirelessTypes.dataFormat_cal_float)

        def hardwareConfig(node):
            def inputRange(node):
                accelChannelMaskIR = mscl.ChannelMask(7)
                print("Pilih Input Range:\n1. 2G\n2. 4G\n3. 8G\n")
                pilihIR= int(input("Masukkan Pilihan Menu: "))
                if pilihIR == 1:
                    config.inputRange(accelChannelMaskIR, mscl.WirelessTypes.range_2G)
                    node.applyConfig(config)
                    setConfig(node)
                elif pilihIR == 2:
                    config.inputRange(accelChannelMaskIR, mscl.WirelessTypes.range_4G)
                    node.applyConfig(config)
                    setConfig(node)
                elif pilihIR == 3:
                    config.inputRange(accelChannelMaskIR, mscl.WirelessTypes.range_8G)
                    node.applyConfig(config)
                    setConfig(node)

            def lowPassFilter(node):
                accelChannelMaskLPF = mscl.ChannelMask(7)
                print("Pilih Low Pass Filter:\n1. 26Hz\n2. 52Hz\n3. 104Hz\n4. 209Hz\n5. 418Hz\n6. 800Hz\n")
                pilihLPF= int(input("Masukkan Pilihan Menu: "))
                if pilihLPF == 1:
                    config.lowPassFilter(accelChannelMaskLPF, mscl.WirelessTypes.filter_26hz)
                    node.applyConfig(config)
                    setConfig(node)
                elif pilihLPF == 2:
                    config.lowPassFilter(accelChannelMaskLPF, mscl.WirelessTypes.filter_52hz)
                    node.applyConfig(config)
                    setConfig(node)
                elif pilihLPF == 3:
                    config.lowPassFilter(accelChannelMaskLPF, mscl.WirelessTypes.filter_104hz)       
                    node.applyConfig(config)
                    setConfig(node)
                elif pilihLPF == 4:
                    config.lowPassFilter(accelChannelMaskLPF, mscl.WirelessTypes.filter_209hz)
                    node.applyConfig(config)
                    setConfig(node)              
                elif pilihLPF == 5:
                    config.lowPassFilter(accelChannelMaskLPF, mscl.WirelessTypes.filter_418hz) 
                    node.applyConfig(config)
                    setConfig(node)           
                elif pilihLPF == 6:
                    config.lowPassFilter(accelChannelMaskLPF, mscl.WirelessTypes.filter_800hz)
                    node.applyConfig(config)
                    setConfig(node)
            
            def highPassFilter(node):
                accelChannelMaskHPF = mscl.ChannelMask(7)
                print("Pilih High Pass Filter:\n1. Enable\n2. Disable")
                pilihHPF= int(input("Masukkan Pilihan Menu: "))
                if pilihHPF == 1:
                    config.highPassFilter(accelChannelMaskHPF, mscl.WirelessTypes.highPass_auto)
                    node.applyConfig(config)
                    setConfig(node)
                if pilihHPF == 2:
                    config.highPassFilter(accelChannelMaskHPF, mscl.WirelessTypes.highPass_off)
                    node.applyConfig(config)
                    setConfig(node)
            print("1. Input Range\n2. Low Pass Filter\n3. High Pass Filter\n4. Back to Configure")
            setHwrInputUser = int(input("\nMasukkan Pilihan Menu: "))
            if setHwrInputUser == 1:
                inputRange(node)
            elif setHwrInputUser == 2:
                lowPassFilter(node)
            elif setHwrInputUser ==3:
                highPassFilter(node)
            elif setHwrInputUser ==4:
                setConfig(node)
            else:
                print("Input Salah!")
                setConfig(node)

        def calibrationConfig(node):
            def calCoef(node):
                accelChannelMaskCh1 = mscl.ChannelMask(1) 
                accelChannelMaskCh2 = mscl.ChannelMask(2)
                accelChannelMaskCh3 = mscl.ChannelMask(4)
                print("Pilih Channel:\n1. CH1\n2. CH2\n3. CH3\n")
                pilihCH = int(input("\nMasukkan Pilihan Menu: "))
                if pilihCH == 1:
                    print("Pilih Unit:\n1. g\n2. milliG\n3. Feet per Second Squared\n4. Meter per Second Squared\n")
                    pilihUnitCH1 = int(input("\nMasukkan Pilihan Menu: "))
                    if pilihUnitCH1 == 1:
                        config.unit(accelChannelMaskCh1, mscl.WirelessTypes.unit_accel_g)
                        node.applyConfig(config)
                        calibrationConfig(node)
                    elif pilihUnitCH1 == 2:
                        config.unit(accelChannelMaskCh1, mscl.WirelessTypes.unit_accel_milliG)    
                        node.applyConfig(config) 
                        calibrationConfig(node)
                    elif pilihUnitCH1 == 3:
                        config.unit(accelChannelMaskCh1, mscl.WirelessTypes.unit_accel_ftPerSec2)          
                        node.applyConfig(config)
                        calibrationConfig(node)
                    elif pilihUnitCH1 == 4:
                        config.unit(accelChannelMaskCh1, mscl.WirelessTypes.unit_accel_mPerSec2)             
                        node.applyConfig(config)
                        calibrationConfig(node)
                if pilihCH == 2:
                    print("Pilih Unit:\n1. g\n2. milliG\n3. Feet per Second Squared\n4. Meter per Second Squared\n")
                    pilihUnitCH2 = int(input("\nMasukkan Pilihan Menu: "))
                    if pilihUnitCH2 == 1:
                        config.unit(accelChannelMaskCh2, mscl.WirelessTypes.unit_accel_g)
                        node.applyConfig(config)
                        calibrationConfig(node)
                    elif pilihUnitCH2 == 2:
                        config.unit(accelChannelMaskCh2, mscl.WirelessTypes.unit_accel_milliG)
                        node.applyConfig(config) 
                        calibrationConfig(node)   
                    elif pilihUnitCH2 == 3:
                        config.unit(accelChannelMaskCh2, mscl.WirelessTypes.unit_accel_ftPerSec2)
                        node.applyConfig(config)  
                        calibrationConfig(node)        
                    elif pilihUnitCH2 == 4:
                        config.unit(accelChannelMaskCh2, mscl.WirelessTypes.unit_accel_mPerSec2)  
                        node.applyConfig(config)
                        calibrationConfig(node)
                if pilihCH == 3:
                    print("Pilih Unit:\n1. g\n2. milliG\n3. Feet per Second Squared\n4. Meter per Second Squared\n")
                    pilihUnitCH3 = int(input("\nMasukkan Pilihan Menu: "))
                    if pilihUnitCH3 == 1:
                        config.unit(accelChannelMaskCh3, mscl.WirelessTypes.unit_accel_g)
                        node.applyConfig(config)
                        calibrationConfig(node)
                    elif pilihUnitCH3 == 2:
                        config.unit(accelChannelMaskCh3, mscl.WirelessTypes.unit_accel_milliG)
                        node.applyConfig(config) 
                        calibrationConfig(node)  
                    elif pilihUnitCH3 == 3:
                        config.unit(accelChannelMaskCh3, mscl.WirelessTypes.unit_accel_ftPerSec2)
                        node.applyConfig(config)  
                        calibrationConfig(node)        
                    elif pilihUnitCH3 == 4:
                        config.unit(accelChannelMaskCh3, mscl.WirelessTypes.unit_accel_mPerSec2)
                        node.applyConfig(config)     
                        calibrationConfig(node)              
            print("1. Change Unit Calibration\n2. Slope Offset\n3. Back to Configure")
            setClbConfig = int(input("\nMasukkan Pilihan Menu: "))
            if setClbConfig == 1:
                calCoef(node)
            elif setClbConfig == 2:
                print ("Belum")
                calibrationConfig(node)
            elif setClbConfig == 3:
                setConfig(node)

        print("1. Hardware\n2. Calibration\n3. Back to Set Node")
        setConfigInputUser = int(input("\nMasukkan Pilihan Menu: "))
        if setConfigInputUser == 1:
            hardwareConfig(node)
        elif setConfigInputUser == 2:
            calibrationConfig(node)
        elif setConfigInputUser ==3:
            setNode()
        else:
            print("Input Salah!")
            setConfig(node)

    print("1. Sampling Network \n2. Set To Idle\n3. Configure\n4. Check Config Sekarang\n5. Show Graph Data\n6. Back to Main Menu")
    setNodeInputUser = int(input("\nMasukkan Pilihan Menu: "))
    if setNodeInputUser == 1:
        samplingNetwork(node)
    elif setNodeInputUser == 2:
        setToIdle(node)
    elif setNodeInputUser == 3:
        setConfig(node)
    elif setNodeInputUser == 4:
        getCurrentConfig(node)
    elif setNodeInputUser == 5:
        showGraph()
    elif setNodeInputUser == 6:
        mainMenu()
    else:
        print("Input Salah!")
        setNode()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())