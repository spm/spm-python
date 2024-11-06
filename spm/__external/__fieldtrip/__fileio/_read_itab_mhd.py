from spm.__wrapper__ import Runtime


def _read_itab_mhd(*args, **kwargs):
    """
    read_itab_mhd is a function.  
          mhd = read_itab_mhd(filename)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_itab_mhd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_itab_mhd", *args, **kwargs)
