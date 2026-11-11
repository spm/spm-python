from spm._runtime import Runtime


def fieldtrip2homer(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fieldtrip2homer.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fieldtrip2homer", *args, **kwargs)
