from spm._runtime import Runtime


def spm_mci_postslices(*args, **kwargs):
    r"""
      Univariate slices through posterior density  
        FORMAT [x,pnum,pgauss] = spm_mci_postslices (post,M,U,Y,Nbins)  
         
        post      posterior data structure  
        M,U,Y     as usual  
        Nbins     Number of bins per dimension  
         
        x         [Np x Nbins] matrix where x(p,:) is domain for pth variable  
        pnum      [Np x Nbins] where pnum(p,j) = p(x(p)=xj|x(\p),Y) ie. the posterior  
                  density of variable p conditioned on the posterior mean of the other  
                  variables. This is estimated numerically from evaluation of log joint  
        pgauss    As pnum but under assumption that posterior is multivariate Gaussian  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_postslices.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_postslices", *args, **kwargs)
