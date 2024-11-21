from spm.__wrapper__ import Runtime


def spm_results_ui(*args, **kwargs):
    """
      User interface for SPM/PPM results: Display and analysis of regional effects  
        FORMAT [hReg,xSPM,SPM] = spm_results_ui('Setup',[xSPM])  
         
        hReg   - handle of MIP XYZ registry object  
                 (see spm_XYZreg.m for details)  
        xSPM   - structure containing specific SPM, distribution & filtering details  
                 (see spm_getSPM.m for contents)  
        SPM    - SPM structure containing generic parameters  
                 (see spm_spm.m for contents)  
         
        NB: Results section GUI CallBacks use these data structures by name,  
            which therefore *must* be assigned to the correctly named variables.  
       __________________________________________________________________________  
         
        The SPM results section is for the interactive exploration and  
        characterisation of the results of a statistical analysis.  
         
        The user is prompted to select a SPM{T} or SPM{F}, that is thresholded at  
        user specified levels. The specification of the contrasts to use and the  
        height and size thresholds are described in spm_getSPM.m. The resulting  
        SPM is then displayed in the Graphics window as a maximum intensity  
        projection, alongside the design matrix and contrasts employed.  
         
        The cursors in the MIP can be moved (dragged) to select a particular  
        voxel. The three mouse buttons give different drag and drop behaviour:  
        Button 1 - point & drop; Button 2 - "dynamic" drag & drop with  
        coordinate & SPM value updating; Button 3 - "magnetic" drag & drop,  
        where the cursor jumps to the nearest suprathreshold voxel in the MIP,  
        and shows the value there.  
        See spm_mip_ui.m, the MIP GUI handling function for further details.  
         
        The design matrix and contrast pictures are "surfable": Click and drag  
        over the images to report associated data. Clicking with different  
        buttons produces different results. Double-clicking extracts the  
        underlying data into the base workspace.  
        See spm_DesRep.m for further details.  
         
        The current voxel specifies the voxel, suprathreshold cluster, or  
        orthogonal planes (planes passing through that voxel) for subsequent  
        localised utilities.  
         
        A control panel in the Interactive window enables interactive exploration  
        of the results.  
         
        p-values buttons:  
          (i) volume   - Tabulates p-values and statistics for entire volume.  
                                                   - see spm_list.m  
         (ii) cluster  - Tabulates p-values and statistics for nearest cluster.  
                       - Note that the cursor will jump to the nearest  
                         suprathreshold voxel, if it is not already at a  
                         location with suprathreshold statistic.  
                                                   - see spm_list.m  
        (iii)  S.V.C   - Small Volume Correction:  
                         Tabulates p-values corrected for a small specified  
                         volume of interest. (Tabulation by spm_list.m)  
                                                   - see spm_VOI.m  
         
        Data extraction buttons:  
        Eigenvariate/CVA  
                       - Extracts the principal eigenvariate for small volumes   
                         of interest; or CVA of data within a specified volume  
                       - Data can be adjusted or not for eigenvariate summaries  
                       - If temporal filtering was specified (fMRI), then it is  
                         the filtered data that is returned.  
                       - Choose a VOI of radius 0 to extract the (filtered &)  
                         adjusted data for a single voxel. Note that this vector  
                         will be scaled to have a 2-norm of 1. (See spm_regions.m  
                         for further details.)  
                       - The plot button also returns fitted and adjusted  
                         (after any filtering) data for the voxel being plotted.)  
                       - Note that the cursor will jump to the nearest voxel for  
                         which raw data was saved.  
                                                   - see spm_regions.m  
         
        Visualisation buttons:  
          (i) plot     - Graphs of adjusted and fitted activity against  
                         various ordinates.  
                       - Note that the cursor will jump to the nearest  
                         suprathreshold voxel, if it is not already at a  
                         location with suprathreshold statistic.  
                       - Additionally, returns fitted and adjusted data to the  
                         MATLAB base workspace.  
                                                      - see spm_graph.m  
         (ii) overlays - Popup menu: Overlays of filtered SPM on a structural image  
            -   slices - Slices of the thresholded statistic image overlaid  
                         on a secondary image chosen by the user. Three  
                         transverse slices are shown, being those at the  
                         level of the cursor in the z-axis and the two  
                         adjacent to it.           - see spm_transverse.m  
            - sections - Orthogonal sections of the thresholded statistic  
                         image overlaid on a secondary image chosen by the user.  
                         The sections are through the cursor position.  
                                                   - see spm_sections.m  
            -   render - Render blobs on previously extracted cortical surface  
                                                   - see spm_render.m  
        (iii) save     - Write out thresholded SPM as image  
                                                   - see spm_write_filtered.m  
         
        The current cursor location can be set by editing the coordinate widgets  
        at the bottom of the Interactive window. (Note that many of the results  
        section facilities are "linked" and can update coordinates. E.g.  
        clicking on the coordinates in a p-value listing jumps to that location.)  
         
        Graphics appear in the bottom half of the Graphics window, additional  
        controls and questions appearing in the Interactive window.  
         
                                  ----------------  
         
        The MIP uses a template outline in MNI space. Consequently for the  
        results section to display properly the input images to the statistics  
        section should be in MNI space.  
         
        Similarly, secondary images should be aligned with the input images used  
        for the statistical analysis.  
         
                                  ----------------  
         
        In addition to setting up the results section, spm_results_ui.m sets  
        up the results section GUI and services the CallBacks. FORMAT  
        specifications for embedded CallBack functions are given in the main  
        body of the code.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_results_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_results_ui", *args, **kwargs)
