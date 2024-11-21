from spm.__wrapper__ import Runtime


def _read_bti_m4d(*args, **kwargs):
    """
      READ_BTI_M4D  
         
        Use as  
          msi = read_bti_m4d(filename)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_bti_m4d.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_bti_m4d", *args, **kwargs)
