from spm._runtime import Runtime


def spm_voice_segmentation(*args, **kwargs):
    r"""
      Plot the results of a segmented sound file or audio stream  
        FORMAT [EEG,PST] = spm_voice_segmentation(wfile,SEG)  
         
        wfile      - (double) timeseries, .wav file or audiorecorder object  
         
        SEG(s).str - lexical class  
        SEG(s).p   - prior  
        SEG(s).L   - posterior  
        SEG(s).P   - prosody class  
        SEG(s).R   - speaker class  
        SEG(s).I0  - first index  
        SEG(s).IT  - final index  
         
        EEG        - simulated EEG for each lexical entry  
        PST        - corresponding peristimulus times for plotting  
         
        This routine plots the timeseries after segmentation and word recognition  
        as implemented by spm_voice_read. It also returns simulated belief  
        updating in the form of local field potentials or EEG for simulation  
        purposes.  
         
        EEG and PST are also placed in the global VOX structure.  
         
        see also: spm_voice_read.m  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_voice_segmentation.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_voice_segmentation", *args, **kwargs)
