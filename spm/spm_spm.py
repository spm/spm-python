from spm.__wrapper__ import Runtime


def spm_spm(*args, **kwargs):
    """
      [Re]ML Estimation of a General Linear Model  
        FORMAT SPM = spm_spm(SPM)  
         
        Required fields of SPM:  
         
        xY.VY - nScan x 1 struct array of image handles (see spm_vol)  
                Images must have the same orientation, voxel size and data type  
              - Any scaling should have already been applied via the image handle  
                scalefactors.  
         
        xX    - Structure containing design matrix information  
              - Required fields are:  
                xX.X      - Design matrix (raw, not temporally smoothed)  
                xX.name   - cellstr of parameter names corresponding to columns  
                            of design matrix  
              - Optional fields are:  
                xX.K      - cell of session-specific structures (see spm_filter)  
                          - Design & data are pre-multiplied by K  
                            (K*Y = K*X*beta + K*e)  
                          - Note that K should not smooth across block boundaries  
                          - defaults to speye(size(xX.X,1))  
                xX.W      - Optional whitening/weighting matrix used to give  
                            weighted least squares estimates (WLS). If not  
                            specified spm_spm will set this to whiten the data  
                            and render the OLS estimates maximum likelihood  
                            i.e. W*W' = inv(xVi.V).  
         
        xVi   - Structure describing intrinsic temporal non-sphericity  
              - Required fields are:  
                xVi.Vi    - array of non-sphericity components  
                          - defaults to {speye(size(xX.X,1))} - i.i.d.  
                          - specifying a cell array of constraints (Qi)  
                            These constraints invoke spm_reml to estimate  
                            hyperparameters assuming V is constant over voxels.  
                            that provide a high precise estimate of xX.V  
              - Optional fields are:  
                xX.V      - Optional non-sphericity matrix.  Cov(e) = sigma^2*V  
                            If not specified spm_spm will compute this using  
                            a 1st pass to identify significant voxels over which  
                            to estimate V.  A 2nd pass is then used to re-estimate  
                            the parameters with WLS and save the ML estimates  
                            (unless xX.W is already specified).  
         
        xM    - Structure containing masking information, or a simple column vector  
                of thresholds corresponding to the images in VY [default: -Inf]  
              - If a structure, the required fields are:  
                xM.TH - nVar x nScan matrix of analysis thresholds, one per image  
                xM.I  - Implicit masking (0=>none, 1 => implicit zero/NaN mask)  
                xM.VM - struct array of explicit mask image handles  
              - (empty if no explicit masks)  
                      - Explicit mask images are >0 for valid voxels to assess.  
                      - Mask images can have any orientation, voxel size or data  
                        type. They are interpolated using nearest neighbour  
                        interpolation to the voxel locations of the data Y.  
              - Note that voxels with constant data (i.e. the same value across  
                scans) are also automatically masked out.  
         
        swd   - Directory where the output files will be saved [default: pwd]  
                If exists, it becomes the current working directory.  
         
        In addition, global SPM "defaults" variable is used (see spm_defaults):  
          
        stats.<modality>.UFp - critical F-threshold for selecting voxels over   
                               which the non-sphericity is estimated (if   
                               required) [default: 0.001]  
          
        stats.maxres         - maximum number of residual images for smoothness  
                               estimation  
         
        stats.maxmem         - maximum amount of data processed at a time (in bytes)  
         
        modality             - SPM modality {'PET','FMRI','EEG'}  
         
       __________________________________________________________________________  
         
        spm_spm is the heart of the SPM package. Given image files and a  
        General Linear Model, it estimates the model parameters, variance  
        hyperparameters, and smoothness of standardised residual fields, writing  
        these out to disk in the current working directory for later  
        interrogation in the results section. (NB: Existing analyses in the  
        current working directory are overwritten).  This directory  
        now becomes the working directory for this analysis and all saved  
        images are relative to this directory.  
         
        The model is expressed via the design matrix (xX.X). The basic model  
        at each voxel is of the form is Y = X*B + e, for data Y, design  
        matrix X, (unknown) parameters B and residual errors e. The errors  
        are assumed to have a normal distribution.  
         
        Sometimes confounds (e.g. drift terms in fMRI) are necessary. These  
        can be specified directly in the design matrix or implicitly, in terms  
        of a residual forming matrix K to give a generalised linear model  
        K*Y = K*X*B + K*e.  In fact K can be any matrix (e.g. a convolution  
        matrix).  
         
        In some instances i.i.d. assumptions about errors do not hold. For  
        example, with serially correlated (fMRI) data or correlations among the  
        levels of a factor in repeated measures designs. This non-sphericity  
        can be specified in terms of components (SPM.xVi.Vi{i}). If specified  
        these covariance components will then be estimated with ReML (restricted  
        maximum likelihood) hyperparameters. This estimation assumes the same  
        non-sphericity for voxels that exceed the global F-threshold. The ReML  
        estimates can then be used to whiten the data giving maximum likelihood  
        (ML) or Gauss-Markov estimators. This entails a second pass of the data  
        with an augmented model K*W*Y = K*W*X*B + K*W*e where W*W' = inv(xVi.V).  
        xVi.V is the non-sphericity based on the hyperparameter estimates.  
        W is stored in xX.W and cov(K*W*e) in xX.V. The covariance of the  
        parameter estimates is then xX.Bcov = pinv(K*W*X)*xX.V*pinv(K*W*X)'.  
         
        If you do not want ML estimates but want to use ordinary least squares  
        (OLS) then simply set SPM.xX.W to the identity matrix. Any non-sphericity  
        V will still be estimated but will be used to adjust the degrees of freedom  
        of the ensuing statistics using the Satterthwaite approximation (c.f.  
        the Greenhouse-Geisser corrections).  
         
        If [non-spherical] variance components Vi are not specified xVi.Vi and  
        xVi.V default to the identity matrix (i.e. i.i.d). The parameters are  
        then estimated by OLS.  In this instance the OLS and ML estimates are  
        the same.  
         
        Note that only a single voxel-specific hyperparameter (i.e. variance  
        component) is estimated, even if V is not i.i.d.  This means spm_spm  
        always implements a fixed-effects model.  
        Random effects models can be emulated using a multi-stage procedure:  
        This entails summarising the data with contrasts such that the fixed  
        effects in a second model on the summary data are those effects of  
        interest (i.e. the population effects). This means contrasts are  
        re-entered into spm_spm to make an inference (SPM) at the next  
        level. At this higher hierarchical level the residual variance for the  
        model contains the appropriate variance components from lower levels.  
         
        Under the additional assumption that the standardised error fields  
        are non-stationary standard Gaussian random fields, results from  
        Random field theory can be applied to estimate the significance  
        statistic images (SPM's) adjusting p values for the multiple tests  
        at all voxels in the search volume. The parameters required for  
        this random field correction are the volume, and Lambda, the covariance  
        matrix of partial derivatives of the standardised error fields, estimated  
        by spm_est_smoothness.  
         
                                   ----------------  
         
        The volume analysed is the intersection of the threshold masks,  
        explicit masks and implicit masks. See spm_spm_ui for further details  
        on masking options.  
       __________________________________________________________________________  
         
        The output of spm_spm takes the form of an SPM.mat file of the analysis  
        parameters, and 'float' flat-file images of the parameter and variance  
        [hyperparameter] estimates. An 8bit zero-one mask image indicating the  
        voxels assessed is also written out, with zero indicating voxels outside  
        the analysed volume.  
         
                                   ----------------  
         
        The following SPM.fields are set by spm_spm (unless specified)  
         
            xVi.V      - estimated non-sphericity trace(V) = rank(V)  
            xVi.h      - hyperparameters  xVi.V = xVi.h(1)*xVi.Vi{1} + ...  
            xVi.Cy     - spatially whitened <Y*Y'> (used by ReML to estimate h)  
         
                                   ----------------  
         
            Vbeta     - struct array of beta image handles (relative)  
            VResMS    - file struct of ResMS image handle  (relative)  
            VM        - file struct of Mask  image handle  (relative)  
         
                                   ----------------  
         
            xX.W      - if not specified W*W' = inv(x.Vi.V)  
            xX.V      - V matrix (K*W*Vi*W'*K') = correlations after K*W is applied  
            xX.xKXs   - space structure for K*W*X, the 'filtered and whitened'  
                        design matrix  
                      - given as spm_sp('Set',xX.K*xX.W*xX.X) - see spm_sp  
            xX.pKX    - pseudoinverse of K*W*X, computed by spm_sp  
            xX.Bcov   - xX.pKX*xX.V*xX.pKX - variance-covariance matrix of  
                        parameter estimates  
                        (when multiplied by the voxel-specific hyperparameter ResMS  
                        of the parameter estimates (ResSS/xX.trRV = ResMS) )  
            xX.trRV   - trace of R*V  
            xX.trRVRV - trace of RVRV  
            xX.erdf   - effective residual degrees of freedom (trRV^2/trRVRV)  
            xX.nKX    - design matrix (xX.xKXs.X) scaled for display  
                        (see spm_DesMtx('sca',... for details)  
         
                                   ----------------  
         
            xVol.M    - 4x4 voxel->mm transformation matrix  
            xVol.iM   - 4x4 mm->voxel transformation matrix  
            xVol.DIM  - image dimensions - column vector (in voxels)  
            xVol.XYZ  - 3 x S vector of in-mask voxel coordinates  
            xVol.S    - Lebesgue measure or volume       (in voxels)  
            xVol.R    - vector of resel counts           (in resels)  
            xVol.FWHM - Smoothness of components - FWHM, (in voxels)  
         
                                   ----------------  
         
            xCon      - Contrast structure (created by spm_FcUtil.m)  
            xCon.name - Name of contrast  
            xCon.STAT - 'F', 'T' or 'P' - for F/T-contrast ('P' for PPMs)  
            xCon.c    - (F) Contrast weights  
            xCon.X0   - Reduced design matrix (spans design space under Ho)  
                        It is in the form of a matrix (spm99b) or the  
                        coordinates of this matrix in the orthogonal basis  
                        of xX.X defined in spm_sp.  
            xCon.iX0  - Indicates how contrast was specified:  
                        If by columns for reduced design matrix then iX0 contains  
                        the column indices. Otherwise, it's a string containing  
                        the spm_FcUtil 'Set' action: Usually one of {'c','c+','X0'}  
                        (Usually this is the input argument F_iX0.)  
            xCon.X1o  - Remaining design space (orthogonal to X0).  
                        It is in the form of the coordinates of this matrix in  
                        the orthogonal basis of xX.X defined in spm_sp.  
            xCon.eidf - Effective interest degrees of freedom (numerator df)  
            xCon.Vcon - ...for handle of contrast/ESS image (empty at this stage)  
            xCon.Vspm - ...for handle of SPM image (empty at this stage)  
       __________________________________________________________________________  
         
        The following images are written to disk:  
         
        mask.<ext>                                          - analysis mask image  
        8-bit (uint8) image of zero-s & one's indicating which voxels were  
        included in the analysis. This mask image is the intersection of the  
        explicit, implicit and threshold masks specified in the xM argument.  
        The XYZ matrix contains the voxel coordinates of all voxels in the  
        analysis mask. The mask image is included for reference, but is not  
        explicitly used by the results section.  
         
                                   ----------------  
         
        beta_????.<ext>                                     - parameter images  
        These are 32-bit (float32) images of the parameter estimates. The image  
        files are numbered according to the corresponding column of the  
        design matrix. Voxels outside the analysis mask (mask.<ext>) are given  
        value NaN.  
         
                                   ----------------  
         
        ResMS.<ext>                           - estimated residual variance image  
        This is a 64-bit (float64) image of the residual variance estimate.  
        Voxels outside the analysis mask are given value NaN.  
         
                                   ----------------  
         
        RPV.<ext>                              - estimated resels per voxel image  
        This is a 64-bit (float64) image of the RESELs per voxel estimate.  
        Voxels outside the analysis mask are given value 0.  These images  
        reflect the nonstationary aspects the spatial autocorrelations.  
         
                                   ----------------  
         
        ResI_????.<ext>                - standardised residual (temporary) images  
        These are 64-bit (float64) images of standardised residuals. At most  
        maxres images will be saved and used by spm_est_smoothness, after which  
        they will be deleted.  
       __________________________________________________________________________  
         
        References:  
         
        Statistical Parametric Maps in Functional Imaging: A General Linear  
        Approach. Friston KJ, Holmes AP, Worsley KJ, Poline JB, Frith CD,  
        Frackowiak RSJ. (1995) Human Brain Mapping 2:189-210.  
         
        Analysis of fMRI Time-Series Revisited - Again. Worsley KJ, Friston KJ.  
        (1995) NeuroImage 2:173-181.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_spm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_spm", *args, **kwargs)
