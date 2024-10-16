from spm.__wrapper__ import Runtime


def spm_chi2_plot(*args, **kwargs):
  """  Display a plot showing convergence of an optimisation routine.  
    FORMAT spm_chi2_plot('Init',title,ylabel,xlabel)  
    Initialise the plot in the 'Interactive' window.  
     
    FORMAT spm_chi2_plot('Set',value)  
    Update the plot.  
     
    FORMAT spm_chi2_plot('Clear')  
    Clear the 'Interactive' window.  
   __________________________________________________________________________  
     
    This function is deprecated, use SPM_PLOT_CONVERGENCE instead.  
   __________________________________________________________________________  
    Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/compat/spm_chi2_plot.m)
  """

  return Runtime.call("spm_chi2_plot", *args, **kwargs, nargout=0)
