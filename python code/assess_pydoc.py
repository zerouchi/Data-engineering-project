from lxml import objectify
import pandas as pd


def xmlTOcsv(file_path):
    xml = objectify.parse(open(file_path))
    root = xml.getroot()

    filename = "asses.csv"
    file = open(filename, "w")

    headers = "FinInstrmGnlAttrbts.Id, FinInstrmGnlAttrbts.FullNm,FinInstrmGnlAttrbts.ClssfctnTp,FinInstrmGnlAttrbts.CmmdtyDerivInd,FinInstrmGnlAttrbts.NtnlCcy,Issr \n"
    file.write(headers)

    a = "FinInstrmGnlAttrbts.Id"
    b = "FinInstrmGnlAttrbts.FullNm"
    c = "FinInstrmGnlAttrbts.ClssfctnTp"
    d = "FinInstrmGnlAttrbts.CmmdtyDerivInd"
    e = "FinInstrmGnlAttrbts.NtnlCcy"
    f = "Issr"

    for x in root.getchildren()[1].getchildren():
        info = x.getchildren()
        a = info[3].text
        b = info[6].text
        c = info[9].text
        d = info[1].text
        e = info[2].text
        f = info[7].text

        print(a + "," + b + "," + c + "," + d + "," + e + "," + f + "\n")
        file.write(a + "," + b + "," + c + "," + d + "," + e + "," + f + "\n")

    file.close()

    return;
