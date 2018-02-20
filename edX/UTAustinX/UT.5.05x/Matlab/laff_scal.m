function [x_out] = laff_scal(alpha,x)
  
    [rows_x, cols_x] = size(x);
    
    if ~isscalar(alpha)
        x_out = 'FAILED';
        return
    end
    
    if ~isvector(x)
        x_out = 'FAILED';
        return
    end
    
    if (cols_x == 1) % we have a column vector
        for i = 1:rows_x
            x(i) = alpha * x(i);
        end
    else
        for j = 1:cols_x
            x(j) = alpha*x(j);
        end
    end
    
    x_out = x;
end
