from spm.__wrapper__ import Runtime


def spm_voice_P300(*args, **kwargs):
    """
      Illustrate voice recognition with lexical priors  
        FORMAT spm_voice_P300  
         
        loads the global variable VOX.mat  
         
        VOX.LEX(w,k) -  structure array for k variants of w words  
        VOX.PRO(p)   -  structure array for p aspects of prosody  
        VOX.WHO(w)   -  structure array for w aspects of idenity  
         
        This routine demonstrates the basic functionality of voice recognition or  
        active listening with a special focus on segmentation and the simulated  
        neurophysiological correlates of belief updating. It starts by  
        demonstrating segmentation; either in response to some spoken sentences  
        (read from prompts in the script or by loading exemplar sentences). It  
        then moves on to demonstrating the effect of changing the precision of  
        prior beliefs about lexical content and how this is expressed in terms of  
        simulated belief updating via the minimisation of variational free  
        energy.  
         
        This routine assumes the necessary files are located in a particular  
        (Sound files) directory; that can be specified by editing the script  
        below.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_P300.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_P300", *args, **kwargs, nargout=0)
