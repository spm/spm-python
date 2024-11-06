from spm.__wrapper__ import Runtime


def spm_graph_ui(*args, **kwargs):
    """
      Graphical display of adjusted data  
        FORMAT [Y,y,beta,Bcov] = spm_graph_ui(xSPM,SPM,hReg)  
         
        xSPM   - structure containing SPM, distributional & filtering details  
                 about the excursion set  
        SPM    - structure containing generic details about the analysis  
        hReg   - handle of MIP register or [x y z] coordinates  
         
        Y      - fitted   data for the selected voxel  
        y      - adjusted data for the selected voxel  
        beta   - parameter estimates (ML or MAP)  
        Bcov   - Covariance of parameter estimates (ML or conditional)  
         
        See spm_getSPM for details.  
       __________________________________________________________________________  
         
        spm_graph is a Callback function that uses the structures above to:  
        (1) send adjusted (y) and fitted data (Y), for the selected voxel, to the  
        workspace and (ii) provide graphics for:  
         
        a) Contrasts of parameter estimates (e.g. activations) and their  
        standard error.  
         
        b) Fitted and adjusted responses that can be plotted against time, scan,  
        or an indicator variable in the design matrix.  
         
        c) (fMRI only).  Evoked responses using the basis functions to give  
        impulse responses that would have been seen in the absence of other  
        effects. The PSTH (peristimulus-time histogram) option provides a finite  
        impulse response (FIR) estimate of the trial-specific evoked response as  
        a function of peristimulus time.  This is estimated by refitting a  
        convolution model to the selected voxel using an FIR basis set.  This is  
        simply a set of small boxes covering successive time bins after trial  
        onset.  The width of each bin is usually the TR.  This option provides a  
        more time-resolved quantitative characterisation of the evoked  
        hemodynamic response.  However, it should not be over-interpreted because  
        inference is usually made using a simpler and more efficient basis set  
        (e.g., canonical hrf, or canonical plus time derivative).  
         
        Getting adjusted data:  
        Ensuring the data are adjusted properly can be important (e.g. in  
        constructing explanatory variables such as in a psychophysiological  
        interaction). To remove or correct for specific effects, specify an  
        appropriate F contrast and simply plot the fitted (and adjusted)  
        responses after selecting that F contrast. The vectors Y (fitted) and y  
        (adjusted) in the workspace will now be corrected for the effects in the  
        reduced design matrix (X0) specified in the contrast manager with the  
        column indices (iX0) of the confounds in this adjustment.  
         
        Plotting data:  
        All data and graphics use filtered/whitened data and residuals. In PET  
        studies the parameter estimates and the fitted data are often the same  
        because the explanatory variables are simply indicator variables taking  
        the value of one.  Only contrasts previously defined can be plotted. This  
        ensures that the parameters plotted are meaningful even when there is  
        collinearity among the design matrix subpartitions.  
         
        Selecting contrasts used for PPMs will automatically give plots  
        based on conditional estimates.  
         
        The structure     contrast.contrast      = cbeta;  
                          contrast.standarderror = SE;  
                          contrast.interval      = 2*CI;  
         
        is assigned in base workspace for plots of contrasts and their error.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_graph_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_graph_ui", *args, **kwargs)
