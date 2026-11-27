from spm._runtime import Runtime


def spm_mountaincar_movie(*args, **kwargs):
    r"""
      makes a move for mountain car problem  
        FORMAT spm_mountaincar_movie(DEM)  
         
        see:  
        Gaussian Processes in Reinforcement Learning  
        Carl Edward Rasmussen and Malte Kuss  
        Max Planck Institute for Biological Cybernetics  
        Spemannstraße 38, 72076 T¨ubingen, Germany  
        {carl,malte.kuss}@tuebingen.mpg.de  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_mountaincar_movie.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mountaincar_movie", *args, **kwargs, nargout=0)
