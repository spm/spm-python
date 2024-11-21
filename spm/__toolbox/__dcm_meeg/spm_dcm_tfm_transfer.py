from spm.__wrapper__ import Runtime


def spm_dcm_tfm_transfer(*args, **kwargs):
    """
      Display time-frequency modulation transfer functions  
        FORMAT spm_dcm_tfm_transfer(dtf,pst,Hz)  
          
        dtf - (t x w x n x u): an array over t time bins, w frequency bins,  
                               n channels and u inputs  
        pst - peristimulus time (seconds)  
        Hz  - frequency range (Hz)  
       __________________________________________________________________________  
         
        This routine displays complex modulation transfer functions over   
        peristimulus time as images of the absolute values and first order  
        kernels mapping from endogenous inputs to neuronal states  
         
        See also: spm_dcm_tfm_responses (and spm_dcm_tfm_image)   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_tfm_transfer.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_tfm_transfer", *args, **kwargs, nargout=0)
