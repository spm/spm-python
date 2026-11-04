from spm._runtime import Runtime


def _swapmemfile(*args, **kwargs):
    r"""
      SWAPMEMFILE swaps a variable from file into memory and clears it   
        again from the memory on the subsequent call  
         
        Use with extreme caution!  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/swapmemfile.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("swapmemfile", *args, **kwargs)
