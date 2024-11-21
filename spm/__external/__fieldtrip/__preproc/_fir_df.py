from spm.__wrapper__ import Runtime


def _fir_df(*args, **kwargs):
    """
      FIR_DF computes default and maximum possible transition band width from  
        FIR filter cutoff frequency(ies)  
         
        Use as  
          [df, maxDf] = fir_df(cutoffArray, Fs)  
        where  
          cutoffArray filter cutoff frequency(ies)  
          Fs          sampling frequency in Hz  
         
        Required filter order/transition band width is estimated with the  
        following heuristic: transition band width is 25% of the lower cutoff  
        frequency, but not lower than 2 Hz, where possible (for bandpass,  
        highpass, and bandstop) and distance from passband edge to critical  
        frequency (DC, Nyquist) otherwise.   
         
        See also FIRWS, FIRWSORD, INVFIRWSORD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/preproc/private/fir_df.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fir_df", *args, **kwargs)
