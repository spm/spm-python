from spm.__wrapper__ import Runtime


def spm_adjmean_fmri_ui(*args, **kwargs):
    """
      Adjusted means of fMRI via box-car General Linear Model with confounds  
        FORMAT spm_adjmean_fmri_ui  
       _______________________________________________________________________  
         
        spm_adjmean_fmri_ui uses the General Linear Model to produce adjusted  
        condition images, adjusted for global effects and confounds.  
         
        This program is designed for collapsing data from a single session  
        fMRI epoch-related design into a set of representative condition  
        images, one for each condition, adjusted for global effects and with  
        low frequency drifts removed via a discrete cosine basis set high  
        pass filter. The resulting data sets are suitable for a (2nd level)  
        random effects analysis of multiple sessions or subjects, or group  
        comparisons.  
         
        See spm_RandFX.man for further details on implementing random effects  
        analyses in SPM96 using a multi-level approach.  
         
         
        Overview  
        ----------------------------------------------------------------------  
        The program works with a single fMRI session, fitting a General  
        Linear Model consisting of simple box-cars (optionally convolved with  
        an estimated haemodynamic response function) and an (optional) high  
        pass filter of discrete cosine basis functions. The effects of  
        interest (the box-cars) are orthogonalised (residualised) with  
        respect to the confounds (the high pass filter) to ensure that *all*  
        confounds are removed from the data, even if they're correlated with  
        the effects of interest. (For well designed experiments this makes  
        little difference.) Proportional scaling and AnCova global  
        normalisation are supported, the latter including the option to scale  
        all the images such that their the grand mean (GM) is a specified  
        value.  
         
        The interface is similar to a cut-down SPM-fMRI, and the adjusted  
        means are the parameter estimates from the model. The user is first  
        prompted to select the scans for a single fMRI session. Then the  
        epoch condition order is specified. This should be a r-vector, where  
        r is the number of epochs, of integers 1:n or 0:n-1 where n is the  
        number of conditions (0 can be used to indicate the baseline or  
        "rest" condition. Then the number of scans per epoch is specified:  
        This can be a single integer (all epochs have the same number of  
        scans), or an r-vector of integers specifying number of scans for the  
        corresponding epoch.  
         
        Once the experimental design has been specified, the user is given  
        various options: The box-cars can be convolved with an approximate  
        haemodynamic response function; High-pass filter components can be  
        added to the confounds (at a user-specified cut-off which defaults to  
        twice the maximum period of the experiment); Global normalisation can  
        be omitted, or implemented by proportional scaling or AnCova; and the  
        grand mean scaling options specified.  
         
        With the design and adjustments specified, the model is constructed,  
        and the user prompted to enter/confirm filenames for the adjusted  
        condition images.  
         
        The model, filenames, global values and options are saved to a MatLab  
        *.mat file named SPMadj.mat in the current working directory.  
         
        Implicit masking is carried out: Zero voxels are implicitly assumed  
        to be masked out. Thus, the adjusted mean is calculated at voxels  
        which are non-zero in *all* the input images pertaining to the  
        adjusted mean (usually those from the appropriate subject). (This is  
        *not* a softmean.) Data realigned in a single session with SPM'96 (or  
        later) are automatically implicitly zero masked with a consistent  
        mask in this way.  
         
        GM, the value for grand mean scaling, is user specified.  
        The default value is 100.  
         
        If computing adjusted means for subsequent (2nd level) modelling, as  
        with a random effects analysis, then it is important to use a  
        separable model, such that the adjustment for one subject is  
        independent of other subjects entered into the model. Thus,  
        proportional scaling or subject-specific AnCova adjustment must be  
        used. Further, multiple runs *must* use the same GM value, and should  
        scale Grand mean *by subject*.  
         
        ( A separate program (spm_adjmean_ui) is available for computing       )  
        ( adjusted condition means of PET data. The functionality is similar   )  
        ( to this code, but the two routines have been separated for           )  
        ( algorithmic clarity.                                                 )  
         
        Diagnostic output  
        ----------------------------------------------------------------------  
        Diagnostic output consists of two sections:  
         
        The first page lists the filenames, various parameters (Grand mean  
        scaling etc.), and gives a plot of the image global means against  
        scan number, overlaid on an "image" of the condition effects. Watch  
        out for condition dependent global changes!  
         
        The second part is a single page depicting the design matrix, effect  
        names, parameter contrasts used, and the corresponding image files  
        written.  
         
        As always, look at the resulting mean images to make sure they look OK!  
         
         
        Algorithm  
        ----------------------------------------------------------------------  
        The model at each voxel is Y = X*B + e, with a set of least squares  
        estimates for the vector of parameters B as b = pinv(X)*Y. For c a  
        vector of contrast weights extracting the appropriate parameter, the  
        contrast of the parameter estimates is c'*b = c'*pinv(X)*Y, a  
        weighted sum (or weighted mean) of the data at that voxel. These  
        weights are identical for all voxels, so the image of the parameter  
        estimate can be computed as a weighted mean of the images.  
         
        The design matrix is split into effects of interest [C], a constant  
        term [B], and confounds [G]. The columns of G are centered so that  
        the confound cannot model any of the mean. The effects of interest  
        are orthogonalised wirit. the confounds, using C=C-G*pinv(G)*C; This  
        ensures that *all* confound effects are removed from the data, even  
        if they are correlated with the effects of interest.  
         
        Once the weights have been worked out for each adjusted mean image,  
        computation proceeds by passing appropriate weights and image  
        filenames to spm_mean, which writes out the appropriate parameter  
        image as an Analyze format image of the same type (see spm_type) as  
        the input images.  
         
         
        Variables saved in SPMadj.mat data file  
        ----------------------------------------------------------------------  
        Des           Structure containing design parameters & specification  
          .DesName    Design name  
          .HForm      Form of DesMtx H partition  
          .iSubj      Subject indicator vector  
          .iCond      Condition indicator vector  
          .iRepl      Replication indicator vector  
          .iGloNorm   Global normalisation option  
          .sGloNorm   Global normalisation description  
          .iGMsca     Grand mean scaling option  
          .sGMsca     Grand mean scaling description  
          .GM         Grand Mean used for scaling  
          .iAdjTo     Adjustment (for AnCova) option  
          .sAdjTo     Adjustment (for AnCova) description  
          .aGM        AnCova adjustment value (subtracted from GX before AnCova)  
          .gSF        Image scale factors for global scaling  
          .X          Design matrix  
          .nX         Normalised (for imaging) design matrix  
          .Xnames     Effects corresponding to cols of X (cellstr)  
          .aPMap      Additional parameter to effect name mappings (see spm_desMtx)  
          .EXnames    English effect names corresponding to TeX parameters of Xnames   
          .iX         Structure defining design matrix subpartitions  
              .H      Columns of X corresponding to H partition  
              .C      Columns of X corresponding to C partition  
              .B      Columns of X corresponding to B partition  
              .G      Columns of X corresponding to G partition  
        c             Matrix of contrasts, contrasts in rows  
        cNames        Names associated with contrasts  
        W             Weights for images corresponding to contrasts  
        Fnames        Filenames of adjusted mean images written (cellstr)  
        rGX           raw global means (before any scaling)  
        GX            Global means after scaling  
         
        P     String matrix of filenames  
        iCond     Condition indicator vector  
        iGloNorm  Global normalisation option  
        sGloNorm  Global normalisation description  
        iGMsca    Grand mean scaling option  
        sGMsca    Grand mean scaling description  
        HPFc      High pass filter cut-off period (s)  
        HPF       High pass filter  
        sHPF      Description of high-pass filter  
        rC        raw C partition of design matrix, prior to orthogonalisation  
        C     C (covariates of interest) partition of design matrix  
        Cnames    Names of parameters corresponding to columns of C  
        B     B (block) partition of the design matrix  
        Bnames    Names of parameters corresponding to columns of B  
        G     G (confounding covariates) partition of design matrix  
        Gnames    Names of parameters corresponding to columns of G  
        rX        raw design matrix, prior to orthogonalisation of C partition  
        X     design matrix (=[C,B,G])  
        nrX       raw design matrix, normalised for display  
        nX        design matrix, normalised for display  
        c     Matrix of contrasts, contrasts in rows  
        cNames    Names associated with contrasts  
        W     Weights for images corresponding to contrasts  
        CWD       Current Working Directory (when run)  
        Fnames    Filenames of adjusted mean images written  
        rGX       raw global means (before any scaling)  
        gSF       Image scale factors for global scaling (inc. grand mean scaling)  
        GX        Global means after scaling  
        GM        Grans Mean used for scaling  
         
         
       _______________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/compat/spm_adjmean_fmri_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_adjmean_fmri_ui", *args, **kwargs, nargout=0)
