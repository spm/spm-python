from spm.__wrapper__ import Runtime


def _prepare_mesh_manual(*args, **kwargs):
    """
      PREPARE_MESH_MANUAL is called by PREPARE_MESH and opens a GUI to manually  
        select points/polygons in an mri dataset.  
         
        It allows:  
          Visualization of 3d data in 3 different projections  
          Adjustment of brightness for every slice  
          Storage of the data points in an external .mat file  
          Retrieval of previously saved data points  
          Slice fast scrolling with keyboard arrows  
          Polygons or points selection/deselection  
         
        See also PREPARE_MESH_SEGMENTATION, PREPARE_MESH_HEADSHAPE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/prepare_mesh_manual.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("prepare_mesh_manual", *args, **kwargs)
