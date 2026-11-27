from spm._runtime import Runtime


def spm_seizure_demo(*args, **kwargs):
    r"""
      Demo routine for local field potential models  
       ==========================================================================  
          
        This routine illustrates how one can model induced responses (e.g.,  
        seizure onset in terms of exogenously forced changes in model parameters -  
        (e.g., recurrent inhibitory connections in a canonical microcircuit  
        model. This calls on extra parameters X and Y. X couples input to  
        parameters, while Y couples hidden states to parameters.  Here we use  
        exogenous input to change the parameters and the ensuing Jacobian to  
        elicit fast gamma activity.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Neural_Models/spm_seizure_demo.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_seizure_demo", *args, **kwargs, nargout=0)
