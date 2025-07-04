from spm._runtime import Runtime


def _project_elec(*args, **kwargs):
    """
      PROJECT_ELEC projects electrodes on a triangulated surface  
        and returns triangle index, la/mu parameters and distance  
         
        Use as  
          [el, prj] = project_elec(elc, pnt, tri)  
        which returns   
          el    = Nx4 matrix with [tri, la, mu, dist] for each electrode  
          prj   = Nx3 matrix with the projected electrode position  
         
        See also TRANSFER_ELEC  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/project_elec.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("project_elec", *args, **kwargs)
