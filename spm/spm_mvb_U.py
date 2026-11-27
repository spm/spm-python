from spm._runtime import Runtime


def spm_mvb_U(*args, **kwargs):
    r"""
      Construct patterns U for Multivariate Bayesian inversion of a linear model  
        FORMAT U = spm_mvb_U(Y,priors,X0,xyz,vox,nu)  
        Y      - data-feature matrix  
        priors - 'null'      % no patterns  
               - 'compact'   % reduced (ns/3); using SVD on local compact support  
               - 'sparse'    % a pattern is a voxel  
               - 'smooth'    % patterns are local Gaussian kernels  
               - 'singular'  % patterns are global singular vectors  
               - 'support'   % the patterns are the images  
         
        X0     - confounds  
        xyz    - location in mm  
        vox    - voxel size in mm  
        nu     - number of patterns (for 'compact')  
         
        U      - pattern or mode weights  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mvb_U.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mvb_U", *args, **kwargs)
