from spm._runtime import Runtime


def _cstructdecode(*args, **kwargs):
    r"""
      CSTRUCTDECODE decodes a structure from a uint8 buffer  
         
        See READ_NEURALYNX_NEV for an example  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/cstructdecode.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cstructdecode", *args, **kwargs)
