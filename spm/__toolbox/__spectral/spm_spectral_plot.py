from spm._runtime import Runtime


def spm_spectral_plot(*args, **kwargs):
    """
      subplot for spectral arrays  
        FORMAT spm_spectral_plot(Hz,csd,str,xlab,ylab)  
         
        str  - format (default: '-')  
        xlab - xlabel (default: 'Hz')  
        ylab - ylabel (default: 'power')  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_spectral_plot.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_spectral_plot", *args, **kwargs, nargout=0)
