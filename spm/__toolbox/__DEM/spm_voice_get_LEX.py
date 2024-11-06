from spm.__wrapper__ import Runtime


def spm_voice_get_LEX(*args, **kwargs):
    """
      Create lexical, prosody and speaker structures from word structures  
        FORMAT [P] = spm_voice_get_LEX(xY,word)  
         
        xY(nw,ns) -  structure array for ns samples of nw words  
        word(nw)  -  cell array of word names  
        NI(nw,ns) -  numeric array of number of minima  
         
        updates or completes the global structure VOX:  
         
        VOX.LEX(nw) -  structure array for nw words (lexical features)  
        VOX.PRO(np) -  structure array for np features of prosody  
        VOX.WHO(nq) -  structure array for nq features of speaker  
         
        P           -  prosody parameters for exemplar (training) words  
         
         This routine creates a triplet of structure arrays used to infer the  
         lexical content and prosody of a word - and the identity of the person  
         talking (in terms of the vocal tract, which determines F1). It uses  
         exemplar word files, each containing 32 words spoken with varying  
         prosody. Each structure contains the expectations and precisions of  
         lexical and prosody parameters (Q and P respectively) - and associated  
         eigenbases. This allows the likelihood of any given word (summarised in  
         a word structure xY)  to be evaluated  under Gaussian assumptions about  
         random fluctuations in parametric space. The identity and prosody  
         likelihoods are based upon the prosody parameters, while the lexical  
         likelihood is based upon the lexical parameters. These (LEX, PRO, and  
         WHO)structures are placed in the VOX structure, which is a global  
         variable. In addition, the expected value of various coefficients are  
         stored in VOX.W and VOX.P.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_get_LEX.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_get_LEX", *args, **kwargs)
