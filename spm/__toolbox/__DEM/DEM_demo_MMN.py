from spm.__wrapper__ import Runtime


def DEM_demo_MMN(*args, **kwargs):
    """
      This Demo uses the linear convolution model of previous examples to  
        simulate chirps (c.f., the bird song demos). By presenting a train of  
        chirps and changing the stimulus after a couple of presentations, we can  
        simulate a roving oddball paradigm used in ERP research. Critically, we  
        hope to see a more exuberant response to the first presentation of a  
        novel chirp (oddball) relative to the same stimulus after learning  
        (standard).  The simulation shows that although veridical percepts obtain  
        from variational de-convolution, the prediction error continues to fall  
        with repetition (as the parameters are optimised). This repetition  
        suppression subtends a mismatch response that has many of the  
        characteristics of the well-known mismatch negativity (MMN).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_MMN.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_MMN", *args, **kwargs, nargout=0)
