from spm.__wrapper__ import Runtime


def _read_biosig_data(*args, **kwargs):
    """
      READ_BIOSIG_DATA reads data from EEG file using the BIOSIG  
        toolbox and returns it in the FCDC framework standard format  
         
        Use as  
         [dat] = read_biosig_data(filename, hdr, begsample, endsample, chanindx)  
        where the header has to be read before with READ_BIOSIG_HEADER.  
         
        The following data formats are supported: EDF, BKR, CNT, BDF, GDF  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_biosig_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_biosig_data", *args, **kwargs)
