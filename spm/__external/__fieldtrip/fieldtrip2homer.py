from spm.__wrapper__ import Runtime


def fieldtrip2homer(*args, **kwargs):
    """
      FIELDTRIP2HOMER converts a continuous raw data structure from FieldTrip format to  
        Homer format.  
         
        Use as  
          nirs = fieldtrip2homer(data, ...)  
        where the input data structure is formatted according to the output of  
        FT_PREPROCESSING and the output nirs structure is according to Homer.  
         
        Additional options should be specified in key-value pairs and can be  
          'event'        = event structure that corresponds to the data, see FT_READ_EVENT  
         
        See https://www.nitrc.org/plugins/mwiki/index.php/homer2:Homer_Input_Files#NIRS_data_file_format  
        for a description of the Homer data structure.  
         
        See also HOMER2FIELDTRIP, FT_PREPROCESSING, FT_DATATYPE_RAW  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fieldtrip2homer.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fieldtrip2homer", *args, **kwargs)
