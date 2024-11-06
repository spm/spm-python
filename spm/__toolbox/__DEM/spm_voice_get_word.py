from spm.__wrapper__ import Runtime


def spm_voice_get_word(*args, **kwargs):
    """
      Evaluate the likelihood of the next word in a file or object  
        FORMAT [O,I,J,F] = spm_voice_get_word(wfile,P)  
         
        wfile  - .wav file, audiorecorder object or (double) time series  
        P      - lexical prior probability [optional]  
         
        O{1}   - lexical likelihood (or posterior if priors are specified)  
        O{2}   - prosody likelihood  
        O{3}   - speaker likelihood  
         
        I      - interval index (1/2 sec. before spectral peak)  
        J      - interval onset and offset  
        F      - maxmium F (log evidence)  
         
        requires the following in the global variable VOX:  
         
        LEX    - lexical structure array  
        PRO    - prodidy structure array  
        WHO    - speaker structure array  
        FS     - sampling    frequency (Hz)  
        F0     - fundamental frequency (Hz)  
        IT     - index or pointer to offset of last word (i.e., CurrentSample)  
         
        and updates:  
        IT     - index or pointer to offset of current word  
         
        This routine evaluates the likelihood of a word, prosody and identity by  
        inverting successive epochs of data from an audiofile or device starting  
        at VOX.IT.  Based on the word with the least variational free energy, it  
        updates the index, ready for the next word. Priors over the words can be  
        specified to implement an Occam's window (of 3 nats); thereby  
        restricting the number of lexical entries evaluated - and augmenting the  
        likelihoods to give the posterior probability over words.  
        If called with more than one prior over lexical content, this routine  
        will perform a tree search and return the likelihoods (and intervals)  
        with the path of greatest log evidence (i.e., free energy).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_get_word.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_get_word", *args, **kwargs)
