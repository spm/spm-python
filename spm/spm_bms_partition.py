from spm.__wrapper__ import Runtime


def spm_bms_partition(*args, **kwargs):
    """
      Compute model partitioning for BMS  
        FORMAT spm_bms_partition(BMS)  
         
        Input:  
        BMS structure (BMS.mat)  
         
        Output:  
        PPM (images) for each of the subsets defined  
        xppm_subsetn.img (RFX) and ppm_subsetn.img (FFX)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_bms_partition.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_bms_partition", *args, **kwargs, nargout=0)
