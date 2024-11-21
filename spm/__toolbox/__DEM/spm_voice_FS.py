from spm.__wrapper__ import Runtime


def spm_voice_FS(*args, **kwargs):
    """
      Sampling frequency and function handle for handling sound signals  
        FORMAT [FS,read] = spm_voice_FS(wfile)  
         
        wfile  - .wav file, audio object or (double) timeseries  
         
        FS     - sampling frequency  
        read   - function handle: Y = read(wfile);  
         
         This auxiliary routine finds the sampling frequency and returns a  
         function handle appropriate for the sound format in question.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_FS.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_FS", *args, **kwargs)
