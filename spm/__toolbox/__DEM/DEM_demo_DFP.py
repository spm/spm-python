from spm._runtime import Runtime


def DEM_demo_DFP(*args, **kwargs):
    r"""
      DEM demo for linear deconvolution:  This demo considers the deconvolution  
        of the responses of a single-input-multiple output input-state-output  
        model (DCM) to disclose the input or causes.  It starts by demonstrating  
        Variational filtering with spm_DFP; this is a stochastic filtering scheme  
        that propagates particles over a changing variational energy landscape   
        such that their sample density can be used to approximate the underlying  
        ensemble or conditional density.  We then repeat the inversion using   
        spm_DEM (i.e., under a Laplace assumption) which involves integrating the  
        path of just one particle (i.e., the mode).  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_demo_DFP.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_demo_DFP", *args, **kwargs, nargout=0)
