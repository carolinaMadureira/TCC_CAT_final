import numpy as np
import pandas as pd
import itertools
from datetime import timedelta

from dateutil.relativedelta import *
from datetime import date
from datetime import datetime


def formatarStr (DataFrame, columns):
    for col in columns:
        DataFrame[col] = DataFrame[col].str.strip()
        
        
def verificarStrInvalida (DataFrame, columns, strInvalida):
    print('Dados ausentes, por coluna: ')
    for col in columns:
        f_item = DataFrame[DataFrame[col] == strInvalida].shape[0]  
        print('inválidos em {}: {}'.format(col, f_item))

        
def calcularIdade(dtNasc, dtAcid):
    try:
        if dtNasc == 0 or dtAcid == 0: 
            return np.nan
        else: 
            dtAcid = dtAcid.replace('/','')
            if len(dtAcid) == 8 :            
                dtBase = datetime.strptime(str(dtAcid), '%d%m%Y').date()
            else:
                dtBase = datetime.strptime(str(dtAcid), '%Y%m').date()
            dob = datetime.strptime(str(dtNasc), '%d/%m/%Y').date()
            age = relativedelta(dtBase, dob)
            return age.years
    except (RuntimeError, TypeError, NameError, ValueError):
        return np.nan
    
    
def calcularAnoMes(dtAcid): 
    if len(dtAcid) == 10:
        anoMesStr = dtAcid[6:]+dtAcid[3:5]
        return anoMesStr
    elif len(dtAcid) == 7:
        anoMesStr = dtAcid.replace('/', '')
        return anoMesStr
    else:
        return dtAcid
    
def recortarCNAE(cnaeStr):
    strSeparada = cnaeStr.rsplit(":")
    if len(strSeparada) > 1:
        return strSeparada[0]
    else:
        return cnaeStr
    

def calcularSomaAnoMes(dtStr):
    try: 
        df_soma = df_result.query("anoMes == \""+dtStr+"\"" )
        total= df_soma['qtde'].sum()    
        return total
    except (RuntimeError, TypeError, NameError, ValueError):
        return np.nan
  
