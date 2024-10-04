from spm.__wrap__ import _Runtime


def spm_epileptor_demo(*args, **kwargs):
  """  Demo routine for local field potential models  
   ==========================================================================  
      
    This routine illustrates how one can model induced responses (e.g.,  
    seizure onset in terms of exogenously forced changes in model parameters -  
    (e.g., recurrent inhibitory connections in a canonical microcircuit  
    model. This calls on extra parameters X and Y. X couples input to  
    parameters, while Y couples hidden states to parameters.  Here we use  
    exogenous input to change the parameters and the ensuing Jacobian to  
    elicit fast gamma activity.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_epileptor_demo.m)
  """

  return _Runtime.call("spm_epileptor_demo", *args, **kwargs, nargout=0)
