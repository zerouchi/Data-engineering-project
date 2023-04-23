from lxml import objectify
import pandas as pd


def xmlTOcsv(file_path):
    #parse the xml document with an input of path to the file
    xml = objectify.parse(open(file_path))
    #storing root of xml tree in root variable
    root = xml.getroot()

    #creating a empty csv file and opening it to write
    filename = "asses.csv"
    file = open(filename, "w")
    
    #initializing headers and wrinting in the empty file
    headers = "FinInstrmGnlAttrbts.Id, FinInstrmGnlAttrbts.FullNm,FinInstrmGnlAttrbts.ClssfctnTp,FinInstrmGnlAttrbts.CmmdtyDerivInd,FinInstrmGnlAttrbts.NtnlCcy,Issr \n"
    file.write(headers)
     
    # as we cannot pass header name as variable in the loop hence we saved the headers in the variable named a,b,c,d,e,f
    a = "FinInstrmGnlAttrbts.Id"
    b = "FinInstrmGnlAttrbts.FullNm"
    c = "FinInstrmGnlAttrbts.ClssfctnTp"
    d = "FinInstrmGnlAttrbts.CmmdtyDerivInd"
    e = "FinInstrmGnlAttrbts.NtnlCcy"
    f = "Issr"

    #initializing loop to  write the info in the empty csv we previously created 
    #x is the doc elements present in the xml file which we have to extract
    for x in root.getchildren()[1].getchildren():
        info = x.getchildren()
        a = info[3].text
        b = info[6].text
        c = info[9].text
        d = info[1].text
        e = info[2].text
        f = info[7].text
        
        #writing the info to the empty file
        file.write(a + "," + b + "," + c + "," + d + "," + e + "," + f + "\n")

    file.close()

    return;


#to call the function you cannot pass the path directly
# first store the path in a variable then pass the variable as input to the function
# for exmple:
    #file_path = 'E:\DataScience_projects\steeleyeAsses\XML_file\\asses.xml'
    #xmlTOcsv(file_path)
