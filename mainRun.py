import importdata as id

s_folderPath = 'Z:\\TimeHistory\\MatLabCodeFromWeb\\Ben_Code\\data2'
s_fileName = 'abraham25n.dat'

test = id.importTemperatureFile(s_folderPath, s_fileName)
test1 = id.importTemperatureFolder(s_folderPath)