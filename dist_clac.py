#-*- coding: utf-8 -*-
import math

def dis_calc(olon, olat, dlon, dlat):
    # gps points
    CurLong = olon
    CurLat = olat
    DesLong = dlon
    DesLat = dlat
    a = 6378137
    b = 6356752
    # ����ת������
    Curlamda = CurLong*math.pi/180
    Curfai = CurLat*math.pi/180
    Deslamda = DesLong*math.pi/180
    Desfai = DesLat*math.pi/180
    # O��
    la = a*math.cos(Curfai)
    lb = b*math.sin(Curfai)
    lc = math.sqrt(la*la + lb*lb) # O�����ľ�
    CurN =(a*b)/lc
    CurX = CurN * math.cos(Curfai)*math.cos(Curlamda)
    CurY = CurN * math.cos(Curfai)*math.sin(Curlamda)
    CurZ = CurN * b*b/a/a*math.sin(Curfai)

    # D��
    la = a*math.cos(Desfai)
    lb = b*math.sin(Desfai)
    lc = math.sqrt(la*la + lb*lb) # D�����ľ�
    DesN =(a*b)/lc
    DesX = DesN *math.cos(Desfai)*math.cos(Deslamda)
    DesY = DesN *math.cos(Desfai)*math.sin(Deslamda)
    DesZ = DesN*b*b/a/a*math.sin(Desfai)

    # OD
    la = DesX - CurX
    lb = DesY - CurY
    lc = DesZ - CurZ

    # distance
    Dis = math.sqrt(la*la + lb*lb + lc*lc)
    return Dis

olon=116.408635
olat=40.0351
dlon=116.408635
dlat=40.0352

print(dis_calc(olon, olat, dlon, dlat))   