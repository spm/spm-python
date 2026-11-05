from spm._runtime import Runtime


def _decode_res4(*args, **kwargs):
    r"""
      DECODE_RES4 is a helper function for real-time processing of CTF data. This  
        function is used to decode the content of the optional ctf_res4 chunck.  
         
        See also DECODE_FIF, DECODE_NIFTI1, SAP2MATLAB  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/decode_res4.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("decode_res4", *args, **kwargs)
