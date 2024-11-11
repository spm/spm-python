from spm.__wrapper__ import Runtime


def spm_delays_demo(*args, **kwargs):
    """
      Demo routine for induced responses  
       ==========================================================================  
         
        This routine illustrates the Taylor approximation to delay differential  
        equation solvers using two (extrinsically connected) neural masses. In  
        this simulation, using a canonical microcircuit model, exogenous inputs  
        are applied to two sources with a unidirectional (forward) connection.  
        The responses of those regions are summarised in terms of their  
        first-order Volterra kernels, under different conduction delays from the  
        source to the target. The effect of these delays can then be seen as a  
        translation of the forward curve and (or impulse response of the target   
        to perturbations of the source.  
          
        See also:  
         spm_dcm_delay.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_delays_demo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_delays_demo", *args, **kwargs, nargout=0)
