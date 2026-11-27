from spm._runtime import Runtime


def spm_DFP_plot(*args, **kwargs):
    r"""
      Plot particles for spm_DFP  
        FORMAT spm_DFP_plot(QU,Nt)  
        FORMAT spm_DFP_plot(QU,pU)  
       --------------------------------------------------------------------------  
        QU{t}(p).x{d}  - ensemble of hidden states  
        QU{t}(p).v{d}  - ensemble of causal states  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_DFP_plot.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_DFP_plot", *args, **kwargs, nargout=0)
