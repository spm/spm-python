from spm.__wrapper__ import Runtime


def spm_voice(*args, **kwargs):
    """
      Create lexical and prosody cell arrays from sound file exemplars  
        FORMAT spm_voice(PATH)  
         
        PATH         -  directory containing sound files of exemplar words  
                        (and a test.wav file in a subdirectory /test)  
         
        saves VOX.mat  
         
        VOX.LEX(w,k) -  structure array for k variants of w words  
        VOX.PRO(p)   -  structure array for p aspects of prosody  
        VOX.WHO(w)   -  structure array for w aspects of idenity  
         
         This routine creates structure arrays used to infer the lexical class,  
         prosody and speaker identity of a word. It uses a library of sound  
         files, each containing 32 words spoken with varying prosody. The name of  
         the sound file labels the word in question. These exemplars are then  
         transformed (using a series of discrete cosine transforms) into a set of  
         parameters, which summarise the lexical content and prosody. The inverse  
         transform generates  timeseries that can be played to articulate a word.  
         The transform operates on a word structure xY to create lexical and  
         prosody parameters (Q and P respectively). The accuracy of  lexical  
         inference (i.e., voice the word recognition) is assessed  using the  
         exemplar (training) set and a narrative sound file called '../test.wav'  
         (and associated '../test.txt'). The operation of each subroutine can be  
         examined using graphical outputs by selecting the appropriate options in  
         a voice recognition specific global variable VOX. this structure is  
         saved in the sound file for subsequent use.  
         
         Auxiliary routines will be found at the end of the script. These include  
         various optimisation schemes and illustrations of online voice  
         recognition  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice", *args, **kwargs, nargout=0)
