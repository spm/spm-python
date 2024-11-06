from spm.__wrapper__ import Runtime


def ft_defacemesh(*args, **kwargs):
    """
      FT_DEFACEMESH allows you to de-identify a scalp surface mesh by erasing specific  
        regions, such as the face and ears. The interactive graphical user interface allows  
        you to position a box over the anatomical data inside which all vertices will be  
        removed. You might have to call this function multiple times when both face and  
        ears need to be removed. Following defacing, you should check the result with  
        FT_PLOT_MESH.  
         
        Use as  
          mesh = ft_defacemesh(cfg, mesh)  
         
        The configuration can contain the following options  
          cfg.method     = string, specification of the shape that is used   
                           as a boundary for exclusion, can be either 'box' or 'plane' (default = 'box')  
          cfg.translate  = initial position of the center of the box, or a point on the plane (default = [0 0 0])  
          cfg.scale      = initial size of the box along each dimension (default is automatic)  
          cfg.rotate     = initial rotation of the box, or the plane (default = [0 0 0])  
          cfg.selection  = which vertices to keep, can be 'inside' or 'outside' (default = 'outside')  
         
        See also FT_ANONYMIZEDATA, FT_DEFACEVOLUME, FT_ANALYSISPIPELINE, FT_PLOT_MESH  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_defacemesh.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_defacemesh", *args, **kwargs)
