from spm.__wrapper__ import Runtime


def spm_voice_get_next(*args, **kwargs):
    """
      Evaluate the likelihood of the next word in a file or object  
        FORMAT [Y,I,FS] = spm_voice_get_next(wfile)  
         
        wfile  - .wav file, audiorecorder object or (double) time series  
         
        Y      - timeseries  
        I      - Index prior to spectral peak  
        FS     - sampling frequency  
         
        This routine finds the index 500 ms before the next spectral peak in a  
        file, timeseries (Y) or audio object. It filters  successive (one second)  
        epochs with a Gaussian kernel of width VOX.C to identify peaks greater  
        than VOX.U. if no such peak exists it advances for 500 ms (at most four  
        times)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_get_next.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_get_next", *args, **kwargs)
