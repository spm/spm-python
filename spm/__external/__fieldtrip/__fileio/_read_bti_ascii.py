from spm._runtime import Runtime


def _read_bti_ascii(*args, **kwargs):
    r"""
      READ_BTI_ASCII reads general data from a BTI configuration file  
         
        The file should be formatted like  
           Group:  
             item1 : value1a value1b value1c  
             item2 : value2a value2b value2c  
             item3 : value3a value3b value3c  
             item4 : value4a value4b value4c  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_bti_ascii.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_bti_ascii", *args, **kwargs)
