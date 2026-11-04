from spm._runtime import Runtime


def DFP_demo_double_well(*args, **kwargs):
    r"""
      DEMO comparing Variational filtering with particle filtering in the   
        context of a bimodal conditional density.  This demonstrates that the  
        variational filter can not only represent free-form densities on the   
        states but also the causes of responses.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DFP_demo_double_well.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DFP_demo_double_well", *args, **kwargs, nargout=0)
