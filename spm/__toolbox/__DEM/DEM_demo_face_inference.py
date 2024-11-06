from spm.__wrapper__ import Runtime


def DEM_demo_face_inference(*args, **kwargs):
    """
      Recognising facial expressions: This demo uses the linear convolution  
        model with two hidden states and one cause to generate coefficients of  
        visual basis functions that produce a moving face. The basis functions are  
        images have been chosen so that the appropriate nonlinear mixture creates  
        a smile. The coefficients of the i-th basis image is   
         
        cos((i - 1)*pi*g(x))  
         
        where g(x) is some none linear mixture of hidden sates that lies in the  
        range [0,1]. (neutral to smiling). Inversion of this model corresponds to  
        nonlinear Bayesian de-convolution of visual input to recognise the dynamic  
        expressions. The associated (roving MMN) demonstration uses this  
        generative model to illustrate perceptual learning and repetition suppression  
        when we repeat the stimulus.  Clicking on the images will display the  
        movies entailed by the true and estimated causes.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_face_inference.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_face_inference", *args, **kwargs, nargout=0)
