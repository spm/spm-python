from spm._runtime import Runtime


def _write_nifti2_hdr(*args, **kwargs):
    r"""
      WRITE_NIFTI2_HDR  
         
        Use as  
          write_nifti2_hdr(filename, hdr)  
        where  
          filename   = string  
          hdr        = structure with nifti-2 header information  
         
        See also READ_NIFTI_HDR, READ_CIFTI, WRITE_CIFTI  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/write_nifti2_hdr.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("write_nifti2_hdr", *args, **kwargs, nargout=0)
