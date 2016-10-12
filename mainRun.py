import importdata as id
import EMD
import pickle

s_folderPath = 'Z:\\TimeHistory\\MatLabCodeFromWeb\\Ben_Code\\data2'
s_fileName = 'abraham25n.dat'

s_storage = 'Z:\\TimeHistory\\MatLabCodeFromWeb\\Ben_Code\\Pickles\\data20161012.p'

dataimport = 1
analyze = 0

if dataimport == 1:
# test = id.importTemperatureFile(s_folderPath, s_fileName)
    test1 = id.importTemperatureFolder(s_folderPath)
    pickle.dump(test1, open(s_storage,'wb'), 0)

if analyze == 1:
    test1 = pickle.load(open(s_storage, 'rb'))
    run = EMD.EMD()
    run.runEMD()
