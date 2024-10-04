from spm.__wrap__ import _Runtime


def spm_plot_convergence(*args, **kwargs):
  """  Display a plot showing convergence of an optimisation routine.  
    FORMAT spm_plot_convergence('Init',title,ylabel,xlabel)  
    Initialise the plot in the 'Interactive' window.  
     
    FORMAT spm_plot_convergence('Set',value)  
    Update the plot.  
     
    FORMAT spm_plot_convergence('Clear')  
    Clear the 'Interactive' window.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_plot_convergence.m)
  """

  return _Runtime.call("spm_plot_convergence", *args, **kwargs, nargout=0)
