from spm.__wrapper__ import Runtime


def bf_inverse_eloreta(*args, **kwargs):
    """
      Computes eLORETA projectors  
         
        please cite  
        R.D. Pascual-Marqui: Discrete, 3D distributed, linear imaging methods of electric neuronal activity. Part 1: exact, zero  
        error localization. arXiv:0710.3341 [math-ph], 2007-October-17, http://arxiv.org/pdf/0710.3341  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_inverse_eloreta.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_inverse_eloreta", *args, **kwargs)
