from spm.__wrapper__ import Runtime


def spm_regions(*args, **kwargs):
    """
      VOI time-series extraction of adjusted data (& local eigenimage analysis)  
        FORMAT [Y,xY] = spm_regions(xSPM,SPM,hReg,[xY])  
         
        xSPM   - structure containing specific SPM, distribution & filtering details  
        SPM    - structure containing generic analysis details  
        hReg   - Handle of results section XYZ registry (see spm_results_ui.m)  
         
        Y      - first scaled eigenvariate of VOI {i.e. weighted mean}  
        xY     - VOI structure  
              xY.xyz          - centre of VOI {mm}  
              xY.name         - name of VOI  
              xY.Ic           - contrast used to adjust data (0 - no adjustment)  
              xY.Sess         - session index  
              xY.def          - VOI definition  
              xY.spec         - VOI definition parameters  
              xY.str          - VOI description as a string  
              xY.XYZmm        - Coordinates of VOI voxels {mm}  
              xY.y            - [whitened and filtered] voxel-wise data  
              xY.u            - first eigenvariate {scaled - c.f. mean response}  
              xY.v            - first eigenimage  
              xY.s            - eigenvalues  
              xY.X0           - [whitened] confounds (including drift terms)  
         
        Y and xY are also saved in VOI_*.mat in the SPM working directory.  
        (See spm_getSPM for details on the SPM & xSPM structures)  
         
        FORMAT [Y,xY] = spm_regions('Display',[xY])  
         
        xY     - VOI structure or filename  
         
       __________________________________________________________________________  
         
        spm_regions extracts a representative time course from voxel data in  
        terms of the first eigenvariate of the filtered and adjusted response in  
        all suprathreshold voxels within a specified VOI centred on the current  
        MIP cursor location. Responses are adjusted by removing variance that  
        can be predicted by the null space of the F contrast specified (usually   
        an F-contrast testing for all effects of interest).  
         
        If temporal filtering has been specified, then the data will be filtered.  
        Similarly for whitening. Adjustment is with respect to the null space of  
        a selected contrast, or can be omitted.  
         
        For a VOI of radius 0, the [adjusted] voxel time-series is returned, and  
        scaled to have a 2-norm of 1. The actual [adjusted] voxel time series can  
        be extracted from xY.y, and will be the same as the [adjusted] data   
        returned by the plotting routine (spm_graph.m) for the same contrast.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_regions.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_regions", *args, **kwargs)
