import sys
import subprocess
from PyQt6 import QtWidgets, QtCore, QtGui

class SystemProfiler(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1900, 800)
        self.setWindowTitle('System Profiler')

        self.tree = QtWidgets.QTreeWidget(self)
        self.tree.setHeaderLabel('Categories')

        hardware = QtWidgets.QTreeWidgetItem(self.tree)
        hardware.setText(0, 'Hardware')
        hardware.addChild(QtWidgets.QTreeWidgetItem(['SPAudioDataType', 'SPCameraDataType', 'SPCardReaderDataType',
                                                     'SPiBridgeDataType', 'SPDisplaysDataType', 'SPHardwareDataType',
                                                     'SPMemoryDataType', 'SPNVMeDataType', 'SPPCIDataType', 'SPParallelSCSIDataType',
                                                     'SPPowerDataType', 'SPSASDataType', 'SPSerialATADataType',
                                                     'SPSPIDataType', 'SPSmartCardsDataType', 'SPStorageDataType',
                                                     'SPThunderboltDataType', 'SPUSBDataType']))

        network = QtWidgets.QTreeWidgetItem(self.tree)
        network.setText(0, 'Network')
        network.addChild(QtWidgets.QTreeWidgetItem(['SPBluetoothDataType', 'SPEthernetDataType', 'SPNetworkDataType',
                                                    'SPAirPortDataType', 'SPNetworkVolumeDataType', 'SPWWANDataType']))

        software = QtWidgets.QTreeWidgetItem(self.tree)
        software.setText(0, 'Software')
        software.addChild(QtWidgets.QTreeWidgetItem(['SPApplicationsDataType', 'SPDeveloperToolsDataType',
                                                     'SPDisabledSoftwareDataType', 'SPExtensionsDataType',
                                                     'SPFontsDataType', 'SPFrameworksDataType',
                                                     'SPInstallHistoryDataType', 'SPLegacySoftwareDataType',
                                                     'SPLogsDataType', 'SPPrefPaneDataType', 'SPPrintersSoftwareDataType',
                                                     'SPConfigurationProfileDataType', 'SPRawCameraDataType',
                                                     'SPSoftwareDataType', 'SPStartupItemDataType', 'SPSyncServicesDataType']))

        self.textEditTop = QtWidgets.QTextEdit(self)
        self.textEditBottom = QtWidgets.QTextEdit(self)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.textEditTop)
        vbox.addWidget(self.textEditBottom)

        self.rightWidget = QtWidgets.QWidget(self)
        self.rightWidget.setLayout(vbox)

        splitter = QtWidgets.QSplitter(QtCore.Qt.Orientation.Horizontal, self)
        splitter.addWidget(self.tree)
        splitter.addWidget(self.rightWidget)
        splitter.setSizes([400, 1500])

        mainLayout = QtWidgets.QHBoxLayout(self)
        mainLayout.addWidget(splitter)

        self.tree.clicked.connect(self.on_tree_clicked)

    def on_tree_clicked(self, index):
        item_text = self.tree.currentItem().text(0)
        cmd = ['system_profiler', item_text]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
        self.textEditTop.setText(result.stdout)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = SystemProfiler()
    ex.show()
    sys.exit(app.exec())
