from spm.__wrapper__ import Runtime


def spm_getSPM(*args, **kwargs):
    """
      Compute a specified and thresholded SPM/PPM following estimation  
        FORMAT [SPM,xSPM] = spm_getSPM;  
        Query SPM in interactive mode.  
         
        FORMAT [SPM,xSPM] = spm_getSPM(xSPM);  
        Query SPM in batch mode. See below for a description of fields that may  
        be present in xSPM input. Values for missing fields will be queried  
        interactively.  
         
        xSPM      - structure containing SPM, distribution & filtering details  
        .swd      - SPM working directory - directory containing current SPM.mat  
        .title    - title for comparison (string)  
        .Z        - minimum of Statistics {filtered on u and k}  
        .n        - conjunction number <= number of contrasts  
        .STAT     - distribution {Z, T, X, F or P}  
        .df       - degrees of freedom [df{interest}, df{residual}]  
        .STATstr  - description string  
        .Ic       - indices of contrasts (in SPM.xCon)  
        .Im       - indices of masking contrasts (in xCon)  
        .pm       - p-value for masking (uncorrected)  
        .Ex       - flag for exclusive or inclusive masking  
        .u        - height threshold  
        .k        - extent threshold {voxels}  
        .XYZ      - location of voxels {voxel coords}  
        .XYZmm    - location of voxels {mm}  
        .S        - search Volume {voxels}  
        .R        - search Volume {resels}  
        .FWHM     - smoothness {voxels}  
        .M        - voxels -> mm matrix  
        .iM       - mm -> voxels matrix  
        .VOX      - voxel dimensions {mm} - column vector  
        .DIM      - image dimensions {voxels} - column vector  
        .Vspm     - Mapped statistic image(s)  
        .Ps       - uncorrected P values in searched volume (for voxel FDR)  
        .Pp       - uncorrected P values of peaks (for peak FDR)  
        .Pc       - uncorrected P values of cluster extents (for cluster FDR)  
        .uc       - 0.05 critical thresholds for FWEp, FDRp, FWEc, FDRc  
        .thresDesc - description of height threshold (string)  
         
        Required fields of SPM  
         
        xVol   - structure containing details of volume analysed  
         
        xX     - Design Matrix structure  
               - (see spm_spm.m for structure)  
         
        xCon   - Contrast definitions structure array  
               - (see also spm_FcUtil.m for structure, rules & handling)  
        .name  - Contrast name  
        .STAT  - Statistic indicator character ('T', 'F' or 'P')  
        .c     - Contrast weights (column vector contrasts)  
        .X0    - Reduced design matrix data (spans design space under Ho)  
                 Stored as coordinates in the orthogonal basis of xX.X from spm_sp  
                 Extract using X0 = spm_FcUtil('X0',...  
        .iX0   - Indicates how contrast was specified:  
                 If by columns for reduced design matrix then iX0 contains the  
                 column indices. Otherwise, it's a string containing the  
                 spm_FcUtil 'Set' action: Usually one of {'c','c+','X0'}  
        .X1o   - Remaining design space data (X1o is orthogonal to X0)  
                 Stored as coordinates in the orthogonal basis of xX.X from spm_sp  
                 Extract using X1o = spm_FcUtil('X1o',...  
        .eidf  - Effective interest degrees of freedom (numerator df)  
               - Or effect-size threshold for Posterior probability  
        .Vcon  - Name of contrast (for 'T's) or ESS (for 'F's) image  
        .Vspm  - Name of SPM image  
         
        Evaluated fields in xSPM (input)  
         
        xSPM      - structure containing SPM, distribution & filtering details  
        .swd      - SPM working directory - directory containing current SPM.mat  
        .title    - title for comparison (string)  
        .Ic       - indices of contrasts (in SPM.xCon)  
        .n        - conjunction number <= number of contrasts  
        .Im       - indices of masking contrasts (in xCon)  
        .pm       - p-value for masking (uncorrected)  
        .Ex       - flag for exclusive or inclusive masking  
        .u        - height threshold  
        .k        - extent threshold {voxels}  
        .thresDesc - description of height threshold (string)  
         
        In addition, the xCon structure is updated. For newly evaluated  
        contrasts, SPM images (spmT_????.{img,hdr}) are written, along with  
        contrast (con_????.{img,hdr}) images for SPM{T}'s, or Extra  
        Sum-of-Squares images (ess_????.{img,hdr}) for SPM{F}'s.  
         
        The contrast images are the weighted sum of the parameter images,  
        where the weights are the contrast weights, and are uniquely  
        estimable since contrasts are checked for estimability by the  
        contrast manager. These contrast images (for appropriate contrasts)  
        are suitable summary images of an effect at this level, and can be  
        used as input at a higher level when effecting a random effects  
        analysis. (Note that the ess_????.{img,hdr} and  
        SPM{T,F}_????.{img,hdr} images are not suitable input for a higher  
        level analysis.)  
         
       __________________________________________________________________________  
         
        spm_getSPM prompts for an SPM and applies thresholds {u & k}  
        to a point list of voxel values (specified with their locations {XYZ})  
        This allows the SPM be displayed and characterized in terms of regionally  
        significant effects by subsequent routines.  
         
        For general linear model Y = XB + E with data Y, design matrix X,  
        parameter vector B, and (independent) errors E, a contrast c'B of the  
        parameters (with contrast weights c) is estimated by c'b, where b are  
        the parameter estimates given by b=pinv(X)*Y.  
         
        Either single contrasts can be examined or conjunctions of different  
        contrasts. Contrasts are estimable linear combinations of the  
        parameters, and are specified using the SPM contrast manager  
        interface [spm_conman.m]. SPMs are generated for the null hypotheses  
        that the contrast is zero (or zero vector in the case of  
        F-contrasts). See the help for the contrast manager [spm_conman.m]  
        for a further details on contrasts and contrast specification.  
         
        A conjunction assesses the conjoint expression of multiple effects. The  
        conjunction SPM is the minimum of the component SPMs defined by the  
        multiple contrasts.  Inference on the minimum statistics can be  
        performed in different ways.  Inference on the Conjunction Null (one or  
        more of the effects null) is accomplished by assessing the minimum as  
        if it were a single statistic; one rejects the conjunction null in  
        favor of the alternative that k=nc, that the number of active effects k  
        is equal to the number of contrasts nc.  No assumptions are needed on  
        the dependence between the tests.  
         
        Another approach is to make inference on the Global Null (all effects  
        null).  Rejecting the Global Null of no (u=0) effects real implies an  
        alternative that k>0, that one or more effects are real.   A third  
        Intermediate approach, is to use a null hypothesis of no more than u  
        effects are real.  Rejecting the intermediate null that k<=u implies an  
        alternative that k>u, that more than u of the effects are real.  
         
        The Global and Intermediate nulls use results for minimum fields which  
        require the SPMs to be identically distributed and independent. Thus,  
        all component SPMs must be either SPM{t}'s, or SPM{F}'s with the same  
        degrees of freedom. Independence is roughly guaranteed for large  
        degrees of freedom (and independent data) by ensuring that the  
        contrasts are "orthogonal". Note that it is *not* the contrast weight  
        vectors per se that are required to be orthogonal, but the subspaces of  
        the data space implied by the null hypotheses defined by the contrasts  
        (c'pinv(X)). Furthermore, this assumes that the errors are  
        i.i.d. (i.e. the estimates are maximum likelihood or Gauss-Markov. This  
        is the default in spm_spm).  
         
        To ensure approximate independence of the component SPMs in the case of  
        the global or intermediate null, non-orthogonal contrasts are serially  
        orthogonalised in the order specified, possibly generating new  
        contrasts, such that the second is orthogonal to the first, the third  
        to the first two, and so on.  Note that significant inference on the  
        global null only allows one to conclude that one or more of the effects  
        are real.  Significant inference on the conjunction null allows one to  
        conclude that all of the effects are real.  
         
        Masking simply eliminates voxels from the current contrast if they  
        do not survive an uncorrected p value (based on height) in one or  
        more further contrasts.  No account is taken of this masking in the  
        statistical inference pertaining to the masked contrast.  
         
        The SPM is subject to thresholding on the basis of height (u) and the  
        number of voxels comprising its clusters {k}. The height threshold is  
        specified as above in terms of an [un]corrected p value or  
        statistic.  Clusters can also be thresholded on the basis of their  
        spatial extent. If you want to see all voxels simply enter 0.  In this  
        instance the 'set-level' inference can be considered an 'omnibus test'  
        based on the number of clusters that obtain.  
         
        BAYESIAN INFERENCE AND PPMS - POSTERIOR PROBABILITY MAPS  
         
        If conditional estimates are available (and your contrast is a T  
        contrast) then you are asked whether the inference should be 'Bayesian'  
        or 'classical' (using GRF).  If you choose Bayesian the contrasts are of  
        conditional (i.e. MAP) estimators and the inference image is a  
        posterior probability map (PPM).  PPMs encode the probability that the  
        contrast exceeds a specified threshold.  This threshold is stored in  
        the xCon.eidf.  Subsequent plotting and tables will use the conditional  
        estimates and associated posterior or conditional probabilities.  
         
        see spm_results_ui.m for further details of the SPM results section.  
        see also spm_contrasts.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_getSPM.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_getSPM", *args, **kwargs)
