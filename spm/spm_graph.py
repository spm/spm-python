from spm.__wrapper__ import Runtime


def spm_graph(*args, **kwargs):
    """
      Return adjusted data for a given voxel location  
        FORMAT [Y,y,beta,Bcov,G] = spm_graph(SPM,XYZ,xG)  
         
        SPM    - structure containing generic details about the analysis  
        XYZ    - [x y z]' coordinates {voxel}  
        xG     - structure containing details about action to perform  
          .def - string describing data type to be returned. One of:  
                  'Contrast estimates and 90% C.I.'  
                  'Fitted responses'  
                  'Event-related responses'  
                  'Parametric responses'  
                  'Volterra Kernels'  
          .spec - structure containing specific details about returned data  
         
        Y      - fitted   data for the selected voxel  
        y      - adjusted data for the selected voxel  
        beta   - parameter estimates (ML or MAP)  
        Bcov   - covariance of parameter estimates (ML or conditional)  
        G      - structure containing further data depending on xG details  
         
        See spm_graph_ui for details.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_graph.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_graph", *args, **kwargs)
