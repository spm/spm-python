from spm.__wrapper__ import Runtime


def _read_asa_vol(*args, **kwargs):
    """
      READ_ASA_VOL reads an ASA volume conductor file  
         
        all data is converted to the following units  
          vertices        mm  
          conductivities  S/m  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_asa_vol.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_asa_vol", *args, **kwargs)
