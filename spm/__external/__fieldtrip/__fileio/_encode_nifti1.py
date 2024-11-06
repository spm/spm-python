from spm.__wrapper__ import Runtime


def _encode_nifti1(*args, **kwargs):
    """
     function blob = encode_nifti1(H)  
         
        Encodes a NIFTI-1 header (=> raw 348 bytes (uint8)) from a Matlab structure  
        that matches the C struct defined in nifti1.h.  
         
        WARNING: This function currently ignores endianness !!!  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/encode_nifti1.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("encode_nifti1", *args, **kwargs)
