from spm.__wrapper__ import Runtime


def spm_DFP_plot(*args, **kwargs):
    """
      Plot particles for spm_DFP  
        FORMAT spm_DFP_plot(QU,Nt)  
        FORMAT spm_DFP_plot(QU,pU)  
       --------------------------------------------------------------------------  
        QU{t}(p).x{d}  - ensemble of hidden states  
        QU{t}(p).v{d}  - ensemble of causal states  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_DFP_plot.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DFP_plot", *args, **kwargs, nargout=0)
