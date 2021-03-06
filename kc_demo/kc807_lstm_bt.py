# -*- coding: utf-8 -*-
'''
TopQuant-简称TQ极宽智能量化回溯分析系统，培训课件-配套教学python课件程序

Top极宽量化(原zw量化)，Python量化第一品牌 
by Top极宽·量化开源团队 2017.10.1 首发

网站： www.TopQuant.vip      www.ziwang.com
QQ群: Top极宽量化1群，124134140
      Top极宽量化2群，650924099
      Top极宽量化3群，450853713
  
'''

import os,arrow,ffn,pickle
import numpy as np
import pandas as pd
import tushare as ts

import plotly as py
import plotly.figure_factory  as pyff

#2
import keras
from keras import initializers,models,layers
from keras.models import Sequential,load_model
from keras.layers import Flatten,Dense, Input, Dropout, Embedding,SimpleRNN,Bidirectional,LSTM,Conv1D, GlobalMaxPooling1D,Activation,MaxPooling1D,GlobalAveragePooling1D
from keras.optimizers import RMSprop
from keras.utils import plot_model

#  TopQuant
import zsys 
import zpd_talib as zta
import ztools as zt
import ztools_tq as ztq
import ztools_bt as zbt
import ztools_sta as zsta
import ztools_str as zstr
import ztools_data as zdat
import ztools_datadown as zddown
import ztools_draw as zdr



#-------------------    

#1 预处理
pd.set_option('display.width', 450)    
pd.set_option('display.float_format', zt.xfloat3)    
pyplt=py.offline.plot      
#---------------

#2 rd.var
print('\n#2,rd.var&model')
fmx0='data/TM_';qx=ztq.ai_varRd(fmx0);

#3
print('\n#3 set.bt.var')
qx.staFun=zsta.lstm010
qx.staVars=[1.0,1.2]
#
qx.trd_buyNum=1000
qx.trd_buyMoney=10000
qx.trd_mode=1
#
qx.usrLevel,qx.trd_nilFlag=5,False
qx.usrMoney0nil=qx.usrMoney0*qx.usrLevel

# 4       
print('\n#4 bt-main')
qx=zbt.bt_main(qx)
#
ztq.tq_prWrk(qx)
zt.prx('\nusrPools',qx.usrPools)  

#--------------
#5
print('\n#5 qx.rw')
fmx0='data/TM2_';ztq.ai_varWr(qx,fmx0)

#
#------------ret
#6
print('\n#6 ret')
#
print('\n#6.1 tq_prTrdlib')      
ztq.tq_prTrdlib(qx)
zt.prx('userPools',qx.usrPools)

print('\n#6.2 tq_usrStkMerge')      
df_usr=ztq.tq_usrStkMerge(qx)
zt.prDF('df_usr',df_usr)

#

print('\n#6.3 tq_usrDatXed')      
df2,k=ztq.tq_usrDatXed(qx,df_usr)
zt.prDF('df2',df2)

#
print('\n#6.4 ret')      
print('ret:',k,'%')
