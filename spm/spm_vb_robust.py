from spm.__wrapper__ import Runtime


def spm_vb_robust(*args, **kwargs):
    """
      Robust GLM modelling in a slice of fMRI  
        FORMAT [slice] = spm_vb_robust (Y,slice)  
         
        Y     -  [T x N] time series with T time points, N voxels  
         
        slice -  data structure containing fields described in spm_vb_glmar.m  
         
        Requires the 'mixture' toolbox: fullfile(spm('Dir'),'toolbox','mixture')  
       __________________________________________________________________________  
         
        Reference:  
        W.D. Penny, J. Kilner and F. Blankenburg. Robust Bayesian General Linear   
        Models. NeuroImage, 36(3):661-671, 2007.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vb_robust.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vb_robust", *args, **kwargs)
