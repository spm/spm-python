from spm.__wrapper__ import Runtime


def spm_voice_speak(*args, **kwargs):
    """
      Generate a continuous state space word discrete causes  
        FORMAT [xY,Y] = spm_voice_speak(q,p,r)  
         
        q      - lexcial index (2 x number of words)  
        p      - prosody index (8 x number of words)  
        r      - speaker index (2 x number of words)  
         
        requires the following in the global variable VOX:  
        LEX    - lexical structure array  
        PRO    - prodidy structure array  
        WHO    - speaker structure array  
         
        xY.W  -  parameters - lexical  
        xY.P  -  parameters - prosody  
        xY.R  -  parameters - speaker  
         
        Y     -  corresponding timeseries  
         
        This routine recomposes and plays a timeseries, specified as a sequence  
        of words that can be articulated with a particular prosody.  This routine  
        plays the same role as spm_voice_iff but uses the dictionaries supplied  
        by the lexical and prosody structures to enable a categorical  
        specification of a spoken phrase. In other words, it allows one to map  
        from discrete state space of lexical content and prosody to continuous  
        time outcomes.  
         
        see also: spm_voice_iff.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_speak.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_speak", *args, **kwargs)
