from spm.__wrapper__ import Runtime


def _decode_nifti1(*args, **kwargs):
    """
      DECODE_NIFTI1 is a helper function for real-time processing of MRI data  
         
        Use as  
          H = decode_nifti1(blob)  
         
        Decodes a NIFTI-1 header given as raw 348 bytes (uint8) into a Matlab structure  
        that matches the C struct defined in nifti1.h, with the only difference that the  
        variable length arrays "dim" and "pixdim" are cut off to the right size, e.g., the  
        "dim" entry will only contain the relevant elements:  
        dim[0..7]={3,64,64,18,x,x,x,x} in C would become dim=[64,64,18] in Matlab.  
         
        WARNING: This function currently ignores endianness !!!  
         
        See also DECODE_RES4, DECODE_NIFTI1, SAP2MATLAB  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/decode_nifti1.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("decode_nifti1", *args, **kwargs)
