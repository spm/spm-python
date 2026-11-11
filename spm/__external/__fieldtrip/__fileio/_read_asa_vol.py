from spm._runtime import Runtime


def _read_asa_vol(*args, **kwargs):
    r"""
      READ_ASA_VOL reads an ASA volume conductor file  
         
        all data is converted to the following units  
          vertices        mm  
          conductivities  S/m  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_asa_vol.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_asa_vol", *args, **kwargs)
