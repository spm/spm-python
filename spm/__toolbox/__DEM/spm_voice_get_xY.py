from spm.__wrapper__ import Runtime


def spm_voice_get_xY(*args, **kwargs):
    """
      Create word arrays from sound file exemplars  
        FORMAT [xY,word,NI] = spm_voice_get_xY(PATH)  
         
        PATH      -  directory containing sound files of exemplar words  
         
        xY(nw,ns) -  structure array for ns samples of nw words  
        word(nw)  -  cell array of word names  
        NI(nw,ns) -  numeric array of number of minima  
         
         This routine uses a library of sound files, each containing 32 words  
         spoken with varying prosody. The name of the sound file labels the word  
         in question. These exemplars are then transformed (using a series of  
         discrete cosine and Hilbert transforms) into a set of parameters, which  
         summarise the lexical content and prosody. The inverse transform  
         generates  timeseries that can be played to articulate a word. The  
         transform operates on a word structure xY to create lexical and prosody  
         parameters (Q and P respectively).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_get_xY.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_get_xY", *args, **kwargs)
