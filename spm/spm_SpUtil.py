from spm.__wrapper__ import Runtime


def spm_SpUtil(*args, **kwargs):
    """
      Space matrix utilities  
        FORMAT varargout = spm_SpUtil(action,varargin)  
         
       _______________________________________________________________________  
         
        spm_SpUtil is a multi-function function containing various utilities  
        for Design matrix and contrast construction and manipulation. In  
        general, it accepts design matrices as plain matrices or as space  
        structures setup by spm_sp.  
         
        Many of the space utilities are computed using an SVD of the design  
        matrix. The advantage of using space structures is that the svd of  
        the design matrix is stored in the space structure, thereby saving  
        unnecessary repeated computation of the SVD. This presents a  
        considerable efficiency gain for large design matrices.  
         
        Note that when space structures are passed as arguments is is  
        assumed that their basic fields are filled in. See spm_sp for  
        details of (design) space structures and their manipulation.  
         
        Quick Reference    :  
       ---------------------  
        ('isCon',x,c)      :  
        ('allCon',x,c)     :  
        ('ConR',x,c)       :  
        ('ConO',x,c)       :  
        ('size',x,dim)     :  
        ('iX0check',i0,sL) :  
       ---------------------  
        ('i0->c',x,i0)     : Out : c  
        ('c->Tsp',x,c)     : Out : [X1o [X0]]  
        ('+c->Tsp',x,c)    : Out : [ukX1o [ukX0]]  
        ('i0->x1o',x,i0)   : Use ('i0->c',x,i0) and ('c->Tsp',X,c)  
        ('+i0->x1o',x,i0)  : Use ('i0->c',x,i0) and ('+c->Tsp',X,c)  
        ('X0->c',x,X0)     :~   
        ('+X0->c',x,cukX0) :~   
       ---------------------  
        ('trRV',x[,V])     :  
        ('trMV',x[,V])     :  
        ('i0->edf',x,i0,V) :  
         
       ---------------------  
         
        Improvement compared to the spm99 beta version :  
         
        Improvements in df computation using spm_SpUtil('trRV',x[,V]) and  
        spm_SpUtil('trMV',sX [,V]). The degrees of freedom computation requires  
        in general that the trace of RV and of RVRV be computed, where R is a  
        projector onto either a sub space of the design space or the residual  
        space, namely the space that is orthogonal to the design space. V is  
        the (estimated or assumed) variance covariance matrix and is a number  
        of scans by number of scans matrix which can be huge in some cases. We  
        have (thanks to S Rouquette and JB) speed up this computation   
        by using matlab built in functions of the frobenius norm and some theorems  
        on trace computations.   
         
        ======================================================================  
         
        FORMAT i = spm_SpUtil('isCon',x,c)  
        Tests whether weight vectors specify contrasts  
        x   - Design matrix X, or space structure of X  
        c   - contrast matrix (I.e. matrix of contrast weights, contrasts in columns)  
              Must have column dimension matching that of X  
              [defaults to eye(size(X,2)) to test uniqueness of parameter estimates]  
        i   - logical row vector indicating estimability of contrasts in c  
         
        A linear combination of the parameter estimates is a contrast if and  
        only if the weight vector is in the space spanned by the rows of X.  
         
        The algorithm works by regressing the contrast weight vectors using  
        design matrix X' (X transposed). Any contrast weight vectors will be  
        fitted exactly by this procedure, leaving zero residual. Parameter  
        tol is the tolerance applied when searching for zero residuals.  
         
        Christensen R (1996)  
          "Plane Answers to Complex Questions"  
           2nd Ed. Springer-Verlag, New York  
         
        Andrade A, Paradis AL, Rouquette S and Poline JB, NeuroImage 9, 1999  
                                  ----------------  
         
        FORMAT i = spm_SpUtil('allCon',x,c)  
        Tests whether all weight vectors specify contrasts:  
        Same as all(spm_SpUtil('isCon',x,c)).  
         
                                  ----------------  
         
        FORMAT r = spm_SpUtil('ConR',x,c)  
        Assess orthogonality of contrasts (wirit the data)  
        x   - Design matrix X, or space structure of X  
        c   - contrast matrix (I.e. matrix of contrast weights, contrasts in columns)  
              Must have column dimension matching that of X  
              defaults to eye(size(X,2)) to test independence of parameter estimates  
        r   - Contrast correlation matrix, of dimension the number of contrasts.  
         
        For the general linear model Y = X*B + E, a contrast weight vector c  
        defines a contrast c*B. This is estimated by c*b, where b are the  
        least squares estimates of B given by b=pinv(X)*Y. Thus, c*b = w*Y,  
        where weight vector w is given by w=c*pinv(X); Since the data are  
        assumed independent, two contrasts are independent if the  
        corresponding weight vectors are orthogonal.  
         
        r is the matrix of normalised inner products between the weight  
        vectors corresponding to the contrasts. For iid E, r is the  
        correlation matrix of the contrasts.  
         
        The logical matrix ~r will be true for orthogonal pairs of contrasts.  
          
                                  ----------------  
         
        FORMAT r = spm_SpUtil('ConO',x,c)  
        Assess orthogonality of contrasts (wirit the data)  
        x   - Design matrix X, or space structure of X  
        c   - contrast matrix (I.e. matrix of contrast weights, contrasts in columns)  
              Must have column dimension matching that of X  
              [defaults to eye(size(X,2)) to test uniqueness of parameter estimates]  
        r   - Contrast orthogonality matrix, of dimension the number of contrasts.  
         
        This is the same as ~spm_SpUtil('ConR',X,c), but uses a quicker  
        algorithm by looking at the orthogonality of the subspaces of the  
        design space which are implied by the contrasts:  
              r = abs(c*X'*X*c')<tol  
          
                                  ----------------  
         
        FORMAT c = spm_SpUtil('i0->c',x,i0)  
        Return F-contrast for specified design matrix partition  
        x   - Design matrix X, or space structure of X  
        i0  - column indices of null hypothesis design matrix  
         
        This functionality returns a rank n mxp matrix of contrasts suitable  
        for an extra-sum-of-squares F-test comparing the design X, with a  
        reduced design. The design matrix for the reduced design is X0 =  
        X(:,i0), a reduction of n degrees of freedom.  
         
        The algorithm, due to J-B, and derived from Christensen, computes the  
        contrasts as an orthonormal basis set for the rows of the  
        hypothesised redundant columns of the design matrix, after  
        orthogonalisation with respect to X0. For non-unique designs, there  
        are a variety of ways to produce equivalent F-contrasts. This method  
        produces contrasts with non-zero weights only for the hypothesised  
        redundant columns.  
         
                                  ----------------  
          
        case {'x0->c'}                %-   
        FORMAT c = spm_SpUtil('X0->c',sX,X0)  
                                  ----------------  
         
        FORMAT [X1,X0] = spm_SpUtil('c->TSp',X,c)  
        Orthogonalised partitioning of design space implied by F-contrast  
        x   - Design matrix X, or space structure of X  
        c   - contrast matrix (I.e. matrix of contrast weights, contrasts in columns)  
              Must have column dimension matching that of X  
        X1o - contrast space - design matrix corresponding according to contrast  
              (orthogonalised wirit X0)  
        X0  - matrix reduced according to null hypothesis  
              (of same size as X but rank deficient)  
        FORMAT [uX1,uX0] = spm_SpUtil('c->TSp+',X,c)  
               + version to deal with the X1o and X0 partitions in the "uk basis"  
         
        ( Note that unless X0 is reduced to a set of linearely independent   )  
        ( vectors, c will only be contained in the null space of X0.  If X0  )  
        ( is "reduced", then the "parent" space of c must be reduced as well )  
        ( for c to be the actual null space of X0.                           )  
         
        This functionality returns a design matrix subpartition whose columns  
        span the hypothesised null design space of a given contrast. Note  
        that X1 is orthogonal(ised) to X0, reflecting the situation when an  
        F-contrast is tested using the extra sum-of-squares principle (when  
        the extra distance in the hypothesised null space is measured  
        orthogonal to the space of X0).  
         
        Note that the null space design matrix will probably not be a simple  
        sub-partition of the full design matrix, although the space spanned  
        will be the same.  
         
                                  ----------------  
         
        FORMAT X1 = spm_SpUtil('i0->x1o',X,i0)  
        x   - Design matrix X, or space structure of X  
        i0  - Columns of X that make up X0 - the reduced model (Ho:B1=0)  
        X1  - Hypothesised null design space, i.e. that part of X orthogonal to X0  
        This offers the same functionality as the 'c->TSp' option, but for  
        simple reduced models formed from the columns of X.  
         
        FORMAT X1 = spm_SpUtil('i0->x1o+',X,i0)  
               + version to deal with the X1o and X0 partitions in the "uk basis"  
         
                                  ----------------  
         
        FORMAT [trRV,trRVRV] = spm_SpUtil('trRV',x[,V])  
        trace(RV) & trace(RVRV) - used in df calculation  
        x      - Design matrix X, or space structure of X  
        V      - V matrix [default eye] (trRV == trRVRV if V==eye, since R idempotent)  
        trRV   - trace(R*V),     computed efficiently  
        trRVRV - trace(R*V*R*V), computed efficiently  
        This uses the Karl's cunning understanding of the trace:  
                     (tr(A*B) = sum(sum(A'*B)).  
        If the space of X is set, then algorithm uses x.u to avoid extra computation.  
         
                                  ----------------  
         
        FORMAT [trMV, trMVMV]] = spm_SpUtil('trMV',x[,V])  
        trace(MV) & trace(MVMV) if two output arguments.  
        x      - Design matrix X, or space structure of X  
        V      - V matrix [default eye] (trMV == trMVMV if V==eye, since M idempotent)  
        trMV   - trace(M*V),     computed efficiently  
        trMVMV - trace(M*V*M*V), computed efficiently  
        Again, this uses the Karl's cunning understanding of the trace:  
                     (tr(A*B) = sum(sum(A'.*B)).  
        If the space of X is set, then algorithm uses x.u to avoid extra computation.  
         
                                  ----------------  
         
        OBSOLETE use FcUtil('H') for spm_SpUtil('c->H',x,c)   
        Extra sum of squares matrix O for beta's from contrast  
        x   - Design matrix X, or space structure of X  
        c   - contrast matrix (I.e. matrix of contrast weights, contrasts in columns)  
              Must have column dimension matching that of X  
        O   - Matrix such that b'*O*b = extra sum of squares for F-test of contrast c  
         
                                  ----------------  
         
        OBSOLETE use spm_sp('=='...) for spm_SpUtil('c==X1o',x,c) {or 'cxpequi'}  
        x   - Design matrix X, or space structure of X  
        c   - contrast matrix (I.e. matrix of contrast weights, contrasts in columns)  
              Must have column dimension matching that of X  
        b   - True is c is a spanning set for space of X  
              (I.e. if contrast and space test the same thing)  
         
                                  ----------------  
         
        FORMAT [df1,df2] = spm_SpUtil('i0->edf',x,i0,V) {or 'edf'}  
        (effective) df1 and df2 the residual df for the projector onto the  
        null space of x' (residual forming projector) and the numerator of  
        the F-test where i0 are the columns for the null hypothesis model.  
        x   - Design matrix X, or space structure of X  
        i0  - Columns of X corresponding to X0 partition X = [X1,X0] & with  
              parameters B = [B1;B0]. Ho:B1=0  
        V   - V matrix  
         
                                  ----------------  
         
        FORMAT  sz           = spm_SpUtil('size',x,dim)  
        FORMAT [sz1,sz2,...] = spm_SpUtil('size',x)  
        Returns size of design matrix  
        (Like MatLab's `size`, but copes with design matrices inside structures.)  
        x   - Design matrix X, or structure containing design matrix in field X  
              (Structure needn't be a space structure.)  
        dim - dimension which to size  
        sz  - size  
         
       _______________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_SpUtil.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_SpUtil", *args, **kwargs)
