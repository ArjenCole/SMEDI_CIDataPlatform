import xlrd


def CheckFile(pFilePath):
    data = xlrd.open_workbook(pFilePath)
    table = data.sheets()[0]
    cell_A1 = table.row(0)[1].value
    rtList = [cell_A1, 'chemistry', 1997, 2000]
    return rtList