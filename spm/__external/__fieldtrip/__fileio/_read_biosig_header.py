from spm._runtime import Runtime


def _read_biosig_header(*args, **kwargs):
    r"""
      READ_BIOSIG_HEADER reads header from EEG file using the BIOSIG  
        toolbox and returns it in the FCDC framework standard format  
         
        Use as  
         [hdr] = read_biosig_header(filename)  
         
        The following data formats are supported: EDF, BKR, CNT, BDF, GDF,  
        see for full documentation http://biosig.sourceforge.net/  
         
        See also READ_BIOSIG_DATA  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_biosig_header.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_biosig_header", *args, **kwargs)
