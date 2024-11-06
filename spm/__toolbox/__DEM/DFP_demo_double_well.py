from spm.__wrapper__ import Runtime


def DFP_demo_double_well(*args, **kwargs):
    """
      DEMO comparing Variational filtering with particle filtering in the   
        context of a bimodal conditional density.  This demonstrates that the  
        variational filter can not only represent free-form densities on the   
        states but also the causes of responses.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DFP_demo_double_well.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DFP_demo_double_well", *args, **kwargs, nargout=0)
