from spm.__wrapper__ import Runtime


def spm_hrf(*args, **kwargs):
    """
      Haemodynamic response function  
        FORMAT [hrf,p] = spm_hrf(RT,p,T)  
        RT   - scan repeat time  
        p    - parameters of the response function (two Gamma functions)  
         
                                                                  defaults  
                                                                 {seconds}  
               p(1) - delay of response (relative to onset)          6  
               p(2) - delay of undershoot (relative to onset)       16  
               p(3) - dispersion of response                         1  
               p(4) - dispersion of undershoot                       1  
               p(5) - ratio of response to undershoot                6  
               p(6) - onset {seconds}                                0  
               p(7) - length of kernel {seconds}                    32  
         
        T    - microtime resolution [Default: 16]  
         
        hrf  - haemodynamic response function  
        p    - parameters of the response function  
       __________________________________________________________________________  
         
        The parameters p(1:4) correspond to the shape and scale parameters of two  
        probability density functions of the Gamma distribution (see spm_Gpdf.m),  
        one corresponding to the main response and the other one to the  
        undershoot.  
        Note that the mean of the Gamma distribution is shape*scale and its mode  
        is (shape-1)*scale.  This means that with the default values of the  
        parameters the peak of the heamodynamic response function will be around  
        5 seconds.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_hrf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_hrf", *args, **kwargs)
