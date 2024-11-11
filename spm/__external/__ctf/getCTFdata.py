from spm.__wrapper__ import Runtime


def getCTFdata(*args, **kwargs):
    """
       getCTFdata.m   Reads specified trials from .meg4 files in CTF-format data set.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/ctf/getCTFdata.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("getCTFdata", *args, **kwargs)
