from spm._runtime import Runtime


def _decode_fif(*args, **kwargs):
    r"""
      DECODE_FIF is a helper function for real-time processing of Neuromag data. This  
        function is used to decode the content of the optional neuromag_fif chunk(s).  
         
        See also DECODE_RES4, DECODE_NIFTI1, SAP2MATLAB  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/decode_fif.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("decode_fif", *args, **kwargs)
