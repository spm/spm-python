from spm._runtime import Runtime


def _read_biosig_data(*args, **kwargs):
    r"""
      READ_BIOSIG_DATA reads data from EEG file using the BIOSIG  
        toolbox and returns it in the FCDC framework standard format  
         
        Use as  
         [dat] = read_biosig_data(filename, hdr, begsample, endsample, chanindx)  
        where the header has to be read before with READ_BIOSIG_HEADER.  
         
        The following data formats are supported: EDF, BKR, CNT, BDF, GDF  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_biosig_data.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_biosig_data", *args, **kwargs)
