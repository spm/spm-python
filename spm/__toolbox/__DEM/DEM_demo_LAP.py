from spm.__wrapper__ import Runtime


def DEM_demo_LAP(*args, **kwargs):
    """
      This demonstration compares Generalised filtering under the Laplace  
        assumption (spm_LAP) with variational filtering under the same fixed form  
        approximation (i.e. DEM). We use a simple linear convolution model to  
        illustrate the differences and similarities. The key difference between  
        the two schemes lies (in this example) lies in estimates of conditional  
        uncertainty. spm_LAP is must less over-confident because it eschews the  
        means-field approximation implicit in DEM. The demonstration addresses   
        quadruple estimation of hidden states, exogenous input, parameters and   
        log-precisions (and, for spm_LAP, log-smoothness)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_LAP.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_LAP", *args, **kwargs, nargout=0)
