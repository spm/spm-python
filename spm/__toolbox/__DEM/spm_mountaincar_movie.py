from spm.__wrapper__ import Runtime


def spm_mountaincar_movie(*args, **kwargs):
    """
      makes a move for mountain car problem  
        FORMAT spm_mountaincar_movie(DEM)  
         
        see:  
        Gaussian Processes in Reinforcement Learning  
        Carl Edward Rasmussen and Malte Kuss  
        Max Planck Institute for Biological Cybernetics  
        Spemannstraße 38, 72076 T¨ubingen, Germany  
        {carl,malte.kuss}@tuebingen.mpg.de  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_mountaincar_movie.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mountaincar_movie", *args, **kwargs, nargout=0)
