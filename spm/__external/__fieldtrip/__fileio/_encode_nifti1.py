from spm._runtime import Runtime


def _encode_nifti1(*args, **kwargs):
    r"""
     function blob = encode_nifti1(H)  
         
        Encodes a NIFTI-1 header (=> raw 348 bytes (uint8)) from a Matlab structure  
        that matches the C struct defined in nifti1.h.  
         
        WARNING: This function currently ignores endianness !!!  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/encode_nifti1.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("encode_nifti1", *args, **kwargs)
