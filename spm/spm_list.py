from spm.__wrapper__ import Runtime


def spm_list(*args, **kwargs):
    """
      Display an analysis of SPM{.}  
        FORMAT TabDat = spm_list('List',xSPM,hReg,[Num,Dis,Str])  
        Summary list of local maxima for entire volume of interest  
        FORMAT TabDat = spm_list('ListCluster',xSPM,hReg,[Num,Dis,Str])  
        List of local maxima for a single suprathreshold cluster  
         
        xSPM    - structure containing SPM, distribution & filtering details  
               - required fields are:  
        .Z     - minimum of n Statistics {filtered on u and k}  
        .n     - number of conjoint tests  
        .STAT  - distribution {Z, T, X or F}  
        .df    - degrees of freedom [df{interest}, df{residual}]  
        .u     - height threshold  
        .k     - extent threshold {voxels}  
        .XYZ   - location of voxels {voxel coords}  
        .S     - search Volume {voxels}  
        .R     - search Volume {resels}  
        .FWHM  - smoothness {voxels}  
        .M     - voxels - > mm matrix  
        .VOX   - voxel dimensions {mm}  
        .DIM   - image dimensions {voxels}  
        .units - space units  
        .VRpv  - filehandle - Resels per voxel  
        .Ps    - uncorrected P values in searched volume (for voxel FDR)  
        .Pp    - uncorrected P values of peaks (for peak FDR)  
        .Pc    - uncorrected P values of cluster extents (for cluster FDR)  
        .uc    - 0.05 critical thresholds for FWEp, FDRp, FWEc, FDRc  
        .thresDesc - description of height threshold (string)  
         
        (see spm_getSPM.m for further details of xSPM structures)  
         
        hReg   - Handle of results section XYZ registry (see spm_results_ui.m)  
         
        Num    - number of maxima per cluster [3]  
        Dis    - distance among clusters {mm} [8]  
        Str    - header string  
         
        TabDat - Structure containing table data  
               - fields are  
        .tit   - table title (string)  
        .hdr   - table header (2x12 cell array)  
        .fmt   - fprintf format strings for table data (1x12 cell array)  
        .str   - table filtering note (string)  
        .ftr   - table footnote information (5x2 cell array)  
        .dat   - table data (Nx12 cell array)  
         
                                  ----------------  
         
        FORMAT spm_list('TxtList',TabDat,c)  
        Prints a tab-delimited text version of the table  
        TabDat - Structure containing table data (format as above)  
        c      - Column of table data to start text table at  
                 (E.g. c=3 doesn't print set-level results contained in columns 1 & 2)  
                                  ----------------  
         
        FORMAT spm_list('SetCoords',xyz,hAx,hReg)  
        Highlighting of table coordinates (used by results section registry)  
        xyz    - 3-vector of new coordinate  
        hAx    - table axis (the registry object for tables)  
        hReg   - Handle of caller (not used)  
       __________________________________________________________________________  
         
        spm_list characterizes SPMs (thresholded at u and k) in terms of  
        excursion sets (a collection of face, edge and vertex connected subsets  
        or clusters).  The corrected significance of the results are based on  
        set, cluster and voxel-level inferences using distributional  
        approximations from the Theory of Gaussian Fields.  These distributions  
        assume that the SPM is a reasonable lattice approximation of a  
        continuous random field with known component field smoothness.  
         
        The p values are based on the probability of obtaining c, or more,  
        clusters of k, or more, resels above u, in the volume S analysed =  
        P(u,k,c).  For specified thresholds u, k, the set-level inference is  
        based on the observed number of clusters C, = P(u,k,C).  For each  
        cluster of size K the cluster-level inference is based on P(u,K,1)  
        and for each voxel (or selected maxima) of height U, in that cluster,  
        the voxel-level inference is based on P(U,0,1).  All three levels of  
        inference are supported with a tabular presentation of the p values  
        and the underlying statistic:  
         
        Set-level     - c    = number of suprathreshold clusters  
                      - P    = prob(c or more clusters in the search volume)  
         
        Cluster-level - k    = number of voxels in this cluster  
                      - Pc   = prob(k or more voxels in the search volume)  
                      - Pu   = prob(k or more voxels in a cluster)  
                      - Qc   = lowest FDR bound for which this cluster would be  
                               declared positive  
         
        Peak-level    - T/F  = Statistic upon which the SPM is based  
                      - Ze   = The equivalent Z score - prob(Z > Ze) = prob(t > T)  
                      - Pc   = prob(Ze or higher in the search volume)  
                      - Qp   = lowest FDR bound for which this peak would be  
                               declared positive  
                      - Pu   = prob(Ze or higher at that voxel)  
         
        Voxel-level   - Qu   = Expd(Prop of false positives among voxels >= Ze)  
         
        x,y,z (mm)    - Coordinates of the voxel  
         
        The table is grouped by regions and sorted on the Ze-variate of the  
        primary maxima.  Ze-variates (based on the uncorrected p value) are the  
        Z score equivalent of the statistic. Volumes are expressed in voxels.  
         
        Clicking on values in the table returns the value to the MATLAB  
        workspace. In addition, clicking on the coordinates jumps the  
        results section cursor to that location. The table has a context menu  
        (obtained by right-clicking in the background of the table),  
        providing options to print the current table as a text table, or to  
        extract the table data to the MATLAB workspace.  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_list.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_list", *args, **kwargs)
