from spm.__wrapper__ import Runtime


def imotions2fieldtrip(*args, **kwargs):
    """
      IMOTIONS2FIELDTRIP imports an iMotions *.txt file and represents it as a FieldTrip  
        raw data structure.  
         
        Use as  
          data = imotions2fieldtrip(filename, ...)  
         
        Additional options should be specified in key-value pairs and can be  
          interpolate   = 'no', 'time' or 'data' (default = 'no')  
          isnumeric     = cell-array with labels corresponding to numeric data (default = {})  
          isinteger     = cell-array with labels corresponding to integer data that should be interpolated with nearest where applicable (default = {})  
          isnotnumeric  = cell-array with labels not corresponding to numeric data (default = {})  
          isevent       = cell-array with labels corresponding to events (default = {})  
          isnotevent    = cell-array with labels not corresponding to events (default = {})  
         
        The options 'isnumeric' and 'isnotnumeric' are mutually exclusive. Idem for  
        'isevent' and 'isnotevent'.  
         
        When using the interpolate='data' option, both the data and the time are interpolated  
        to a regularly sampled representation, when using the interpolate='time' option, only  
        the time axis is interpolated to a regularly sampled representation.  This addresses  
        the case that the data was actually acquired with a regular sampling rate, but the time  
        stamps in the file are not correctly representing this (a known bug with some type of  
        iMotions data).  
         
        See also FT_DATATYPE_RAW, FT_PREPROCESSING, FT_HEARTRATE, FT_ELECTRODERMALACTIVITY  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/imotions2fieldtrip.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("imotions2fieldtrip", *args, **kwargs)
