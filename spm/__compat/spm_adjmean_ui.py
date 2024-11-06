from spm.__wrapper__ import Runtime


def spm_adjmean_ui(*args, **kwargs):
    """
      Scaled (for grand mean) & adjusted (for global) means via General Linear Model  
        FORMAT spm_adjmean_ui  
       _______________________________________________________________________  
         
        spm_adjmean_ui uses the General Linear Model to produce mean images  
        adjusted for global effects.  
         
        This program is designed for collapsing data within condition to give  
        a single adjusted mean scan per condition per subject, suitable for a  
        (2nd level) random effects analysis.  
         
        See spm_RandFX.man for further details on implementing random effects  
        analyses in SPM96 using a multi-level approach.  
         
        Overview  
        ----------------------------------------------------------------------  
        The program supports multiple conditions, multiple subjects, Grand  
        Mean (GM) scaling by subject or overall grand mean, proportional  
        scaling global normalisation; and AnCova (regression) global  
        normalisation, both overall and subject specific, with adjustment to  
        subject or overall grand means (after scaling). The availability of  
        these options is customised for various designs.  
         
        Adjustment is performed via the General Linear Model. The interface  
        is similar to SPM-PET, and the adjusted means are the parameter  
        estimates from the model. Having chosen a design, the user is  
        prompted for scans (by subject and/or condition where appropriate),  
        and then asked to set scaling/normalisation/adjustment options as  
        appropriate. With the design specified, the model is constructed, and  
        the user prompted to enter/confirm filenames for the adjusted mean  
        images, which are written to the current working directory (pwd).  
         
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
        The default value is 50.  
         
        If computing adjusted means for subsequent (2nd level) modelling, as  
        with a random effects analysis, then it is important to use a  
        separable model, such that the adjustment for one subject is  
        independent of other subjects entered into the model. Thus,  
        proportional scaling or subject-specific AnCova adjustment must be  
        used. Further, multiple runs *must* use the same GM value, and should  
        scale Grand mean *by subject*.  
         
        ( A separate program (spm_adjmean_fmri_ui) is available for computing  )  
        ( adjusted condition means of fMRI data, adjusting for global effects  )  
        ( and removing low frequency drifts with a high-pass filer (discrete   )  
        ( cosine basis set). The functionality is similar to this code, but    )  
        ( the two routines have been separated for algorithmic clarity.        )  
         
        Diagnostic output  
        ----------------------------------------------------------------------  
        Diagnostic output consists of two sections:  
         
        The first is a list of the image filenames; their global values; and  
        the respective subject (block), condition and replication indices; in  
        the order in which the the data are entered into the model. This is  
        followed by a brief description of appropriate parameters (Grand mean  
        scaling etc.)  
         
        The second part is a single page depicting the design matrix, effect  
        names, parameter contrasts used, and the corresponding image files  
        written.  
         
        As always, look at the resulting mean images to make sure they look OK!  
         
         
        AdjMean "recipes"...  
        ----------------------------------------------------------------------  
        Rather than offer a bewildering array of options, various  
        pre-configured recipes are offered for common scenarios:  
         
        * Basic means: +/- grand mean scaling; +/- global normalisation  
         
         1) Straight mean  
              - as the neame suggests! Prompts for files and writes their mean.  
         2) PropSca & Average  
              - Average of images adjusted for global differences by proportional  
                scaling: Scales all images to have global mean of GM, and then  
                writes their mean.  
         3) Linear (AnCova) adjusted mean (scaled mean)  
              - Data scaled so that grand mean is GM. Single mean of images  
                adjusted for global effects by linear regression to mean global.  
                (Actually, this turns out to be a straight mean of the grand mean  
                scaled data, hence the description "scaled mean".)  
         4) Multi linear adjusted means (scaled means)  
              - Multiple block means. Data scaled within blocks to (block) Grand  
                Means of GM. Linear global adjustment within block to block grand  
                mean, and computation of adjusted block means. It's like running  
                option (3) multiple times. Since this is equivalent to grand mean  
                scaling within block and then writing out the block means, it's  
                also tagged "scaled means".  
         
        * The "condition" recipes: Adjusted condition means, computed within subj.  
         
         5) SingleSubj: Condition means (PropSca)  
              - Proportional scaling global normalisation of image global means  
                to GM. Computation of means of adjusted data within condition.  
         6) SingleSubj: Condition means (AnCova)  
              - Grand mean scaling of mean global to GM. AnCova global  
                normalisation (parallel lines for each condition).  
                Condition means of AnCova adjusted data written. These are the  
                condition effects of the standard SPM single subject activation  
                AnCova.  
         7) MultiSubj: Condition means (PropSca)  
              - Multiple subject version of option (5).  
                It's like running option (5) repeatedly.  
         8) MultiSubj: Condition means (AnCova by subject)  
              - Multiple subject version of option (6):  
                Grand mean scaling by subject, AnCova by subject.  
                It's like running option (6) repeatedly.  
         
         
        Algorithm  
        ----------------------------------------------------------------------  
        The model at each voxel is Y = X*B + e, with least squares estimates  
        (for full rank X) for the vector B of parameters as b =  
        inv(X'*X)*X'*Y. For c a vector of contrast weights extracting the  
        appropriate parameter, the contrast of the parameter estimates is  
        c'*b = c'* inv(X'*X)*X' * Y, a weighted sum (or weighted mean) of the  
        data at that voxel. These weights are identical for all voxels, so  
        the image of the parameter estimate can be computed as a weighted  
        mean of the images.  
         
        Once the weights have been worked out for each adjusted mean image,  
        computation proceeds by passing appropriate weights and image  
        filenames to spm_add, which writes out the appropriate parameter  
        image as an Analyze format image of the same type (see spm_type) as  
        the input images.  
         
        Variables saved in SPMadj.mat data file  
        ----------------------------------------------------------------------  
        DesDef        Structure containing defaults for chosen design  
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
         
       _______________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/compat/spm_adjmean_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_adjmean_ui", *args, **kwargs, nargout=0)
