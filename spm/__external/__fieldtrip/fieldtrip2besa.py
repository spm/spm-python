from spm.__wrapper__ import Runtime


def fieldtrip2besa(*args, **kwargs):
    """
      FIELDTRIP2BESA saves a FieldTrip data structures to a corresponding BESA file. This  
        export function is based on documentation that was provided by Todor Jordanov of  
        BESA.  
         
        Use as  
          fieldtrip2besa(filename, data)  
        with data as obtained from FT_PREPROCESSING to export single trial data as a  
        set of .avr files.  
         
        Use as  
          fieldtrip2besa(filename, elec)  
        or  
          fieldtrip2besa(filename, grad)  
        with an electrode structure as obtained from FT_READ_SENS to export channel  
        positions to an .elp file.  
         
        Additional key-value pairs can be specified according to  
          channel = cell-array, can be used to make subset and to reorder the channels  
         
        See also FIELDTRIP2SPSS, FIELDTRIP2FIFF  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fieldtrip2besa.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fieldtrip2besa", *args, **kwargs, nargout=0)
