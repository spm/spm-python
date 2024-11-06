from spm.__wrapper__ import Runtime


def flattopwin(*args, **kwargs):
    """
      Author: Paul Kienzle <pkienzle@users.sf.net> (2004)  
        This program is granted to the public domain.  
         
        flattopwin(L, [periodic|symmetric])  
         
        Return the window f(w):  
         
          f(w) = 1 - 1.93 cos(2 pi w) + 1.29 cos(4 pi w)  
                   - 0.388 cos(6 pi w) + 0.0322cos(8 pi w)  
         
        where w = i/(L-1) for i=0:L-1 for a symmetric window, or  
        w = i/L for i=0:L-1 for a periodic window.  The default  
        is symmetric.  The returned window is normalized to a peak  
        of 1 at w = 0.5.  
         
        This window has low pass-band ripple, but high bandwidth.  
         
        According to [1]:  
         
           The main use for the Flat Top window is for calibration, due  
           to its negligible amplitude errors.  
         
        [1] Gade, S; Herlufsen, H; (1987) 'Use of weighting functions in DFT/FFT  
        analysis (Part I)', Bruel & Kjaer Technical Review No.3.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/external/signal/flattopwin.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("flattopwin", *args, **kwargs)
