from spm.__wrapper__ import Runtime


def spm_voice_read(*args, **kwargs):
    """
      Read and translate a sound file or audio source  
        FORMAT [SEG,W,P,R] = spm_voice_read(wfile,[P])  
         
        wfile  - .wav file or audio object or (double) timeseries  
        P      - prior likelihood of lexical content or  
               - number of words to read (N or size(P,2))  
         
        requires the following in the global variable VOX:  
        LEX    - lexical structure array  
        PRO    - prodidy structure array  
        WHO    - speaker structure array  
         
        for each (s-th) word:  
         
        SEG(s).str - lexical class  
        SEG(s).p   - prior  
        SEG(s).L   - posterior  
        SEG(s).W   - lexical class  
        SEG(s).P   - prosody class  
        SEG(s).R   - speaker class  
        SEG(s).I0  - first index  
        SEG(s).IT  - final index  
         
        This routine takes a sound file or audio stream as an input and infers the lexical  
        content and prosody. In then articulates the phrase or  
        sequence of word segments (SEG). If called with no output arguments it  
        generates graphics detailing the segmentation. This routine assumes that  
        all the variables in the VOX structure are set appropriately;  
        especially, the fundamental and first formant frequencies (F0 and F1)  
        appropriate for speaker identity. If called with no inputs, it will  
        create an audio recorder object and record dictation for a few seconds.  
         
        see also: spm_voice_speak.m and spm_voice_segmentation.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_read.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_read", *args, **kwargs)
