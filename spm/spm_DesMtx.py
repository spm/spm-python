from spm.__wrapper__ import Runtime


def spm_DesMtx(*args, **kwargs):
    """
      Design matrix construction from factor level and covariate vectors  
        FORMAT [X,Pnames] = spm_DesMtx(<FCLevels-Constraint-FCnames> list)  
        FORMAT [X,Pnames,Index,idx,jdx,kdx] = spm_DesMtx(FCLevels,Constraint,FCnames)  
         
        <FCLevels-Constraints-FCnames>  
               - set of arguments specifying a portion of design matrix (see below)  
               - FCnames parameter, or Constraint and FCnames parameters, are optional  
               - a list of multiple <FCLevels-Constraint-FCnames> triples can be  
             specified, where FCnames or Constraint-FCnames may be omitted  
             within any triple. The program then works recursively.  
         
        X      - design matrix  
        Pnames - parameter names as (constructed from FCnames) - a cellstr  
        Index  - integer index of factor levels  
               - only returned when computing a single design matrix partition  
         
        idx,jdx,kdx - reference vectors mapping I & Index (described below)  
                    - only returned when computing a single design matrix partition  
                      for unconstrained factor effects ('-' or '~')  
         
                                  ----------------  
         
        FORMAT [nX,nPnames] = spm_DesMtx('sca',X1,Pnames1,X2,Pnames2,...)  
        Produces a scaled design matrix nX with max(abs(nX(:))<=1, suitable  
        for imaging with: image((nX+1)*32)  
        X1,X2,...             - Design matrix partitions  
        Pnames1, Pnames2,...  - Corresponding parameter name string mtx/cellstr (opt)  
        nX                    - Scaled design matrix  
        nPnames               - Concatenated parameter names for columns of nX  
         
       __________________________________________________________________________  
         
        Returns design matrix corresponding to given vectors containing  
        levels of a factor; two way interactions; covariates (n vectors);  
        ready-made sections of design matrix; and factor by covariate  
        interactions.  
         
        The specification for the design matrix is passed in sets of arguments,  
        each set corresponding to a particular Factor/Covariate/&c., specifying  
        a section of the design matrix. The set of arguments consists of the   
        FCLevels matrix (Factor/Covariate levels), an optional constraint string,  
        and an optional (string) name matrix containing the names of the   
        Factor/Covariate/&c.  
         
        MAIN EFFECTS: For a main effect, or single factor, the FCLevels  
        matrix is an integer vector whose values represent the levels of the  
        factor. The integer factor levels need not be positive, nor in  
        order.  In the '~' constraint types (below), a factor level of zero  
        is ignored (treated as no effect), and no corresponding column of  
        design matrix is created.  Effects for the factor levels are entered  
        into the design matrix *in increasing order* of the factor levels.  
        Check Pnames to find out which columns correspond to which levels of  
        the factor.  
         
        TWO WAY INTERACTIONS: For a two way interaction effect between two  
        factors, the FCLevels matrix is an nx2 integer matrix whose columns  
        indicate the levels of the two factors. An effect is included for  
        each unique combination of the levels of the two factors. Again,  
        factor levels must be integer, though not necessarily positive.  
        Zero levels are ignored in the '~' constraint types described below.  
         
        CONSTRAINTS: Each FactorLevels vector/matrix may be followed by an   
        (optional) ConstraintString.  
         
        ConstraintStrings for main effects are:  
                         '-'   - No Constraint  
                         '~'   - Ignore zero level of factor  
                                 (I.e. cornerPoint constraint on zero level,  
                                 (same as '.0', except zero level is always ignored,  
                                 (even if factor only has zero level, in which case  
                                 (an empty DesMtx results and a warning is given  
                         '+0'  - sum-to-zero constraint  
                         '+0m' - Implicit sum-to-zero constraint  
                         '.'   - CornerPoint constraint  
                         '.0'  - CornerPoint constraint applied to zero factor level  
                                 (warns if there is no zero factor level)  
         Constraints for two way interaction effects are  
           '-'                 - No Constraints  
                         '~'   - Ignore zero level of any factor  
                                 (I.e. cornerPoint constraint on zero level,  
                                 (same as '.ij0', except zero levels are always ignored  
           '+i0','+j0','+ij0'  - sum-to-zero constraints  
           '.i', '.j', '.ij'   - CornerPoint constraints  
           '.i0','.j0','.ij0'  - CornerPoint constraints applied to zero factor level  
                                 (warns if there is no zero factor level)  
           '+i0m', '+j0m'      - Implicit sum-to-zero constraints  
         
        With the exception of the "ignore zero" '~' constraint, constraints  
        are only applied if there are sufficient factor levels. CornerPoint  
        and explicit sum-to-zero Constraints are applied to the last level of  
        the factor.  
         
        The implicit sum-to-zero constraints "mean correct" appropriate rows  
        of the relevant design matrix block. For a main effect, constraint  
        '+0m' "mean corrects" the main effect block across columns,  
        corresponding to factor effects B_i, where B_i = B'_i - mean(B'_i) :  
        The B'_i are the fitted parameters, effectively *relative* factor  
        parameters, relative to their mean. This leads to a rank deficient  
        design matrix block. If Matlab's pinv, which implements a  
        Moore-Penrose pseudoinverse, is used to solve the least squares  
        problem, then the solution with smallest L2 norm is found, which has  
        mean(B'_i)=0 provided the remainder of the design is unique (design  
        matrix blocks of full rank). In this case therefore the B_i are  
        identically the B'_i - the mean correction imposes the constraint.  
               
         
        COVARIATES: The FCLevels matrix here is an nxc matrix whose columns  
        contain the covariate values. An effect is included for each covariate.  
        Covariates are identified by ConstraintString 'C'.  
         
         
        PRE-SPECIFIED DESIGN BLOCKS: ConstraintString 'X' identifies a  
        ready-made bit of design matrix - the effect is the same as 'C'.  
         
         
        FACTOR BY COVARIATE INTERACTIONS: are identified by ConstraintString  
        'FxC'. The last column is understood to contain the covariate. Other  
        columns are taken to contain integer FactorLevels vectors. The  
        (unconstrained) interaction of the factors is interacted with the  
        covariate. Zero factor levels are ignored if ConstraintString '~FxC'  
        is used.  
         
         
        NAMES: Each Factor/Covariate can be 'named', by passing a name  
        string.  Pass a string matrix, or cell array (vector) of strings,  
        with rows (cells) naming the factors/covariates in the respective  
        columns of the FCLevels matrix.  These names default to <Fac>, <Cov>,  
        <Fac1>, <Fac2> &c., and are used in the construction of the Pnames  
        parameter names.  
        E.g. for an interaction, spm_DesMtx([F1,F2],'+ij0',['subj';'cond'])  
        giving parameter names such as subj*cond_{1,2} etc...  
         
        Pnames returns a string matrix whose successive rows describe the  
        effects parameterised in the corresponding columns of the design  
        matrix. `Fac1*Fac2_{2,3}' would refer to the parameter for the  
        interaction of the two factors Fac1 & Fac2, at the 2nd level of the  
        former and the 3rd level of the latter. Other forms are  
         - Simple main effect (level 1)        : <Fac>_{1}  
         - Three way interaction (level 1,2,3) : <Fac1>*<Fac2>*<Fac3>_{1,2,3}  
         - Two way factor interaction by covariate interaction :  
                                               : <Cov>@<Fac1>*<Fac2>_{1,1}  
         - Column 3 of prespecified DesMtx block (if unnamed)  
                                               : <X> [1]  
        The special characters `_*()[]{}' are recognised by the scaling  
        function (spm_DesMtx('sca',...), and should therefore be avoided  
        when naming effects and covariates.  
         
         
        INDEX: An Integer Index matrix is returned if only a single block of  
        design matrix is being computed (single set of parameters). It  
        indexes the actual order of the effect levels in the design matrix block.  
        (Factor levels are introduced in order, regardless of order of  
        appearance in the factor index matrices, so that the parameters  
        vector has a sensible order.) This is used to aid recursion.  
         
        Similarly idx,jdx & kdx are indexes returned for a single block of  
        design matrix consisting of unconstrained factor effects ('-' or '~').  
        These indexes map I and Index (in a similar fashion to the `unique`  
        function) as follows:  
         - idx & jdx are such that I = Index(:,jdx)' and  Index = I(idx,:)'  
           where vector I is given as a column vector  
         - If the "ignore zeros" constraint '~' is used, then kdx indexes the  
           non-zero (combinations) of factor levels, such that  
                            I(kdx,:) = Index(:,jdx)' and  Index == I(kdx(idx),:)'  
         
                                  ----------------  
         
        The design matrix scaling feature is designed to return a scaled  
        version of a design matrix, with values in [-1,1], suitable for  
        visualisation. Special care is taken to apply the same normalisation  
        to blocks of design matrix reflecting a single effect, to preserve  
        appropriate relationships between columns. Identification of effects  
        corresponding to columns of design matrix portions is via the parameter  
        names matrices. The design matrix may be passed in any number of  
        parts, provided the corresponding parameter names are given. It is  
        assumed that the block representing an effect is contained within a  
        single partition. Partitions supplied without corresponding parameter  
        names are scaled on a column by column basis, the parameters labelled as  
        <UnSpec> in the returned nPnames matrix.  
          
        Effects are identified using the special characters `_*()[]{}' used in  
        parameter naming as follows: (here ? is a wildcard)  
              - ?(?)          - general  block (column normalised)  
              - ?[?]          - specific block (block normalised)  
              - ?_{?}         - main effect or interaction of main effects  
              - ?@?_{?}       - factor by covariate interaction  
        Blocks are identified by looking for runs of parameters of the same type  
        with the same names: E.g. a block of main effects for factor 'Fac1'  
        would have names like Fac1_{?}.  
          
        Scaling is as follows:  
              * fMRI blocks are scaled around zero to lie in [-1,1]  
              * No scaling is carried out if max(abs(tX(:))) is in [.4,1]  
                This protects dummy variables from normalisation, even if  
                using implicit sum-to-zero constraints.  
              * If the block has a single value, it's replaced by 1's  
              * FxC blocks are normalised so the covariate values cover [-1,1]  
                but leaving zeros as zero.  
              * Otherwise, block is scaled to cover [-1,1].  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_DesMtx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DesMtx", *args, **kwargs)
