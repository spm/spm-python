from spm._runtime import Runtime


def spm_plot_convergence(*args, **kwargs):
    r"""
      Display a plot showing convergence of an optimisation routine.  
        FORMAT spm_plot_convergence('Init',title,ylabel,xlabel)  
        Initialise the plot in the 'Interactive' window.  
         
        FORMAT spm_plot_convergence('Set',value)  
        Update the plot.  
         
        FORMAT spm_plot_convergence('Clear')  
        Clear the 'Interactive' window.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_plot_convergence.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_plot_convergence", *args, **kwargs, nargout=0)
