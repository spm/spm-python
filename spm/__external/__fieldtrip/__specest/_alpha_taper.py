from spm.__wrapper__ import Runtime


def _alpha_taper(*args, **kwargs):
    """
      ALPHA_TAPER returns an asymmetric taper that can be used to construct a  
        complex wavelet with the peak at a distance of 0.8 times the cycle length  
        from the end.  
         
        Use as  
          tap = alpha_taper(n, f)  
        where  
          n = number of samples  
          f = frequency of desired wavelet, relative to the sampling frequency  
         
        The taper will be sufficiently long for a wavelet when n>=5/f.  
         
        Example:  
          f = 0.01; % 10 Hz wavelet at 1000 Hz sampling rate  
          plot(alpha_taper(5/f, f)); hold on  
          plot(alpha_taper(5/f, f) .* cos(2*pi*10*(-499:0)/1000), 'r');  
          plot(alpha_taper(5/f, f) .* sin(2*pi*10*(-499:0)/1000), 'g');  
         
        This function implements equation 3 from Mitchell, Baker and Baker (2007);  
        Muscle Responses to Transcranial Stimulation Depend on Background Oscillatory  
        Activity. http://jp.physoc.org/cgi/content/abstract/jphysiol.2007.134031v1  
         
        The original paper contains a typo. The equation 3 in the paper reads  
          W(F,t) = -(5/4)*F*t * exp( (1+(5/4)*F*t) * i*2*pi*F*t )  
        but should read  
          W(F,t) = -(5/4)*F*t * exp( (1+(5/4)*F*t) + i*2*pi*F*t )  
        since then it is equal to  
          W(F,t) = -(5/4)*F*t * exp(1+(5/4)*F*t) * exp(i*2*pi*F*t)  
        which is simply  
          W(F,t) = taper(F,t) * exp(i*2*pi*F*t)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/specest/private/alpha_taper.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("alpha_taper", *args, **kwargs)
