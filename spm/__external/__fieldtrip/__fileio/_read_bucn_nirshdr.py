from spm._runtime import Runtime


def _read_bucn_nirshdr(*args, **kwargs):
    r"""
      READ_BUCN_NIRSHDR reads the header information of ASCII-formatted NIRS  
        data acquired with the UCL-BIRKBECK machine and postprocessed by the  
        Paris group. The first line contains the channel labels and the rest of  
        the file contains per line a time sample. The first column specifies the  
        time axis.  
         
        Use as  
          [hdr] = read_bucn_nirshdr(filename)  
         
        See also READ_BUCN_NIRSDATA, READ_BUCN_NIRSEVENT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_bucn_nirshdr.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_bucn_nirshdr", *args, **kwargs)
