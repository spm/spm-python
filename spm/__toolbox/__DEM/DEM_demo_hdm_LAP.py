from spm.__wrapper__ import Runtime


def DEM_demo_hdm_LAP(*args, **kwargs):
    """
      Demo for Hemodynamic deconvolution: Cross-validation of Laplace scheme  
       __________________________________________________________________________  
        This demonstration compares generalised filtering and DEM in the context  
        of a nonlinear convolution model using empirical data. These are the data  
        used to illustrate hemodynamic deconvolution. We have deliberately made  
        the problem difficult here to highlight the ability of Generalised  
        filtering to accumulate evidence to optimise in parameters and hyper-  
        parameters, which allows it to outperform DEM (although it does not  
        find visual motion effects with 90% confidence)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_hdm_LAP.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_hdm_LAP", *args, **kwargs, nargout=0)
