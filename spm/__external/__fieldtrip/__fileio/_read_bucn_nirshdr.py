from spm.__wrapper__ import Runtime


def _read_bucn_nirshdr(*args, **kwargs):
    """
      READ_BUCN_NIRSHDR reads the header information of ASCII-formatted NIRS  
        data acquired with the UCL-BIRKBECK machine and postprocessed by the  
        Paris group. The first line contains the channel labels and the rest of  
        the file contains per line a time sample. The first column specifies the  
        time axis.  
         
        Use as  
          [hdr] = read_bucn_nirshdr(filename)  
         
        See also READ_BUCN_NIRSDATA, READ_BUCN_NIRSEVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_bucn_nirshdr.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_bucn_nirshdr", *args, **kwargs)
