from spm._runtime import Runtime


def spm_voice_test(*args, **kwargs):
    r"""
      Read and translate a sound file to assess recognition accuracy  
        FORMAT [L] = spm_voice_test(wfile,sfile)  
         
        wfile   - .wav file  
        sfile   - .txt file  
         
        rqeuires  
        VOX.LEX - lexical structure array  
        VOX.PRO - prodidy structure array  
        VOX.WHO - speaker structure array  
         
        L       - accuracy (log likelihood)  
         
         This routine tests, recognition on a small test corpus specified in  
         terms of a sound file and text file of successive words. It assesses  
         the accuracy of inference in relation to the known words and then plays  
         them back with and without prosody (or lexical content)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_voice_test.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_voice_test", *args, **kwargs)
