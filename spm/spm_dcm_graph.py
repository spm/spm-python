from spm.__wrapper__ import Runtime


def spm_dcm_graph(*args, **kwargs):
    """
      Region and anatomical graph display  
        FORMAT spm_dcm_graph(xY,[A])  
        xY    - cell of region structures (see spm_regions) (fMRI)  
                or ECD locations xY.Lpos and xY.Sname (EEG)  
        A     - connections of weighted directed graph  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_graph.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_graph", *args, **kwargs, nargout=0)
