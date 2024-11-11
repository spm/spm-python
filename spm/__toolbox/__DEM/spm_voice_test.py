from spm.__wrapper__ import Runtime


def spm_voice_test(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_test.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_test", *args, **kwargs)
