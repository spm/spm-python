from spm._runtime import Runtime


def spm_read_hdr(*args, **kwargs):
    r"""
      Read (SPM customised) Analyze header  
        FORMAT [hdr,otherendian] = spm_read_hdr(fname)  
        fname       - .hdr filename  
        hdr         - structure containing Analyze header  
        otherendian - byte swapping necessary flag  
       _______________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/compat/spm_read_hdr.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_read_hdr", *args, **kwargs)
