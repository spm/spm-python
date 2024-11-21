from spm.__wrapper__ import Runtime


def spm_get_bf(*args, **kwargs):
    """
      Fill in basis function structure  
        FORMAT [xBF] = spm_get_bf(xBF)  
         
        xBF.dt      - time bin length {seconds}  
        xBF.name    - description of basis functions specified  
                      'hrf'  
                      'hrf (with time derivative)'  
                      'hrf (with time and dispersion derivatives)'  
                      'Fourier set'  
                      'Fourier set (Hanning)'  
                      'Gamma functions'  
                      'Finite Impulse Response'  
                      'Cosine set'  
                      (any other specification will default to 'hrf')  
        xBF.length  - window length (seconds)  
        xBF.order   - order  
        xBF.T       - microtime resolution (for 'hrf*')  
         
        xBF.bf      - array of basis functions  
       __________________________________________________________________________  
         
        spm_get_bf prompts for basis functions to model event or epoch-related  
        responses.  The basis functions returned are unitary and orthonormal  
        when defined as a function of peri-stimulus time in time-bins.  
        It is at this point that the distinction between event and epoch-related   
        responses enters.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_get_bf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_get_bf", *args, **kwargs)
