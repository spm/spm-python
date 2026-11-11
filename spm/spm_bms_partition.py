from spm._runtime import Runtime


def spm_bms_partition(*args, **kwargs):
    r"""
      Compute model partitioning for BMS  
        FORMAT spm_bms_partition(BMS)  
         
        Input:  
        BMS structure (BMS.mat)  
         
        Output:  
        PPM (images) for each of the subsets defined  
        xppm_subsetn.img (RFX) and ppm_subsetn.img (FFX)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_bms_partition.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bms_partition", *args, **kwargs, nargout=0)
