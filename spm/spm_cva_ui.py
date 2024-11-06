from spm.__wrapper__ import Runtime


def spm_cva_ui(*args, **kwargs):
    """
      VOI extraction of adjusted data and CVA  
        FORMAT [CVA] = spm_cva_ui('specify',xSPM,SPM,CVA)  
         
        xSPM   - structure containing specific SPM details  
            xSPM.Ic  - indice of contrast (in SPM.xCon)  
        SPM    - structure containing generic analysis details  
         
        CVA.contrast -  contrast name  
        CVA.name     -  CVA name  
        CVA.c        -  contrast weights  
        CVA.X        -  contrast subspace  
        CVA.Y        -  whitened and adjusted data  
        CVA.X0       -  null space of contrast  
         
        CVA.XYZ      -  locations of voxels (mm)  
        CVA.xyz      -  seed voxel location (mm)  
        CVA.VOX      -  dimension of voxels (mm)  
         
        CVA.V        -  canonical vectors  (data)  
        CVA.v        -  canonical variates (data)  
        CVA.W        -  canonical vectors  (design)  
        CVA.w        -  canonical variates (design)  
        CVA.C        -  canonical contrast (design)  
         
        CVA.chi      -  Chi-squared statistics testing D >= i  
        CVA.df       -  d.f.  
        CVA.p        -  p-values  
         
        also saved in CVA_*.mat in the SPM working directory  
         
        FORMAT [CVA] = spm_cva_ui('results',CVA)  
        Display the results of a CVA analysis  
       __________________________________________________________________________  
         
        This routine allows one to make inferences about effects that are  
        distributed in a multivariate fashion or pattern over voxels. It uses  
        conventional canonical variates (CVA) analysis (also know as canonical  
        correlation analysis, ManCova and linear discriminant analysis).  CVA is  
        a complement to MVB, in that the predictor variables remain the design  
        matrix and the response variable is the imaging data in the usual way.  
        However, the multivariate aspect of this model allows one to test for  
        designed effects that are distributed over voxels and thereby increase  
        the sensitivity of the analysis.  
         
        Because there is only one test, there is no multiple comparison problem.  
        The results are shown in term of the maximum intensity projection of the  
        (positive) canonical image or vector and the canonical variates based on  
        (maximally) correlated mixtures of the explanatory variables and data.  
         
        CVA uses the generalised eigenvalue solution to the treatment and  
        residual sum of squares and products of a general linear model. The  
        eigenvalues (i.e., canonical values), after transformation, have a  
        chi-squared distribution and allow one to test the null hypothesis that  
        the mapping is D or more dimensional. This inference is shown as a bar  
        plot of p-values.  The first p-value is formally identical to that  
        obtained using Wilks' Lambda and tests for the significance of any  
        mapping.  
         
        This routine uses the current contrast to define the subspace of interest  
        and treats the remaining design as uninteresting. Conventional results  
        for the canonical values are used after the data (and design matrix) have  
        been whitened; using the appropriate ReML estimate of non-sphericity.  
         
        CVA can be used for decoding because the model employed by CVA does not  
        care about the direction of the mapping (hence canonical correlation  
        analysis). However, one cannot test for mappings between nonlinear  
        mixtures of regional activity and some experimental variable (this is  
        what the MVB was introduced for).  
         
        References:  
         
        Characterizing dynamic brain responses with fMRI: a multivariate  
        approach. Friston KJ, Frith CD, Frackowiak RS, Turner R. NeuroImage. 1995  
        Jun;2(2):166-72.  
         
        A multivariate analysis of evoked responses in EEG and MEG data. Friston  
        KJ, Stephan KM, Heather JD, Frith CD, Ioannides AA, Liu LC, Rugg MD,  
        Vieth J, Keber H, Hunter K, Frackowiak RS. NeuroImage. 1996 Jun;  
        3(3):167-174.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_cva_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cva_ui", *args, **kwargs)
