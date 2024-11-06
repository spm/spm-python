from spm.__wrapper__ import Runtime


def hanning(*args, **kwargs):
    """
     HANNING   Hanning window.  
          HANNING(N) returns the N-point symmetric Hanning window in a column  
          vector.  Note that the first and last zero-weighted window samples  
          are not included.  
         
          HANNING(N,'symmetric') returns the same result as HANNING(N).  
         
          HANNING(N,'periodic') returns the N-point periodic Hanning window,  
          and includes the first zero-weighted window sample.  
         
          NOTE: Use the HANN function to get a Hanning window which has the   
                 first and last zero-weighted samples.   
         
          See also BARTLETT, BLACKMAN, BOXCAR, CHEBWIN, HAMMING, HANN, KAISER  
          and TRIANG.  
            
          This is a drop-in replacement to bypass the signal processing toolbox  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/external/signal/hanning.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("hanning", *args, **kwargs)
