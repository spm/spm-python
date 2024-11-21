from spm.__wrapper__ import Runtime


def spm_sp(*args, **kwargs):
    """
      Orthogonal (design) matrix space setting & manipulation  
        FORMAT varargout = spm_spc(action,varargin)  
         
        This function computes the different projectors related to the row  
        and column spaces X. It should be used to avoid redundant computation  
        of svd on large X matrix.  It is divided into actions that set up the  
        space, (Create,Set,...) and actions that compute projections (pinv,  
        pinvXpX, pinvXXp, ...) This is motivated by the problem of rounding  
        errors that can invalidate some computation and is a tool to work  
        with spaces.  
         
        The only thing that is not easily computed is the null space of  
        the line of X (assuming size(X,1) > size(X,2)).  
        To get this space (a basis of it or a projector on it) use spm_sp on X'.  
         
        The only restriction on the use of the space structure is when X is  
        so big that you cannot fit X and its svd in memory at the same time.  
        Otherwise, the use of spm_sp will generally speed up computations and  
        optimise memory use.  
         
        Note that since the design matrix is stored in the space structure,  
        there is no need to keep a separate copy of it.  
         
                                  ----------------  
         
        The structure is:  
          x = struct(...  
              'X',    [],...      % Mtx  
              'tol',  [],...      % tolerance  
              'ds',   [],...      % vectors of singular values   
              'u',    [],...      % u as in X = u*diag(ds)*v'  
              'v',    [],...      % v as in X = u*diag(ds)*v'  
              'rk',   [],...      % rank  
              'oP',   [],...      % orthogonal projector on X  
              'oPp',  [],...      % orthogonal projector on X'  
              'ups',  [],...      % space in which this one is embedded  
              'sus',  []);        % subspace  
         
        The basic required fields are X, tol, ds, u, v, rk.  
         
        =========================================================================  
         
        FORMAT x = spm_sp('Set',X)  
        Set up space structure, storing matrix, singular values, rank & tolerance  
        X - a (design) matrix (2D)  
        x - the corresponding space structure, with basic fields filled in  
            The SVD is an "economy size" svd, using MatLab's svd(X,0)  
         
         
        FORMAT r = spm_sp('oP',x[,Y])  
        FORMAT r = spm_sp('oPp',x[,Y])  
        Return orthogonal projectors, or orthogonal projection of data Y (if passed)  
        x - space structure of matrix X  
        r - ('oP' usage)  ortho. projection matrix projecting into column space of x.X  
          - ('oPp' usage) ortho. projection matrix projecting into row space of x.X  
        Y - data (optional)  
          - If data are specified then the corresponding projection of data is  
            returned. This is usually more efficient that computing and applying  
            the projection matrix directly.  
         
         
        FORMAT pX = spm_sp('pinv',x)  
        Returns a pseudo-inverse of X - pinv(X) - computed efficiently  
        x - space structure of matrix X  
        pX - pseudo-inverse of X  
        This is the same as MatLab's pinv - the Moore-Penrose pseudoinverse  
        ( Note that because size(pinv(X)) == size(X'), it is not generally  )  
        ( useful to compute pinv(X)*Data sequentially (as is the case for   )  
        ( 'res' or 'oP')                                                    )  
         
         
        FORMAT pXpX = spm_sp('pinvxpx',x)  
        Returns a pseudo-inverse of X'X - pinv(X'*X) - computed efficiently  
        x    - space structure of matrix X  
        pXpX - pseudo-inverse of (X'X)  
        ( Note that because size(pinv(X'*X)) == [size(X,2) size(X,2)],      )  
        ( it is not useful to compute pinv(X'X)*Data sequentially unless    )  
        ( size(X,1) < size(X,2)                                             )  
         
         
        FORMAT XpX = spm_sp('xpx',x)  
        Returns (X'X) - computed efficiently  
        x    - space structure of matrix X  
        XpX  - (X'X)  
         
         
        FORMAT pXXp = spm_sp('pinvxxp',x)  
        Returns a pseudo-inverse of XX' - pinv(X*X') - computed efficiently  
        x    - space structure of matrix X  
        pXXp - pseudo-inverse of (XX')  
         
         
        FORMAT XXp = spm_sp('xxp',x)  
        Returns (XX') - computed efficiently  
        x    - space structure of matrix X  
        XXp  - (XX')  
         
         
        FORMAT b = spm_sp('isinsp',x,c[,tol])  
        FORMAT b = spm_sp('isinspp',x,c[,tol])  
        Check whether vectors c are in the column/row space of X  
        x   - space structure of matrix X  
        c   - vector(s) (Multiple vectors passed as a matrix)  
        tol - (optional) tolerance (for rounding error)  
               [defaults to tolerance specified in space structure: x.tol]  
        b   - ('isinsp'  usage) true if c is in the column space of X  
            - ('isinspp' usage) true if c is in the column space of X  
          
        FORMAT b = spm_sp('eachinsp',x,c[,tol])  
        FORMAT b = spm_sp('eachinspp',x,c[,tol])  
        Same as 'isinsp' and 'isinspp' but returns a logical row vector of  
        length size(c,2).  
         
        FORMAT N = spm_sp('n',x)  
        Simply returns the null space of matrix X (same as matlab NULL)  
        (Null space = vectors associated with zero eigenvalues)  
        x - space structure of matrix X  
        N - null space  
         
         
        FORMAT r = spm_sp('nop',x[,Y])  
        Orthogonal projector onto null space of X, or projection of data Y (if passed)  
        x - space structure of matrix X  
        Y - (optional) data  
        r - (if no Y passed) orthogonal projection matrix  into the null space of X  
          - (if Y passed   ) orthogonal projection of data into the null space of X  
        ( Note that if xp = spm_sp('set',x.X'), we have:                    )  
        (       spm_sp('nop',x) == spm_sp('res',xp)                      )  
        ( or, equivalently:                                                 )  
        (       spm_sp('nop',x) + spm_sp('oP',xp) == eye(size(xp.X,1));  )  
         
         
        FORMAT r = spm_sp('res',x[,Y])  
        Returns residual formaing matrix wirit column space of X, or residuals (if Y)  
        x - space structure of matrix X  
        Y - (optional) data  
        r - (if no Y passed) residual forming matrix for design matrix X  
          - (if Y passed   ) residuals, i.e. residual forming matrix times data  
                           ( This will be more efficient than  
                           ( spm_sp('res',x)*Data, when size(X,1) > size(X,2)  
        Note that this can also be seen as the orthogonal projector onto the  
        null space of x.X' (which is not generally computed in svd, unless  
        size(X,1) < size(X,2)).  
         
         
        FORMAT oX  = spm_sp('ox', x)  
        FORMAT oXp = spm_sp('oxp',x)  
        Returns an orthonormal basis for X ('ox' usage) or X' ('oxp' usage)  
        x   - space structure of matrix X  
        oX  - orthonormal basis for X - same as orth(x.X)  
        xOp - *an* orthonormal for X' (but not the same as orth(x.X'))  
         
         
        FORMAT b = spm_sp('isspc',x)  
        Check a variable is a structure with the right fields for a space structure  
        x - candidate variable  
        b - true if x is a structure with fieldnames corresponding to spm_sp('create')  
         
         
        FORMAT [b,e] = spm_sp('issetspc',x)  
        Test whether a variable is a space structure with the basic fields set  
        x - candidate variable  
        b - true is x is a structure with fieldnames corresponding to  
            spm_sp('Create'), which has it's basic fields filled in.  
        e - string describing why x fails the issetspc test (if it does)  
        This is simply a gateway function combining spm_sp('isspc',x) with  
        the internal subfunction sf_isset, which checks that the basic fields  
        are not empty. See sf_isset (below).  
         
       --------------------------------------------------------------------------  
        SUBFUNCTIONS:  
         
        FORMAT b = sf_isset(x)  
        Checks that the basic fields are non-empty (doesn't check they're right!)  
        x - space structure  
        b - true if the basic fields are non-empty  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_sp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_sp", *args, **kwargs)
