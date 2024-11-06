from spm.__wrapper__ import Runtime


def homer2fieldtrip(*args, **kwargs):
    """
      HOMER2FIELDTRIP converts a continuous raw data structure from Homer to FieldTrip  
        format.  
         
        Use as  
          data = homer2fieldtrip(filename)  
        where the input is a file name, or  
          data = homer2fieldtrip(nirs)  
        where the input nirs structure is according to the Homer format and the output data  
        structure is formatted according to the output of FT_PREPROCESSING.  
         
        See https://www.nitrc.org/plugins/mwiki/index.php/homer2:Homer_Input_Files#NIRS_data_file_format  
        for a description of the Homer data structure.  
         
        See also FIELDTRIP2HOMER, FT_PREPROCESSING, FT_DATATYPE_RAW  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/homer2fieldtrip.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("homer2fieldtrip", *args, **kwargs)
