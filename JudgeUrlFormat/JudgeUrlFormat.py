#-----------------------------------------
#---本程序主要功能为识别url格式--------
#------字典格式较少，欢迎补充----------
#---------欢迎指正和交流----------------
#-----------Author：Vi-------------------
#-----------------------------------------

import requests
import  urllib2
import struct
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')


EXT_JPG = "JPG" 
EXT_PNG = "PNG"
EXT_GIF ="GIF"
EXT_TIF = "TIF"
EXT_BMP = "BMP"
EXT_DWG ="DWG"
EXT_PSD ="PSD"
EXT_RTF ="RTF"
EXT_XML = "XML"
EXT_HTML1 = "HTML"
EXT_HTML2 = "HTML"
EXT_EML = "EML"
EXT_DBX = "DBX"
EXT_PST  = "PST"
EXT_XLS_OR_DOC ="XLS or DOC" 
EXT_MDB = "MDB"
EXT_WPD = "WPD"
EXT_EPS_OR_PS ="EPS or PS"
EXT_PDF = "PDF"
EXT_QDF ="QDF"
EXT_PWL ="PWL"
EXT_ZIP = "ZIP"
EXT_RAR = "RAR"
EXT_WAV = "WAV"
EXT_AVI = "AVI"
EXT_RAM  = "RAM"
EXT_RM ="RM"
EXT_MPG1  = "MPG"
EXT_MPG2 = "MPG"
EXT_MOV = "MOV"
EXT_ASF = "ASF"
EXT_MID  = "MID"
EXT_ART = "ART"
EXT_PCX = "PCX"
EXT_WMF = "WMF"
EXT_EMF ="EMF"
EXT_DWG = "DWG"
EXT_DBX = "DBX"
EXT_EXE = "EXE"

def TypeList():
    return {
        "FFD8FF" : EXT_JPG ,
        "89504E47" : EXT_PNG ,
        "47494638" : EXT_GIF ,
        "49492A00" : EXT_TIF ,
        "424D" : EXT_BMP ,
        "41433130" : EXT_DWG ,
        "38425053" : EXT_PSD ,
        "7B5C727466" : EXT_RTF ,
        "3C3F786D6C" : EXT_XML ,
        "3C68746D6C3E" : EXT_HTML1 ,
        "3C21444F43545950452068746D6C3E" : EXT_HTML2,
        "44656C69766572792D646174653A" : EXT_EML ,
        "CFAD12FEC5FD746F" : EXT_DBX ,
        "2142444E" : EXT_PST ,
        "D0CF11E0" : EXT_XLS_OR_DOC , 
        "5374616E64617264204A" : EXT_MDB ,
        "FF575043" : EXT_WPD ,
        "252150532D41646F6265" : EXT_EPS_OR_PS ,
        "255044462D312E" : EXT_PDF ,
        "AC9EBD8F" : EXT_QDF ,
        "E3828596" : EXT_PWL ,
        "504B0304" : EXT_ZIP ,
        "52617221" : EXT_RAR ,
        "57415645" : EXT_WAV ,
        "41564920" : EXT_AVI ,
        "2E7261FD" : EXT_RAM ,
        "2E524D46" : EXT_RM ,
        "000001BA" : EXT_MPG1 ,
        "000001B3" : EXT_MPG2 ,
        "6D6F6F76" : EXT_MOV ,
        "3026B2758E66CF11" : EXT_ASF ,
        "4D546864" : EXT_MID  ,
        "4A47030E000000" : EXT_ART,
        "0A050108" : EXT_PCX,
        "D7CDC69A" : EXT_WMF,
        "01000900" : EXT_WMF,
        "02000900" : EXT_WMF,
        "0100000058000000" : EXT_EMF,
        "41433130" : EXT_DWG,
        "CFAD12FE" : EXT_DBX,
        "4D5A" : EXT_EXE,
        #"01000900" : EXT_WMF,        
        #"01000900" : EXT_WMF,
        #"01000900" : EXT_WMF,
    }

def Bytes2hex(bytes):
    num = len (bytes)
    hexstr = u""
    for i in range(num):
        t = u"%x" % bytes[i]
        if len(t) % 2:
            hexstr += u"0"
        hexstr += t
    return hexstr.upper()

def FileType(path):
    myfile = open (path , 'rb')
    tl = TypeList()
    ftype = 'unknown'
    for hcode in tl.keys():
        numbytes = len(hcode) / 2 #需要读的字节数
        myfile.seek(0)
        hbytes = struct.unpack_from("B" * numbytes, myfile.read(numbytes))
        f_hcode = Bytes2hex(hbytes)
        if f_hcode == hcode:
            ftype = tl[hcode]
            break
    myfile.close()
    return ftype

def main():
    file = open ("url.txt") 
    f = open("FormatInfo.txt","a+")
    while (True):
        lines = file.readlines()
        if not lines:
            break
        for line in lines:
            url = line.strip('\n')
            #url = raw_input("请输入链接地址：") 
            #filename = url[url.rindex("/")+1:url.rindex(".")]
            if "." in url:
                b = url[-1]
                if b=="/":
                    suffix = "NO-SUFFIX"
                else:
                    suffix = url[url.rindex("."):]
            else:
                suffix = "NO-SUFFIX"
            #   filename = userl[url.rindex("/"):]
            #folder = os.getcwd()
            try:
                r=requests.get(url,timeout=1)
            except:
                continue
            path="E:\\Download\\info" #+ filename + ext
            with open(path,"wb") as code:
                code.write(r.content) 
            try:
                f.write("URL:"+url+", SUFFIX:"+suffix+", FORMAT:"+FileType(path))
                f.write("\n")
                print "URL: %s , SUFFIX : %s , 格式：%s"  % (url , suffix , FileType(path))
            except:
                print "Can't read the type of %s"%url
        print "已将url格式信息写入FormatInfo.txt"
    os.remove(path)
    file.close()
    f.close() 
    
if __name__ == '__main__': 
    print "正在识别,请稍等..."
    main()
       
sys.exit()