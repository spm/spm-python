from spm._runtime import Runtime


def _read_micromed_trc(*args, **kwargs):
    r"""
     --------------------------------------------------------------------------  
        reads Micromed .TRC file into matlab, version Mariska, edited by Romain  
        input: filename  
        output: datamatrix  
       --------------------------------------------------------------------------  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_micromed_trc.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_micromed_trc", *args, **kwargs)
