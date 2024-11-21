from spm.__wrapper__ import Runtime


def _read_4d_hdr(*args, **kwargs):
    """
      hdr=READ_4D_HDR(datafile, configfile)  
        Collects the required Fieldtrip header data from the data file 'filename'  
        and the associated 'config' file for that data.  
         
        Adapted from the MSI>>Matlab code written by Eugene Kronberg  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_4d_hdr.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_4d_hdr", *args, **kwargs)
