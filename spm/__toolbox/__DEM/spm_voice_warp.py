from spm.__wrapper__ import Runtime


def spm_voice_warp(*args, **kwargs):
    """
      Resample a vector to normalise the phase at a particular frequency  
        FORMAT [I] = spm_voice_warp(Y,N)  
         
        Y    - timeseries  
        N    - number of cycles (i.e., scale of normalisation)  
         
        I    - resampling indices  
         
        This auxiliary routine returns the indices of a vector that realigns the phase,  
        following a Hilbert transform at a frequency of N cycles per vector  
        length; i.e., warps the vector to normalise the phase at a specified  
        scalable frequency  
          
        This routine is not actually used but is retained for reference  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_warp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_warp", *args, **kwargs)
