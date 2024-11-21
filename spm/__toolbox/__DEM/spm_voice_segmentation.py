from spm.__wrapper__ import Runtime


def spm_voice_segmentation(*args, **kwargs):
    """
      Plot the results of a segmented sound fileor audio stream  
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_segmentation.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_segmentation", *args, **kwargs)
