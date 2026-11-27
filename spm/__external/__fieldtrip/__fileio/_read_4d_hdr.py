from spm._runtime import Runtime


def _read_4d_hdr(*args, **kwargs):
    r"""
      hdr=READ_4D_HDR(datafile, configfile)  
        Collects the required Fieldtrip header data from the data file 'filename'  
        and the associated 'config' file for that data.  
         
        Adapted from the MSI>>Matlab code written by Eugene Kronberg  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_4d_hdr.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_4d_hdr", *args, **kwargs)
